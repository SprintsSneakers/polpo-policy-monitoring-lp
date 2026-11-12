# Polpo LP v2 (trial account): decisions and open points

Date: 2026-11-11

## Sources
- Copy: Polpo's copy spec (Polpo_AI_Copy_Spec_EN_NL_BE.json + docx, review date 2026-11-03). EN and NL-BE copy used as given.
- Structure: S&S Canva feedback (logos and EU/BE/NL above the fold, How it works right after the hero in a horizontal layout, visual "what is ready", without/with section, product screenshots removed).

## Pages
- EN: https://polpo.ai/ (index.html)
- NL-BE: https://polpo.ai/nl-be/ (nl-be/index.html)
- Repo: sigivts/polpo-policy-brief (Sigi's Vercel Hobby project). DNS at Spaceship unchanged.

## Removed because Polpo's spec says not to claim them without confirmation (G2)
Free, 30 days, no card, IBM 75%, 5-minute lag, ready in two working days, AI Assistant access.

## Form
- Posts JSON to the production n8n webhook (webhook/lead-intake).
- One policy level (EU / NL / BE). Context field is optional.
- New hidden fields: lang (en / nl-BE), fbclid. UTMs, li_fat_id, gclid and fbclid are kept 30 days in the browser, so a language switch or later visit keeps the source.

## Tracking
- UTMs and click ids are measured and sent with every request.
- LinkedIn conversions are not measured yet: that needs the LinkedIn Insight Tag, which is on polpo.nl and not on polpo.ai. Adding Polpo's existing tag to both pages plus a conversion for the form submit fixes it.

## Open
- G2: trial duration, price, included dashboards, AI Assistant access.
- G3: booking route for the training (only then T03-T05 booking copy).
- Leger des Heils logo is not on Polpo's public logo list.
- LinkedIn Insight Tag + conversion event on polpo.ai.
- Add lang and fbclid columns in n8n / sheet.
