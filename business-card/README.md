# Visitenkarte — Titze.Consulting

`index.html` ist die **Design-Quelle** (85 × 55 mm, Vorder- und Rückseite, Vektor,
nutzt `../styles/tokens.css`). `qr-vcard.svg` ist der QR mit der vCard direkt
(Quelle = `../marco-titze.vcf`: Name, Firma, Tel, E-Mail, Website).

## Druckreife Dateien → `print/`

Die fertigen Druckdateien liegen in **`print/`** (aus der Design-Quelle erzeugt):

- **`print/rgb/`** — für einen Online-Druckdienst mit RGB-Workflow (der Dienst konvertiert selbst)
- **`print/cmyk/`** — für eine klassische Druckerei (DeviceCMYK)

Alle: 88 × 58 mm inkl. 1,5 mm Beschnitt, Endformat 85 × 55 mm (TrimBox), Schrift in
Pfade gewandelt, QR vektoriell (K-only). Upload-Anleitung & Neu-Erzeugung: `print/README.md`.

> Der Beschnitt beträgt hier **1,5 mm** je Seite (88 × 58 mm). Eine klassische Druckerei
> verlangt oft **3 mm** — dann bei ihr das Template/Maß anfragen und in `print/src/build_cards.py`
> den Beschnitt anpassen (aktuell auf 1,5 mm getrimmt, mit 3 mm Übermalung gerendert).

## Farb-Hinweise für eine klassische Druckerei (CMYK)

Ohne Proof sind die CMYK-Werte in `print/cmyk/` Näherungen. Mit der Druckerei abstimmen:

- **Oxidrot** `#A8261F` → definierter CMYK-Wert (aktuell ~C8 M89 Y89 K20) **oder** Pantone.
- **Anthrazit** `#14181A` → **Rich Black C60 M40 Y40 K100** (bereits so gesetzt), nicht reines K100.
- **Ziel-Farbprofil** der Druckerei erfragen (z. B. ISO Coated v2 / FOGRA39) und ggf. neu konvertieren.
- **Format:** ggf. PDF/X-1a/X-4 verlangt → aus den CMYK-PDFs mit der Druckerei-Vorgabe erzeugen.
- **Material (Empfehlung):** 350 g/m², matt laminiert.
