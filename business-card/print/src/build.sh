#!/usr/bin/env bash
# Erzeugt die druckreifen Visitenkarten (RGB + CMYK) aus der Design-Quelle.
#
# Voraussetzungen: Google Chrome, Ghostscript (brew install ghostscript),
#                  Python mit pikepdf (pip install pikepdf).
# pikepdf-Python via PYTHON-Env setzen, falls nicht global installiert:
#   PYTHON=/pfad/zu/venv/bin/python ./build.sh
set -euo pipefail
cd "$(dirname "$0")"                      # .../business-card/print/src
PRINT="$(cd .. && pwd)"                   # .../business-card/print
PY="${PYTHON:-python3}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CMYK_ICC_SRC="/System/Library/ColorSync/Profiles/Generic CMYK Profile.icc"

mkdir -p "$PRINT/rgb" "$PRINT/cmyk"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cp "$CMYK_ICC_SRC" "$TMP/cmyk.icc"

echo "1/5  Print-HTMLs (88x58 mit 3mm Uebermalung) erzeugen"
"$PY" build_cards.py

for s in front back; do
  echo "2/5  $s: Chrome -> Vektor-PDF"
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$TMP/$s.pdf" "file://$PWD/print-$s.html" 2>/dev/null

  echo "3/5  $s: Schrift in Pfade wandeln (RGB)"
  gs -q -dNOSAFER -o "$PRINT/rgb/visitenkarte-$s.pdf" -sDEVICE=pdfwrite \
     -dNoOutputFonts -dColorConversionStrategy=/LeaveColorUnchanged \
     -dCompatibilityLevel=1.5 "$TMP/$s.pdf"

  echo "4/5  $s: RGB -> CMYK + definierte Plattenwerte"
  gs -q -dNOSAFER -o "$PRINT/cmyk/visitenkarte-$s.pdf" -sDEVICE=pdfwrite \
     -dColorConversionStrategy=/CMYK -sProcessColorModel=DeviceCMYK \
     -sOutputICCProfile="$TMP/cmyk.icc" -dCompatibilityLevel=1.4 \
     "$PRINT/rgb/visitenkarte-$s.pdf"
  "$PY" remap_cmyk.py "$PRINT/cmyk/visitenkarte-$s.pdf" >/dev/null
done

echo "5/5  Boxen exakt setzen (88x58 Media / 85x55 Trim) + Kombi-PDFs"
"$PY" crop_cards.py "$PRINT"/rgb/visitenkarte-{front,back}.pdf "$PRINT"/cmyk/visitenkarte-{front,back}.pdf
for cs in rgb cmyk; do
  "$PY" - "$PRINT/$cs" <<'PY'
import sys, pikepdf
d = sys.argv[1]
out = pikepdf.new()
for s in ("front","back"):
    out.pages.extend(pikepdf.open(f"{d}/visitenkarte-{s}.pdf").pages)
out.save(f"{d}/visitenkarte-vorder-und-rueckseite.pdf")
PY
done
echo "Fertig: $PRINT/rgb/  und  $PRINT/cmyk/"
