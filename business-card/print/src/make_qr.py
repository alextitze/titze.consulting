#!/usr/bin/env python3
"""Erzeugt business-card/qr-vcard.svg aus der Quelle marco-titze.vcf (Repo-Wurzel).
Fehlerkorrektur 'M', Anthrazit-Module, gleiche Optik wie zuvor (segno-SVG)."""
import segno, pathlib

HERE = pathlib.Path(__file__).resolve().parent      # .../business-card/print/src
ROOT = HERE.parents[2]                               # Repo-Wurzel
vcf  = (ROOT / "marco-titze.vcf").read_text().splitlines()
payload = "\r\n".join(l for l in vcf if l.strip())   # vCard: CRLF-Zeilen

qr = segno.make(payload, error="m")
out = ROOT / "business-card" / "qr-vcard.svg"
qr.save(str(out), kind="svg", scale=1, border=4, dark="#14181a")
print(f"QR neu -> {out}  (Version {qr.version}, EC {qr.error.upper()}, "
      f"{qr.symbol_size(scale=1, border=0)[0]} Module)")
