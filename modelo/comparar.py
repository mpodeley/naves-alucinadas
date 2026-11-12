#!/usr/bin/env python3
"""Compare hypotheses about a testimony, feature by feature.

Reads modelo/rasgos.json (hypotheses, priors, features with a likelihood level
per hypothesis) and writes modelo/resultado.json and modelo/resultado.md.

The likelihoods are structured judgments, not measurements. The script exists to
make them explicit and to show how much the conclusion depends on each one:

  - features are grouped in clusters; correlated features in a cluster count once
    (their log-likelihoods are averaged) so one fact told three ways is not
    triple-counted;
  - leave-one-cluster-out shows which cluster carries the result;
  - a Monte Carlo jitter moves every level up or down to show how stable the
    ranking is;
  - several prior sets are run side by side.

Usage: python3 modelo/comparar.py [--seed 7] [--draws 20000]
"""
import argparse
import json
import math
import pathlib
import random

HERE = pathlib.Path(__file__).resolve().parent

# Verbal scale -> P(feature | hypothesis). Coarse on purpose.
LEVELS = {
    "casi_nunca": 0.03,
    "raro": 0.15,
    "indiferente": 0.50,
    "esperable": 0.80,
    "casi_seguro": 0.95,
}
ORDER = list(LEVELS)


def logit(p):
    return math.log(p / (1 - p))


def inv_logit(x):
    return 1 / (1 + math.exp(-x))


def cluster_loglik(features, hyps, lik):
    """Mean log-likelihood per cluster, then sum across clusters."""
    clusters = {}
    for f in features:
        clusters.setdefault(f["grupo"], []).append(f)
    out = {}
    for name, feats in clusters.items():
        out[name] = {
            h: sum(math.log(lik(f, h)) for f in feats) / len(feats) for h in hyps
        }
    return out


def posterior(prior, cl, hyps, skip=None):
    logp = {h: math.log(prior[h]) for h in hyps}
    for name, ll in cl.items():
        if name == skip:
            continue
        for h in hyps:
            logp[h] += ll[h]
    m = max(logp.values())
    z = sum(math.exp(v - m) for v in logp.values())
    return {h: math.exp(logp[h] - m) / z for h in hyps}


def base_lik(f, h):
    return LEVELS[f["p"][h]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--draws", type=int, default=20000)
    ap.add_argument("--jitter", type=float, default=1.0,
                    help="sd of the logit noise applied to every likelihood")
    args = ap.parse_args()

    data = json.loads((HERE / "rasgos.json").read_text())
    hyps = [h["id"] for h in data["hipotesis"]]
    label = {h["id"]: h["nombre"] for h in data["hipotesis"]}
    feats = data["rasgos"]

    for f in feats:
        missing = [h for h in hyps if h not in f["p"]]
        bad = [v for v in f["p"].values() if v not in LEVELS]
        if missing or bad:
            raise SystemExit(f"rasgo {f['id']}: faltan {missing}, niveles inválidos {bad}")

    cl = cluster_loglik(feats, hyps, base_lik)
    result = {"hipotesis": label, "priors": {}, "sin_grupo": {}, "montecarlo": {}}

    for pname, prior in data["priors"].items():
        s = sum(prior.values())
        prior = {h: prior[h] / s for h in hyps}
        result["priors"][pname] = {"prior": prior, "posterior": posterior(prior, cl, hyps)}

    ref_name = data["prior_de_referencia"]
    ref = result["priors"][ref_name]["prior"]
    for name in cl:
        result["sin_grupo"][name] = posterior(ref, cl, hyps, skip=name)

    # Monte Carlo: jitter every likelihood in logit space, recompute.
    rng = random.Random(args.seed)
    wins = {h: 0 for h in hyps}
    samples = {h: [] for h in hyps}
    for _ in range(args.draws):
        noise = {(f["id"], h): rng.gauss(0, args.jitter) for f in feats for h in hyps}

        def lik(f, h):
            p = inv_logit(logit(LEVELS[f["p"][h]]) + noise[(f["id"], h)])
            return min(max(p, 1e-4), 1 - 1e-4)

        post = posterior(ref, cluster_loglik(feats, hyps, lik), hyps)
        wins[max(post, key=post.get)] += 1
        for h in hyps:
            samples[h].append(post[h])
    for h in hyps:
        xs = sorted(samples[h])
        result["montecarlo"][h] = {
            "gana": wins[h] / args.draws,
            "p05": xs[int(0.05 * len(xs))],
            "p50": xs[int(0.50 * len(xs))],
            "p95": xs[int(0.95 * len(xs))],
        }
    result["parametros"] = {"seed": args.seed, "draws": args.draws, "jitter": args.jitter,
                            "prior_de_referencia": ref_name, "niveles": LEVELS}

    # Per-feature evidence weight between two named hypotheses (decibans).
    a, b = data["contraste"]
    result["peso_por_rasgo"] = [
        {"id": f["id"], "grupo": f["grupo"], "rasgo": f["rasgo"],
         "db": 10 * math.log10(base_lik(f, a) / base_lik(f, b))}
        for f in feats
    ]
    result["contraste"] = [a, b]

    (HERE / "resultado.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))

    pct = lambda x: f"{100 * x:.0f}%" if x >= 0.005 else "<1%"
    L = ["# Resultado del modelo", "",
         "Los números ordenan juicios, no miden nada. Ver `comparar.py` y `rasgos.json`.", "",
         "## Posterior según el prior", "",
         "| Prior | " + " | ".join(label[h] for h in hyps) + " |",
         "|---|" + "---|" * len(hyps)]
    for pname, r in result["priors"].items():
        L.append(f"| {pname} (prior) | " + " | ".join(pct(r["prior"][h]) for h in hyps) + " |")
        L.append(f"| {pname} (posterior) | " + " | ".join(pct(r["posterior"][h]) for h in hyps) + " |")
    L += ["", f"## Sin un grupo de rasgos (prior: {ref_name})", "",
          "| Grupo quitado | " + " | ".join(label[h] for h in hyps) + " |",
          "|---|" + "---|" * len(hyps)]
    for name, post in result["sin_grupo"].items():
        L.append(f"| {name} | " + " | ".join(pct(post[h]) for h in hyps) + " |")
    L += ["", f"## Estabilidad ({args.draws} sorteos, ruido logit sd {args.jitter})", "",
          "| Hipótesis | Queda primera | p05 | mediana | p95 |", "|---|---|---|---|---|"]
    for h in hyps:
        m = result["montecarlo"][h]
        L.append(f"| {label[h]} | {pct(m['gana'])} | {pct(m['p05'])} | {pct(m['p50'])} | {pct(m['p95'])} |")
    L += ["", f"## Peso de cada rasgo: {label[a]} contra {label[b]}", "",
          "Decibanes; positivo favorece a la primera. 10 dB equivale a una razón de 10 a 1.", "",
          "| Rasgo | Grupo | dB |", "|---|---|---|"]
    for w in sorted(result["peso_por_rasgo"], key=lambda w: -w["db"]):
        L.append(f"| {w['rasgo']} | {w['grupo']} | {w['db']:+.1f} |")
    (HERE / "resultado.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
