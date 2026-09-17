#!/usr/bin/env python3
"""Baut druckreife Print-HTMLs (88x58mm, Bleed) aus der Design-Quelle."""
import re, pathlib

# Pfade relativ zum Skript ableiten -> portabel (Skript liegt in business-card/print/src/)
HERE = pathlib.Path(__file__).resolve().parent          # .../business-card/print/src
ROOT = HERE.parents[2]                                   # Repo-Wurzel
OUT  = HERE                                              # Print-HTMLs landen neben dem Skript
FONTS = ROOT / "assets" / "fonts"

# --- QR aus Quelle lesen, auf reines Schwarz setzen, viewBox ergaenzen (bleibt Vektor) ---
qr_src = (ROOT / "business-card" / "qr-vcard.svg").read_text()
m = re.search(r'd="([^"]+)"', qr_src)
assert m, "QR-Pfad nicht gefunden"
qr_path = m.group(1)
# viewBox aus der Quell-Breite ableiten (inkl. Ruhezone) -> QR wird NICHT abgeschnitten
mw = re.search(r'width="(\d+)"', qr_src)
qr_box = int(mw.group(1)) if mw else 61
QR_SVG = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {qr_box} {qr_box}" '
          f'width="22mm" height="22mm" class="qr">'
          f'<path stroke="#000000" d="{qr_path}"/></svg>')

FONTFACE = f"""
@font-face{{font-family:'Archivo';font-style:normal;font-weight:100 900;
  src:url('file://{FONTS}/archivo.woff2') format('woff2');}}
@font-face{{font-family:'IBM Plex Mono';font-style:normal;font-weight:400;
  src:url('file://{FONTS}/ibm-plex-mono-400.woff2') format('woff2');}}
@font-face{{font-family:'IBM Plex Mono';font-style:normal;font-weight:500;
  src:url('file://{FONTS}/ibm-plex-mono-500.woff2') format('woff2');}}
"""

# Groesser rendern: 91x61mm (3mm Uebermalung je Seite), spaeter exakt auf 88x58 zuschneiden.
BASE = """
*{-webkit-print-color-adjust:exact;print-color-adjust:exact;box-sizing:border-box;}
html,body{margin:0;padding:0;}
@page{size:91mm 61mm;margin:0;}
.page{width:91mm;height:61mm;overflow:hidden;position:relative;}
"""

LOGO = ('<svg width="{s}" height="{s}" viewBox="0 0 62 62" fill="none">'
        '<circle cx="31" cy="31" r="29" stroke="{ring}" stroke-width="4"></circle>'
        '<circle cx="31" cy="31" r="18" stroke="{red}" stroke-width="7"></circle>'
        '<path d="M31 7A24 24 0 0 1 55 31" stroke="{green}" stroke-width="5" stroke-linecap="butt"></path>'
        '</svg>')

# ---------- VORDERSEITE ----------
front = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE}
.front{{background:#14181A;height:100%;display:flex;flex-direction:column;
  justify-content:space-between;padding:12mm 11mm;
  font-family:'Archivo',sans-serif;color:#FBFAF7;}}
.front svg{{display:block;}}
.front__word{{display:flex;align-items:baseline;font-size:26px;letter-spacing:-0.028em;color:#FBFAF7;}}
.front__word .name{{font-weight:600;}}
.front__word .dot{{color:#D8483F;font-weight:600;}}
.front__word .rest{{font-weight:400;}}
.claim{{display:block;margin-top:8px;font-family:'IBM Plex Mono',monospace;
  font-size:11px;letter-spacing:.13em;color:#C8CBCC;}}
</style></head><body><div class="page"><div class="front">
{LOGO.format(s=50, ring="#FBFAF7", red="#D8483F", green="#5E9B77")}
<div>
<span class="front__word"><span class="name">Titze</span><span class="dot">.</span><span class="rest">Consulting</span></span>
<span class="claim">RETHINKING TRENCHLESS REHABILITATION</span>
</div>
</div></div></body></html>"""

# ---------- RUECKSEITE ----------
# Beige-Feld: Original 26mm am rechten Rand des 85mm-Trims -> mit 1.5mm Bleed rechts = 27.5mm.
back = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE}
.page{{background:#FBFAF7;font-family:'Archivo',sans-serif;}}
.back__main{{position:absolute;left:0;top:0;bottom:0;right:29mm;
  display:flex;flex-direction:column;justify-content:space-between;
  padding:12mm 0 12mm 11mm;}}
.back__name{{font-size:18px;font-weight:600;letter-spacing:-0.015em;color:#14181A;}}
.back__role{{display:block;margin-top:5px;font-family:'IBM Plex Mono',monospace;
  font-size:11px;letter-spacing:.1em;color:#A8261F;}}
.back__contact{{display:flex;flex-direction:column;gap:3px;font-family:'IBM Plex Mono',monospace;
  font-size:12.5px;letter-spacing:.02em;color:#4A5055;line-height:1.4;}}
.back__contact .web{{color:#14181A;}}
.back__side{{position:absolute;right:0;top:0;bottom:0;width:29mm;background:#E9E6DF;
  display:flex;flex-direction:column;align-items:center;justify-content:space-between;
  padding:11mm 3mm 11mm 0;}}
.back__side svg.logo{{display:block;}}
.qr{{display:block;}}
</style></head><body><div class="page">
<div class="back__main">
<div>
<span class="back__name">Marco Titze</span>
<span class="back__role">SENIOR CONSULTANT</span>
</div>
<div class="back__contact">
<span>+49 151 11281477</span>
<span>marco@titze.consulting</span>
<span class="web">titze.consulting</span>
</div>
</div>
<div class="back__side">
{LOGO.format(s=30, ring="#14181A", red="#A8261F", green="#2F6B4F").replace('<svg ', '<svg class="logo" ')}
{QR_SVG}
</div>
</div></body></html>"""

OUT.joinpath("print-front.html").write_text(front)
OUT.joinpath("print-back.html").write_text(back)
print("geschrieben:", OUT / "print-front.html")
print("geschrieben:", OUT / "print-back.html")
