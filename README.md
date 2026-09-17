# titze.consulting

Öffentliche Website (Onepager, DE/EN) und Designsystem für **Titze.Consulting** — unabhängige Beratung für die grabenlose Sanierung unterirdischer Infrastruktur.

Statische Seite, **kein Build-Schritt**, gehostet über GitHub Pages. Website und Visitenkarte bauen auf derselben Design-Token-Quelle auf; Präsentationen entstehen separat und referenzieren die hier veröffentlichten Tokens/Assets (siehe „Designsystem nachnutzen").

## Struktur

```
index.html            Redirect → /de/
de/ · en/             Onepager + Impressum/Datenschutz (imprint/privacy)
marco-titze.vcf       vCard unter stabiler URL /marco-titze.vcf
styles/
  tokens.css          ★ Single Source of Truth (Farben, Typo, Abstände)
  fonts.css           @font-face, selbst gehostet
  site.css            Onepager- und Rechtstext-Layout
assets/
  logo/               Bildmarke + Lockup (hell/dunkel)
  fonts/              Archivo + IBM Plex Mono (woff2) + OFL-Lizenzen
  favicon.svg
BRAND.md              Marken-/Designsystem-Dokumentation
business-card/        Karten-Design (85 × 55 mm) + QR + Print-Specs (README)
CNAME                 titze.consulting
```

## Lokal ansehen

Kein Toolchain nötig. Einfachster Weg — statischer Server aus dem Repo-Root:

```bash
python3 -m http.server 8000
# dann http://localhost:8000/  (leitet auf /de/)
```

(Direktes Öffnen der HTML-Dateien per `file://` funktioniert grundsätzlich auch; ein Server bildet aber die absoluten Pfade `/styles/…`, `/assets/…` sauber ab.)

## Deployment (GitHub Pages)

1. **Settings → Pages**: Source = *Deploy from a branch*, Branch = `main`, Folder = `/ (root)`.
2. **Custom domain**: `titze.consulting` (die `CNAME`-Datei ist bereits im Repo). „Enforce HTTPS" aktivieren, sobald das Zertifikat ausgestellt ist.
3. **DNS** beim Domain-Provider setzen:

   | Typ | Name | Wert |
   |---|---|---|
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | AAAA | `@` | `2606:50c0:8000::153` |
   | AAAA | `@` | `2606:50c0:8001::153` |
   | AAAA | `@` | `2606:50c0:8002::153` |
   | AAAA | `@` | `2606:50c0:8003::153` |
   | CNAME | `www` | `alextitze.github.io.` |

## Vor dem Live-Gang offen

- **Impressum/Datenschutz**: Verantwortlichen-Daten eintragen (Name, Anschrift, ggf. USt-IdNr.) und juristisch prüfen lassen — die `TODO`-Kästen markieren die Stellen.
- Optional: Porträtfoto, Referenzen, Analytics (falls cookiefrei).

## Designsystem nachnutzen

Präsentationen und andere Medien liegen **außerhalb** dieses Repos und referenzieren die hier veröffentlichten, stabilen URLs:

- Tokens: `https://titze.consulting/styles/tokens.css`
- Schriften: `https://titze.consulting/styles/fonts.css` (+ `assets/fonts/`)
- Logos: `https://titze.consulting/assets/logo/`
- Regeln: `BRAND.md`

Hinweis: Für Cross-Origin-Einbindung der Schriften kann je nach Zielumgebung ein CORS-Header nötig sein; im Zweifel die woff2 im Präsentations-Setup mitbündeln.

## Lizenz

- **Code** (HTML/CSS): [MIT](LICENSE).
- **Marke, Logos, Texte, Visitenkarte**: © 2026 Marco Titze — keine Nachnutzung.
- **Schriften**: Archivo und IBM Plex Mono unter SIL OFL 1.1 (`assets/fonts/OFL-*.txt`).
