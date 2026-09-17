#!/usr/bin/env python3
"""Setzt im CMYK-PDF zwei Farben auf definierte Plattenwerte:
   - Anthrazit (~C81 M73 Y66 K63) -> Rich Black C60 M40 Y40 K100
   - QR/reines Schwarz (~C74 M71 Y65 K80) -> K-only C0 M0 Y0 K100
Alle anderen Farben bleiben unveraendert."""
import sys, re, pikepdf

def near(v, target, tol=0.04):
    return all(abs(a-b) <= tol for a, b in zip(v, target))

ANTHRA = (0.81, 0.73, 0.66, 0.63)   # -> rich black
QRBLK  = (0.74, 0.71, 0.65, 0.80)   # -> K-only
RICH   = "0.6 0.4 0.4 1"
KONLY  = "0 0 0 1"

NUM = r'([0-9]*\.?[0-9]+)'
PAT = re.compile(rf'{NUM} {NUM} {NUM} {NUM} (k|K)\b')

for path in sys.argv[1:]:
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    page = pdf.pages[0]
    data = page.Contents.read_bytes().decode("latin1")
    n_rich = n_k = 0
    def repl(m):
        global n_rich, n_k
        v = tuple(float(m.group(i)) for i in range(1, 5))
        op = m.group(5)
        if near(v, ANTHRA):
            n_rich += 1; return f"{RICH} {op}"
        if near(v, QRBLK):
            n_k += 1; return f"{KONLY} {op}"
        return m.group(0)
    new = PAT.sub(repl, data)
    page.Contents.write(new.encode("latin1"))
    pdf.save(path)
    pdf.close()
    print(f"{path}: Anthrazit->RichBlack x{n_rich}, Schwarz->K-only x{n_k}")
