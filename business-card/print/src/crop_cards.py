#!/usr/bin/env python3
"""Schneidet die uebergross gerenderten PDFs zentriert auf exakt 88x58mm (Bleed)
und setzt TrimBox = 85x55mm (Endformat)."""
import sys, pikepdf

MM = 72 / 25.4
BLEED_W, BLEED_H = 88 * MM, 58 * MM      # Endformat inkl. Beschnitt
TRIM_W,  TRIM_H  = 85 * MM, 55 * MM      # Endformat (Schnittkante)

for path in sys.argv[1:]:
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    page = pdf.pages[0]
    mb = [float(x) for x in page.MediaBox]
    cx = (mb[0] + mb[2]) / 2
    cy = (mb[1] + mb[3]) / 2

    def box(w, h):
        return [round(cx - w/2, 3), round(cy - h/2, 3),
                round(cx + w/2, 3), round(cy + h/2, 3)]

    bleed = box(BLEED_W, BLEED_H)
    trim  = box(TRIM_W,  TRIM_H)
    page.MediaBox = bleed
    page.CropBox  = bleed
    page.BleedBox = bleed
    page.TrimBox  = trim
    pdf.save(path)
    pdf.close()
    w = (bleed[2]-bleed[0])/MM; h = (bleed[3]-bleed[1])/MM
    print(f"{path}: MediaBox {w:.3f} x {h:.3f} mm  |  TrimBox 85 x 55 mm")
