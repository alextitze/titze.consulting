# Visitenkarte — Titze.Consulting

`index.html` ist die **Design-Quelle** (85 × 55 mm, Vorder- und Rückseite, Vektor, nutzt `../styles/tokens.css`). `qr-vcard.svg` ist der QR mit der vCard direkt (Inhalt = `/marco-titze.vcf`).

Die Druckdatei wird aus dieser Quelle erzeugt — die HTML-Datei selbst geht **nicht** an die Druckerei.

## Was die Druckerei braucht

- **Format:** PDF/X-1a (klassisch) oder PDF/X-4 (mit Transparenz/ICC).
- **Farbe:** CMYK, nicht RGB. Markenfarben definiert festlegen, damit sie nicht kippen:
  - Oxidrot `#A8261F` → als definierter CMYK-Wert **oder** Pantone (mit der Druckerei abstimmen).
  - Anthrazit `#14181A` → „Rich Black" (z. B. C60 M40 Y40 K100), nicht reines K100.
- **Beschnitt:** 3 mm rundum (85 × 55 mm → 91 × 61 mm) + Schnittmarken. Inhalt ≥ 3–5 mm von der Kante.
- **Schrift:** in Pfade wandeln oder einbetten (Archivo/IBM Plex Mono).
- **QR:** rein schwarz, vektoriell (ist er) → sicher scanbar.
- **Seiten:** Vorderseite + Rückseite als zwei Seiten.
- **Material (Empfehlung Handover):** 350 g/m², matt laminiert.

## Weg zur Druckdatei

1. **Empfohlen:** Template der konkreten Druckerei anfordern (Maße/Bleed/Farbprofil/Format) und die Karte in Scribus (kostenlos) / Affinity Publisher / InDesign anhand der Tokens nachbauen, als PDF/X-1a mit Bleed exportieren.
2. **Automatisiert (mit Farb-Vorbehalt):** HTML → PDF (Chromium/WeasyPrint) → Ghostscript + ICC → PDF/X-1a/CMYK. Das Rot vor dem Druck per Proof prüfen.

Browser „Drucken → Als PDF" liefert nur einen **RGB-Proof ohne Bleed** — für die digitale Weitergabe okay, nicht druckreif.
