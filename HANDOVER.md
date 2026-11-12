# Polpo landing page v2: handover

Status (11 Nov 2026, v2.1): built and checked, not live yet. The page is in English (`/`) and Flemish (`/nl-be/`) and is meant to replace the current page on https://polpo.ai.

Changed since the first build? See `CHANGELOG.md`. The biggest one: the request form now sits in the hero, where the photo used to be.

## What is in this zip

- `site/`: the deploy-ready website. Copy this folder's contents into the repo root as-is.
  - `index.html`: English page (https://polpo.ai/)
  - `nl-be/index.html`: Flemish page (https://polpo.ai/nl-be/)
  - `assets/`: customer logos and Polpo logo parts. The hero photo and the monitoring diagram are still in here but no longer used, see `CHANGELOG.md`.
  - `og-image.jpg`: image shown when the link is shared
  - `vercel.json`: makes `/nl-be` resolve to `/nl-be/`, redirects `/nl` and `/be-nl` there, and adds the HSTS security header
  - `DEPLOY.md`: the same deploy steps, in Dutch, for Sigi
- `source/`: the generator, so copy changes are made in one place.
  - `lpcopy.py`: all page text, English and Flemish. Each client line carries the ID from Polpo's spec (H01, C01, F12…).
  - `gen.py`: builds both pages. Run `python3 gen.py ../site` from `source/` after editing `lpcopy.py`.
  - `style.css`, `sprite.svg`, `stars.svg`: design inputs used by `gen.py`.
- `client-brief/`: Polpo's copy spec (docx + json) and the S&S Canva feedback screenshot the layout is based on.
- `decisions.md`: what was decided and why (also in the Claude Project "Polpo landingpage Policy Brief").
- `CHANGELOG.md`: what changed after the first build, and what still needs a decision.

## To go live: GitHub, then Vercel, then polpo.ai

1. **Get access to the repo.** The code is in Sigi's private repo `sigivts/polpo-policy-brief`. It's connected to Sigi's own Vercel Hobby project, not the S&S Tools account, and polpo.ai is attached to that project. Ask Sigi to add you to the repo, or send Sigi the `site/` folder to push himself.
2. **Push to a branch first.** Copy the contents of `site/` into the repo root on a new branch, for example `trial-v2`, and push. Vercel builds a preview URL for that branch automatically.
3. **Test the preview:**
   - Open both languages and use the EN/NL switch.
   - Submit one test request per language. It lands in the production n8n flow, so mark it as a test.
   - Open the preview with `?utm_source=test&utm_campaign=test` and check that the UTMs arrive in n8n.
4. **Merge to `main`.** Vercel deploys it to polpo.ai.
5. **DNS: change nothing.** The records at Spaceship are already correct: A record `@` → `216.198.79.1` (the older `76.76.21.21` also still works) and CNAME `www` → `cname.vercel-dns.com`. SSL is issued by Vercel automatically.

## What still needs to be added

- **n8n / sheet:** two new fields come in with every request. `lang` is `en` or `nl-BE`, so you can route Flemish leads. `fbclid` is Facebook's click ID. Add them as columns if you want to see them. All other field names are the same as the current page.
- **LinkedIn tracking:** not possible yet (see below).
- **From Polpo (Desmin):**
  - Trial length, price, included dashboards and whether the AI Assistant is part of the trial. These are deliberately not on the page until Polpo confirms them (their spec, decision G2).
  - Whether there will be a booking link for the 30-minute training. Their spec has extra confirmation copy for that, IDs T03 to T05 (decision G3).
  - Whether the Leger des Heils logo may be used. It's not on Polpo's public logo list.
  - Whether the topic suggestions in the form are right. EN: AI Act, CBAM, Packaging rules, Energy policy, ETS reform. NL: Energiebeleid, Stikstof, Mobiliteit, AI Act, CBAM.
- **Optional:** a Flemish share image (`og-image.jpg` is shared by both pages).

## Tracking: what is measured

- **UTMs are measured and sent to the webhook with every request:** `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, plus the click IDs `li_fat_id`, `gclid` and `fbclid`, the page URL, the referrer and the language.
  - The browser keeps them for 30 days. A visitor who switches language or comes back later without UTMs in the link is still attributed to the original source.
- **LinkedIn conversion tracking is not possible yet.** It needs the LinkedIn Insight Tag on the page. Polpo's Insight Tag is on polpo.nl, not on polpo.ai. To measure LinkedIn conversions, someone with access to Polpo's LinkedIn Campaign Manager needs to:
  1. Add the same Insight Tag (same partner ID) to both pages, in the `<head>` of `site/index.html` and `site/nl-be/index.html`, or in `gen.py` so it survives a rebuild.
  2. Create a conversion for the form submit.
- **Form endpoint:** the form posts JSON to the production webhook `https://n8n.sprintsandsneakers.com/webhook/lead-intake`. The test webhook is `/webhook-test/lead-intake`.

## Review links (LP agent, optional)

Both pages passed the LP agent's checks. These review links lead to a shareable preview once approved:

- EN: https://lp-agent.sprintsandsneakers.com/review/980708ef-27cd-41ed-889a-3c889dd19df8
- NL: https://lp-agent.sprintsandsneakers.com/review/ab494cb3-c870-40ba-bbd4-98218884334e
