# Polpo landing page: change log

What changed after the first handover build, and why. Newest at the top.

Both pages are rebuilt from `source/` with `python3 gen.py ../site`. Nothing in
this round touched the form endpoint, the hidden fields or the UTM script.

---

## v2.2 — 12 Nov 2026

### Closing section headline

| | Before | After |
| --- | --- | --- |
| Z01 (EN) | Let's set up your first monitor | Let's set up your monitor |
| Z01 (NL) | Laat je eerste monitor voor je instellen | Laat je monitor voor je instellen |

Z01 was still on Polpo's approved wording, so it joins the deviation list.
Still one line at 1100 px in both languages.

### A second line under the form

The privacy note now has a line above it, with a green check:

- EN: Free 1:1 onboarding included
- NL: Gratis 1-op-1 onboarding inbegrepen

It is the first thing under the Continue button, in navy at 0.92rem and semibold.
The privacy note drops to 0.82rem in grey and sits below it, so the two read as
a claim and a footnote rather than two equal lines.

Both sit outside the `<form>` element, so they stay visible on all four steps.

The divider that used to sit on `.reassure` moved up to `.perk`, which keeps the
line in the same place under the button.

The Flemish line is longer and missed a single 375 px line by about 0.2 px, so
it wrapped. It drops to 0.85rem under 420 px. Both languages hold one line now.

### Monitor handover card

| | Before | After |
| --- | --- | --- |
| P05 (EN) | Review your setup together and take control of your account. | We'll walk you through your tailored monitor together, so you're ready to start tracking. |
| P05 (NL) | We nemen je inrichting samen door en jij neemt de controle over je account. | We lopen je monitor op maat samen door, zodat je meteen kunt beginnen met volgen. |

Card two now runs three lines against card one's two. The cards are grid
children so they still match in height.

One thing to look at: benefit card B03 already says "We'll walk you through your
setup so you can start monitoring with confidence." Two blocks on the same page
now open the same way. B03 is further down and the wording was approved in the
v2.0 round, so I left it. Worth a look on the next copy pass.

### The hero button is gone

The hero had a "Get started" button pointing at `#request`. The form now sits in
the next column, and on mobile directly below the copy, so the button scrolled
the visitor to something already in front of them.

What is left in the hero is the "How it works" text link. The form's own
Continue button is the primary action.

The four other "Get started" buttons on the page are untouched. They sit far
enough down that the jump back up to the form still does something.

One side effect worth watching: on a 375x812 screen the form card starts at
656 px, and that button was the only thing above the fold pointing at it.

### Shorter form intro and consent line

| | Before | After |
| --- | --- | --- |
| F02 (EN) | One topic is enough to get started. We'll use your answer to build your monitor, then arrange your 30-minute onboarding session. | We'll use your answer to build a monitor tailored to your needs and schedule your free onboarding session. |
| F02 (NL) | Eén onderwerp is genoeg om te starten. Met je antwoord bouwen we je monitor en plannen we je onboardingsessie van 30 minuten in. | Met je antwoord bouwen we een monitor op jouw maat en plannen we je gratis onboardingsessie in. |

The consent checkbox on step 4 ran to six lines. It now reads:

- EN: I consent to Polpo using my answers to create my trial account and contact
  me, in line with the Privacy Policy.
- NL: Ik geef Polpo toestemming om mijn antwoorden te gebruiken om mijn
  proefaccount aan te maken en mij te contacteren, volgens het privacybeleid.

Three lines instead of six. The link to the privacy policy is still in there,
same URL, same place in the sentence.

### Mobile hero order, decided

Earlier in the day I moved the form above the headline on phones. Miguel asked
for it back the other way round: a visitor needs to know what the page is before
they meet a form. So the headline leads again on mobile, same as desktop.

The `order:-1` rule is gone. The only thing left from that attempt is a tighter
gap between the two hero blocks, `1.75rem` instead of `2rem`, which pulls the
form up a little without reordering anything.

| On a 375x812 screen | Now |
| --- | --- |
| Headline block starts at | 100 px |
| Form card starts at | 656 px |

### New headline and eyebrow

| | Before | After |
| --- | --- | --- |
| H1 (EN) | Your policy monitor. / Built for you. | Policy monitoring. / Built for you. |
| H1 (NL) | Jouw beleidsmonitor. / Wij bouwen hem. | Beleidsmonitoring. / Voor jou gebouwd. |
| Eyebrow (EN) | Political monitoring trial | Made for Public Affairs teams. |
| Eyebrow (NL) | Proefaccount politieke monitoring | Gemaakt voor Public Affairs-teams. |

The eyebrow first read "Built for Public Affairs teams." Stacked above a
headline ending in "Built for you." it repeated itself, so it is "Made for" now.

"Policy monitoring." is wider than "Your policy monitor.", so the old type scale
broke it onto two lines in the narrow hero column. The clamp is now
`clamp(2.15rem, 3.9vw, 2.95rem)`, with a separate rule under 480 px that lets it
shrink with the viewport instead of sitting on a floor it cannot fit under. Each
line holds on one row at 375, 960, 1100 and 1381 px, in both languages.

I shortened the Flemish second line to "Voor jou gebouwd." "Op jouw maat
gebouwd." was my first attempt and it wrapped at every desktop width.

### One privacy line instead of four ticks

The four orange checkmarks under the form are gone. In their place sits a single
centred line with a lock icon:

- EN: Your details stay private.
- NL: Je gegevens blijven privé.

The lines that went away were "One topic is enough to start", "Searches and
alerts prepared before your onboarding session", "Your answers are never sold or
shared" and "Unsubscribe in one click", plus their Flemish equivalents.

I also removed the lock line that used to sit under the submit button on step 4,
because it said the same thing as the new one and the two would have appeared
within a few pixels of each other. The copy keys `safe_note` and the old list
form of `reassure` are deleted from `lpcopy.py`.

### Every CTA now says the same thing

| | Before | After |
| --- | --- | --- |
| Page CTAs, C01 (EN) | Request my trial | Get started |
| Page CTAs, C01 (NL) | Vraag mijn proefaccount aan | Aan de slag |
| Form submit, F15 (EN) | Get Started | Get started |

C01 feeds every CTA button on the page, so one copy key covered the lot. The
submit button already said "Get Started" with a capital S from v2.1, which no
longer matched once the page CTAs changed, so it is lower case now. Flemish was
already "Aan de slag" on the submit button and now matches everywhere.

C01 fed five buttons when I made this change. The hero one came out afterwards,
so it is four now.

### Full-width buttons in the form

Continue, Back and the submit button run the full width of the form card and
line up with the input above them. `.stepnav` was a wrapping flex row, so on the
steps that have both buttons they sat side by side at their natural widths.
It is a column now and the buttons stack, Continue on top.

Measured at 1381 px and at 375 px: the button's left and right edges land on the
same pixels as the input field above it. Text stays centred and nothing about
the button's colour, radius or shadow changed.

### Rounded corners on the example card

The "Your trial account" card has a 26 px radius, but `.brief-body` painted an
opaque white rectangle over the bottom two corners, so the card read as cut off.
The body now carries the matching bottom radius.

I did not use `overflow:hidden` on the card. The orange EXAMPLE badge is
positioned above the card's top edge and clipping would have eaten it.

### Checked after the changes, both languages

| Check | Result |
| --- | --- |
| Forms on the page | 1 |
| Hidden tracking fields | 14 |
| Webhook in the HTML | present, unchanged |
| UTM and click ID capture | utm_source, utm_medium, utm_campaign, gclid, page_url all populated |
| Step navigation | step 1 to step 2, topic value kept |
| Headline wrapping | one line per row at 375, 960, 1100, 1381 px |
| Card corners | bottom radius 25 px, badge not clipped |
| CTA copy | all four page buttons plus submit read the same |
| Button alignment | edges match the input field at 375 px and 1381 px |
| Hero buttons | 0, text link only |
| Consent link | privacy policy URL unchanged, still inside the sentence |
| Perk line | one line at 375 px in both languages, visible on all four steps |

No test request was sent to n8n.

### If you preview this in a headless browser

The reveal-on-scroll animation does not run, because IntersectionObserver never
fires there. Every `.rise` element stays at `opacity:0`, so the page below the
hero looks blank and the reassurance ticks look like empty circles. Neither is a
page bug and neither happens in a real browser. To check below-the-fold layout
in a headless preview, add the classes by hand first:

    document.querySelectorAll('.rise').forEach(n => n.classList.add('in'));
    document.querySelectorAll('.draw').forEach(n => n.classList.add('drawn'));

---

## v2.1 — 11 Nov 2026

### The form moved into the hero

The hero photo and the monitoring diagram are gone. The request form sits in
their place, next to the headline.

The form was **moved, not copied**. It is the same single `<form id="brief-form">`
element, with the same `action`, the same 14 hidden fields and the same script.
A copy would have created duplicate element IDs and silently broken validation
and tracking.

`id="request"` moved onto the new hero wrapper, so all six `href="#request"`
buttons still work without any link changes.

The old `<section id="request">` below the FAQ was deleted.

Checked after the move, on both languages:

| Check | Result |
| --- | --- |
| Forms on the page | 1 |
| Hidden tracking fields | 14 |
| Webhook in the HTML | present, unchanged |
| UTM + click ID capture | all 8 keys populated on load |
| 30-day persistence | values survive a visit without UTMs |
| Full submit (fetch stubbed) | 21 fields, correct webhook, EN and NL |

No test request was sent to n8n.

### Form split from three steps to four

"What matters to your organisation?" moved onto its own step. It stays optional.
Step one is now a single easy question, which is the first thing someone sees.

Progress label and bar run 1 to 4.

### Copy changes

| Where | Before | After |
| --- | --- | --- |
| Form intro (F02) | "We'll use your answers to prepare your trial, then arrange your 30-minute training and account handover." | "We'll use your answer to build your monitor, then arrange your 30-minute onboarding session." |
| Form button (F15) | "Request my trial" / "Vraag mijn proefaccount aan" | "Get Started" / "Aan de slag" |
| Under the button | "We prepare the setup. You receive access during the 30-minute training." | removed |
| Under the button | — | lock icon + "Your data is safe with us." / "Je gegevens zijn bij ons veilig." |
| Whole page | "training" / "training" | "onboarding session" / "onboardingsessie" |

The word swap hit 13 places per language: meta description, hero bullet, form
intro, last-step line, confirmation message, four reassurance and FAQ answers,
and the closing section.

Removed outright:

- "Here's an example of what we'll prepare for you." (EN and NL)
- "Example. Your account is prepared around the topic you give us." (the caption
  under the mock card)

### Layout and typography

- "Your monitor, ready in two steps" now fits on one line. Verified at 1305,
  960, 768 and 640 px. It wraps to two lines at 375 px, which is expected.
- "Transform how you monitor policy." same fix, same result.
- "All the answers you need. / In one place." split across two lines and
  centred, description centred with it.
- "See what changes once your topic is being monitored for you." centred.

The headline fix is a `head-wide` modifier that releases the heading from the
62-character measure while body text keeps it.

### Two bugs found and fixed

1. **Form labels rendered white on white.** `header.hero` sets `color:#fff` for
   the navy background, and the white form card inherited it. Fixed with
   `color:var(--ink)` on `.hero-media .form-card`.
2. **Reassurance checkmarks rendered as empty circles.** The scroll animation
   only watched `.rise` elements, and that block uses `.draw`, so it never got
   the class that reveals the tick. This was already broken before the form
   moved, just invisible below the fold. The observer now watches both.

### Dead code removed

The hero parallax script, the image load and error handlers, and the `img_alt`
and `diagram_alt` copy keys. All of them referenced the image that is gone.

Still orphaned in `style.css`, harmless, left for a later cleanup: `.shot`,
`.shot-fb`, `.shot-veil`, `.shot-diagram`, `#shot-img`, `.brief-foot`.
Also unused in `site/assets/`: `hero-european-parliament.webp`,
`diagram-monitoring.png`, and four logo files.

---

## v2.0 — baseline

The first build, from Polpo's copy spec (review date 3 Nov 2026) and the S&S
Canva feedback. See `HANDOVER.md` and `decisions.md`.

Copy lines that already deviated from Polpo's approved spec in this round carry
a `(changed by S&S)` comment in `source/lpcopy.py`. The full list as it stands
now, per language:

H01, H02, H03, M02, P03, P04, P05, V01, V02, B01-B04, C01, F02, F14, F15, T02,
Z01, Z02.

F16 was deleted.

---

## Open, needs a decision

- **Mobile hero order.** Settled in v2.2: headline first, form below it. The
  form starts at 656 px on a 375x812 screen, so paid traffic still has to
  scroll to reach it, and the hero button that used to point at it is gone.
  Worth watching once there is live data. If mobile conversion looks weak, the
  cheapest fix is a sticky bar rather than putting the button back.
- **Copy sign-off.** Everything in the deviation list above differs from what
  Polpo approved. It needs a pass from Desmin before going live.
- **Consent wording.** The shortened consent line is a marketing edit, not a
  legal one. Someone at Polpo who owns the privacy policy should read it.
- **Flemish sign-off.** The NL H1, the new eyebrow, the new privacy line, the
  shortened consent and form intro, the new perk line, the rewritten handover
  card and the "onboardingsessie" wording all need
  a native Flemish reader. "Voor jou
  gebouwd." and "Gemaakt voor Public Affairs-teams." are my translations, not a
  Flemish writer's.
- **Luxembourg.** It sits in the hero country chips but is not a confirmed
  coverage claim, and it is missing from the form's level options. Adding it
  there needs a matching change in n8n.
- **Flag emoji.** The country flags fall back to plain letter pairs on Windows.
  Flag images would fix it.
- **Deploy route.** The live code is in Sigi's private repo
  `sigivts/polpo-policy-brief`, on his personal Vercel account. Nothing has been
  committed or pushed from here.
