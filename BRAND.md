# Titze.Consulting — Marken- & Designsystem

Verbindliche Quelle der Werte: [`styles/tokens.css`](styles/tokens.css).
Dieses Dokument erklärt die Anwendung. Farben, Typografie und Visitenkarte sind **abgenommen** — nicht neu interpretieren.

## Grundregeln

- Firmenname immer **`Titze.Consulting`** — mit Punkt, ohne Leerzeichen, nie mit Bindestrich. Der Punkt ist Markenbestandteil (Leitfarbe Oxidrot).
- **Maximal zwei Flächenfarben pro Ansicht.** Grün nie als Fläche — nur als Linie oder Label.
- **Keine** Radien, **keine** Schatten in der Web-UI. Trennung über 1-px-Linien und Flächenwechsel.
- Sachlich-technische Haltung: keine Scroll-Animationen, kein Parallax. Hover nur Farbwechsel (120 ms).
- Rufnummer: Anzeige `+49 151 11281477` (E.123/DIN 5008), in `href`/vCard `+4915111281477` (E.164).

## Farben

| Token (CSS-Variable) | Hex | Verwendung |
|---|---|---|
| `--color-anthracite` | `#14181A` | Text auf hell, Vollflächen (Hero, Footer) |
| `--color-oxide-red` | `#A8261F` | Leitfarbe: Punkt, Primärbutton, Labels, Links |
| `--color-oxide-red-light` | `#D8483F` | Rot auf dunklem Grund |
| `--color-moss` | `#2F6B4F` | Akzent, sparsam — Linie/Nachhaltigkeit |
| `--color-moss-light` | `#5E9B77` | Grün auf dunklem Grund |
| `--color-steel` | `#6E7378` | Sekundärtext, inaktive Zustände |
| `--color-slate` | `#4A5055` | Fließtext |
| `--color-fog` | `#C8CBCC` | Fließtext auf dunklem Grund |
| `--color-paper` | `#FBFAF7` | Grundfläche, Text auf dunkel |
| `--color-limebeige` | `#E9E6DF` | Sekundärfläche (Person/Kontakt) |
| `--color-edge` | `#EAE5DB` | Innenlinien auf Papier |
| `--color-edge-strong` | `#D8D3C8` | Außenrahmen, Trenner |

## Typografie

- **Archivo** (`--font-sans`, Variable Font 100–900) — Überschriften und Fließtext.
- **IBM Plex Mono** (`--font-mono`, 400/500) — Labels, Rubriken, Kontaktdaten, Maße. Immer Versalien, immer gesperrt (`.12em`–`.16em`), immer kurz.
- Skala (Archivo): 52 / 28 / 20 / 19 / 17 / 16 / 14 px. Mono: 12 / 11 / 10.5 px.
- `letter-spacing` eng bei großen Graden (−0.035em @52px, −0.02em @28px, −0.015em ab 20px), normal ab 16px.
- `text-wrap: pretty` auf allen Fließtextabsätzen.
- Fonts sind **selbst gehostet** (`assets/fonts/`, SIL OFL 1.1) — kein Google-CDN, damit die Seite cookie-/bannerfrei bleibt.

## Abstände

Skala (`--space-*`): 5 · 7 · 10 · 12 · 14 · 18 · 20 · 22 · 24 · 26 · 28 · 32 · 36 · 44 · 48 · 72 px.
Bandpadding horizontal 36 px (mobil 24 px), vertikal 20 px (Header/Footer), 44 px (Person), 72 px (Hero).
Inhaltsbreite: max. 1000 px (Onepager), 640 px (Rechtstexte).

## Logo

- **Bildmarke** (`assets/logo/logo-mark-*.svg`): Rohr im Rohr — Altrohr außen (Anthrazit), Liner innen (Oxidrot), Bogen = sanierter Abschnitt (Moosgrün). Quadratisch; Favicon/Avatar/App-Icon.
- **Lockup** (`assets/logo/logo-lockup-*.svg`): Marke + Wortbild + Claim „RETHINKING TRENCHLESS REHABILITATION". Achtung: Text als `<text>` mit Fontverweis — für Druck/fremde Systeme vorher Schrift in Pfade wandeln.
- `-light-bg` auf hellem, `-dark-bg` auf dunklem Grund.

## Visitenkarte

`business-card/index.html` — 85 × 55 mm, Vorderseite Anthrazit (Lockup + Claim), Rückseite Papier (Name, `SENIOR CONSULTANT`, Kontakt, QR ≥ 22 mm). QR enthält die vCard direkt (Quelle: `/marco-titze.vcf` im Repo-Root). Kontakt-E-Mail durchgängig `marco@titze.consulting` (Website, Karte, vCard). Bewusst **keine** Anschrift auf der Karte. Für den Druck 3 mm Beschnitt ergänzen, 350 g/m² matt laminiert.
