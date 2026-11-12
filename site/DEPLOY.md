# Polpo trial-landingspagina v2: deployen

Twee talen, één project:

| URL | Bestand | Taal |
|---|---|---|
| https://polpo.ai/ | `index.html` | Engels |
| https://polpo.ai/nl-be/ | `nl-be/index.html` | Nederlands (België) |

## Bestanden in de repo `sigivts/polpo-policy-brief`

Vervang of voeg toe in de root van de repo:

- `index.html` (vervangt de huidige pagina)
- `nl-be/index.html` (nieuw)
- `assets/` (alle 13 bestanden; de twee screenshots worden niet meer gebruikt en mogen blijven staan of weg)
- `vercel.json` (nieuw: `/nl-be` met slash, redirects `/nl` en `/be-nl`, HSTS-header)
- `og-image.jpg` blijft zoals het is

Afbeeldingen staan met een absoluut pad (`/assets/...`), zodat ze op `/` en `/nl-be/` allebei laden.

## Volgorde

1. Commit op een aparte branch, bv. `trial-v2`. Vercel maakt daar automatisch een preview-URL van.
2. Controleer de preview (beide talen, formulier). Een testinzending komt in de productie-flow van n8n, dus markeer die als test.
3. Merge naar `main`. Dan staat het op polpo.ai.

## DNS

Niets aanpassen. Het A-record (`@` → `216.198.79.1`, of het oude `76.76.21.21`) en de CNAME (`www` → `cname.vercel-dns.com`) bij Spaceship blijven zoals ze zijn. SSL regelt Vercel zelf.

## Formulier

- Post als JSON naar de productie-webhook: `https://n8n.sprintsandsneakers.com/webhook/lead-intake`
- Velden: `dossier`, `context` (nu optioneel), `policy_level` (één van `EU` / `NL` / `BE`), `full_name`, `work_email`, `consent`, `offer`, `lang` (nieuw: `en` of `nl-BE`), `page_url`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `li_fat_id`, `gclid`, `fbclid` (nieuw), `submitted_at`, `ts_loaded`, `hp_company_website` (spamval, moet leeg zijn).
- UTM's en klik-id's komen uit de URL. Komt iemand later terug of wisselt hij van taal zonder UTM's in de URL, dan stuurt de pagina de waarden mee waarmee hij binnenkwam (30 dagen bewaard in de browser).
- `lang` en `fbclid` zijn nieuw: voeg ze toe in n8n / de sheet als je ze wilt zien.
