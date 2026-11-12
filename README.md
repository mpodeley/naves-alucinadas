# Naves alucinadas

Investigación sobre el testimonio de Bob Lazar de 1989: qué percibió de primera mano, qué leyó o le contaron, y por qué canal llegó el relato al público. Parte de la idea de las "naves estructuralmente alucinadas" del archivo 009 de HERCULANEUM-299 y la contrasta con una explicación más barata: una exhibición controlada.

Estado al 12 de noviembre de 2026: cinco notas de investigación, un modelo de comparación de hipótesis y un ensayo, publicado en <https://mpodeley.github.io/naves-alucinadas/>.

## Qué hay

| Ruta | Contenido |
|---|---|
| `ensayo.md` | El ensayo. Fuente de `index.html`. |
| `index.html` | El ensayo en una página autocontenida. Lo genera `armar.sh`. |
| `notas/01-vallee-diarios.md` | Knapp, Lear, Lazar y DeLonge en los diarios de Vallée (tomos 3 a 6), con 50 citas cotejadas. |
| `notas/02-lazar-testimonio.md` | Inventario del testimonio sobre transcripciones de 1989 a 2026. |
| `notas/03-precedentes-engano.md` | Yankee Blue, Kirtland, Howe, Moore y el estado del tomo II de AARO. |
| `notas/04-knapp-cronologia.md` | Cronología de George Knapp 1979–2026 y red de 89 vínculos. |
| `notas/05-papoose-y-cronologia.md` | Papoose, programas reales de 1986 a 1990 y la cronología de la contratación. |
| `modelo/rasgos.json` | Cinco hipótesis, cuatro priors y 16 rasgos con un nivel por hipótesis y su razón. |
| `modelo/comparar.py` | Calcula posteriores, quita un grupo por vez y sortea los niveles. |
| `modelo/resultado.md` | Salida del modelo. |
| `datos/red.csv` | La red de vínculos, extraída de la nota 04. |

## Cómo se rehace

```bash
./armar.sh
```

Corre el modelo, extrae la red y arma `index.html` con pandoc. Para cambiar un juicio del modelo se edita `modelo/rasgos.json`; el código no tiene casos especiales.

## Cómo se hizo

Cada nota la escribió un agente de investigación con un encargo acotado: fuentes primarias antes que resúmenes, cita textual con fecha, y una etiqueta para lo documentado, lo dicho por una sola parte y lo inferido. El ensayo se cotejó después, frase por frase, contra las notas, y sus citas contra las páginas de origen.

## Límites

Las notas citan páginas web leídas el 11 de noviembre de 2026. Las 17 citas que usa el ensayo se cotejaron contra el original al día siguiente; las demás citas de las notas siguen sin ese cotejo. Los diarios de Vallée registran lo que otros le contaron. Los niveles del modelo son juicios de quien lo cargó. El proyecto no afirma nada sobre las intenciones de las personas nombradas.
