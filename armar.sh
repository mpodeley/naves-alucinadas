#!/usr/bin/env bash
# Rebuild everything derived: model output, network CSV, self-contained index.html.
set -euo pipefail
cd "$(dirname "$0")"

python3 modelo/comparar.py > /dev/null

# Network edge list: the fenced csv block in notas/04 is the source of truth.
mkdir -p datos
python3 - <<'EOF'
import pathlib, re
text = pathlib.Path("notas/04-knapp-cronologia.md").read_text()
block = re.search(r"```csv\n(.*?)```", text, re.S).group(1)
pathlib.Path("datos/red.csv").write_text(block)
EOF

pandoc ensayo.md --standalone --embed-resources \
  --include-in-header=plantilla/estilo.html \
  --metadata pagetitle="Naves alucinadas" \
  --output index.html
echo "index.html $(wc -c < index.html) bytes"
