# Druckdateien — Visitenkarte

Druckreife Dateien für die Visitenkarte (85 × 55 mm, doppelseitig), erzeugt aus der
Design-Quelle `../index.html`. Zwei Varianten:

| Ordner | Farbraum | Wofür |
|--------|----------|-------|
| **`rgb/`** | RGB | Online-Druckdienst mit RGB-Workflow (konvertiert selbst nach CMYK) |
| **`cmyk/`** | CMYK (DeviceCMYK) | klassische Druckerei mit CMYK-Workflow |

Jeder Ordner enthält:
- `visitenkarte-front.pdf` — Vorderseite (Marke + Claim)
- `visitenkarte-back.pdf` — Rückseite (Kontakt + QR)
- `visitenkarte-vorder-und-rueckseite.pdf` — beide Seiten als 2-Seiten-PDF (Backup)

## Beim RGB-Druckdienst bestellen → `rgb/`

Standard-Visitenkarte, **doppelseitig**, dann im Upload-Dialog **Vorderseite** und
**Rückseite** aus `rgb/` **getrennt** hochladen. Material z. B. 350 g/m², matt laminiert
(wählst du im Bestellprozess, steckt nicht in der Datei).

> Den `cmyk/`-Ordner **nicht** bei einem RGB-Druckdienst hochladen — dessen RGB-Pipeline
> würde ein zweites Mal konvertieren.

## Gemeinsame Spezifikation (beide Varianten)

- **Format inkl. Beschnitt:** exakt 88 × 58 mm (`MediaBox`)
- **Endformat / Schnittkante:** 85 × 55 mm (`TrimBox`) → 1,5 mm Beschnitt je Seite
- **Sicherheitsbereich:** 82 × 52 mm — alle Inhalte liegen deutlich innerhalb
- **Schrift:** vollständig in Pfade gewandelt (keine Fonts eingebettet → keine
  Preflight-Warnung „nicht eingebettete Schriftarten")
- **QR:** vektoriell, reines Schwarz (CMYK: K-only) → sicher scanbar
- **Keine Schnittmarken** (der Beschnitt ist im Format enthalten)

## CMYK-Details (`cmyk/`)

Konvertiert mit dem System-Profil **„Generic CMYK Profile"** (Apple). Zwei Marken­farben
sind auf **definierte Plattenwerte** gesetzt (statt blinder Profil-Konvertierung):

- **Anthrazit** `#14181A` → **Rich Black C60 M40 Y40 K100** (240 % Farbauftrag)
- **QR / reines Schwarz** → **C0 M0 Y0 K100** (K-only)

Übrige Farben (Oxidrot, Moos­grün, Grautöne, Beige, Papier) sind profilkonvertiert:
- Oxidrot `#A8261F` → ca. C8 M89 Y89 K20

> **Wichtig für die Druckerei:** Ohne Proof sind das Näherungen. Vor dem Druck das
> Ziel-Farbprofil der Druckerei abstimmen und Oxidrot ggf. als definierten CMYK-Wert
> oder Pantone festlegen (siehe `../README.md`).

## Neu erzeugen

```sh
cd src
# pikepdf muss verfügbar sein; bei Bedarf venv nutzen:
#   PYTHON=/pfad/zu/venv/bin/python ./build.sh
./build.sh
```

`src/` enthält die Build-Quelle: `build.sh` (Gesamt-Pipeline), `build_cards.py`
(HTML mit Beschnitt), `crop_cards.py` (exakter Zuschnitt + Boxen),
`remap_cmyk.py` (definierte CMYK-Plattenwerte), `make_qr.py` (QR aus der vCard)
und die generierten `print-front.html` / `print-back.html`.

### QR-Code / vCard

Quelle ist `../../marco-titze.vcf`. Der QR enthält Name, ORG (Titze.Consulting),
Telefon, E-Mail und **Website** (`URL:https://titze.consulting`) — bewusst **ohne**
Titel/Funktion. Nach Änderungen an der vCard den QR neu erzeugen und Karten neu bauen:

```sh
cd src && python make_qr.py && ./build.sh
```

> Der QR wird bei jedem Build aus `../qr-vcard.svg` eingebettet; die `viewBox` wird
> automatisch aus der Quellgröße abgeleitet (sonst würde ein größerer QR abgeschnitten).
