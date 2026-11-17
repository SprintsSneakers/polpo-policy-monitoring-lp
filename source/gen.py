"""Build the Polpo trial landing page (EN + NL-BE) from copy.py.

usage: python3 gen.py OUTDIR [ASSET_BASE]
ASSET_BASE defaults to "/assets/" (root-absolute, works on / and /nl-be/).
"""
import json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lpcopy import EN, NL

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
ASSET = sys.argv[2] if len(sys.argv) > 2 else "/assets/"
SITE = "https://polpo.ai"
WEBHOOK = "https://n8n.sprintsandsneakers.com/webhook/lead-intake"

# LinkedIn Insight Tag. Partner ID is Polpo's (ad account 503387535).
# The tag loads only after the visitor clicks Accept on the cookie banner.
# Conversion ID is the form-submit "Lead" conversion in Campaign Manager.
LINKEDIN_PARTNER_ID = "894450"

BASE_CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
SPRITE = open(os.path.join(HERE, "sprite.svg"), encoding="utf-8").read().replace('"assets/', '"' + ASSET)
STARS = open(os.path.join(HERE, "stars.svg"), encoding="utf-8").read()

e = html.escape
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'
CROSS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>'
SPARK = '<i class="spark"></i><i class="spark"></i><i class="spark"></i>'
ICON = {
    "eu": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 2.6 15 0 18M12 3c-2.6 2.6-2.6 15 0 18"/></svg>',
    "nl": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 21h16M6 21V9l6-4 6 4v12"/><path d="M10 21v-5h4v5"/></svg>',
    "be": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 21V4h9l-1.5 3.5L14 11H5"/><path d="M5 21h14"/></svg>',
}
BICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v14H4z"/><path d="M4 8l8 5 8-5"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 11h18"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h10M4 12h16M4 18h7"/><circle cx="17" cy="6" r="2"/><circle cx="14" cy="18" r="2"/></svg>',
]
STEPICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
]
# file, alt, intrinsic width at 140px tall, optical scale.
# Square-ish marks get a scale above 1 so they do not read as half-size next to
# the wide wordmarks. Roughly 1 / sqrt(aspect ratio), clamped for sanity.
LOGOS = [("logo-asml.png", "ASML", 498, 1), ("logo-siemens-energy.png", "Siemens Energy", 408, 1),
         ("logo-uber.png", "Uber", 403, 1), ("logo-ikea.png", "IKEA", 375, 1),
         ("logo-eli-lilly.png", "Eli Lilly", 257, 1.15),
         ("logo-kwf.webp", "KWF", 519, 1), ("logo-cz.webp", "CZ", 155, 1.5),
         ("logo-leger-des-heils.webp", "Leger des Heils", 151, 1.5)]

EXTRA_CSS = r"""
/* ===================== v2 additions ===================== */
.navright{display:flex;align-items:center;gap:1.6rem}
.langsw{display:inline-flex;align-items:center;gap:.15rem;padding:.2rem;border:1px solid rgba(255,255,255,.22);border-radius:100px}
.langsw a,.langsw span{display:inline-flex;align-items:center;justify-content:center;min-width:44px;min-height:44px;padding:0 .7rem;border-radius:100px;font-size:.82rem;font-weight:600;letter-spacing:.02em;text-decoration:none}
.langsw span{background:#fff;color:var(--navy)}
.langsw a{color:rgba(255,255,255,.78)}
.langsw a:hover{color:#fff;background:rgba(255,255,255,.1)}
.hero .chip{white-space:nowrap}
.hero h1 span.l{display:block}
.hero-cta{display:flex;flex-wrap:wrap;gap:.8rem;align-items:center}
.textlink{display:inline-flex;align-items:center;gap:.4rem;min-height:44px;padding:0 .4rem;color:#fff;font-weight:600;text-decoration:none;border-bottom:1px solid transparent}
.textlink:hover{border-bottom-color:rgba(255,255,255,.6)}
.textlink svg{width:18px;height:18px;fill:none;stroke:#FF8A4D;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.hero-grid{margin-top:clamp(1.5rem,3vw,2rem)}
.glass{padding-top:clamp(1.75rem,3.5vw,2.4rem);padding-bottom:clamp(1.75rem,3.5vw,2.4rem)}
/* sized so each headline line stays unbroken from the two-column breakpoint up */
.hero h1{font-size:clamp(2.15rem,3.9vw,2.95rem);margin-top:1rem}
/* on a phone the 2.15rem floor pushes "Policy monitoring." about 4px past the
   column, so it wrapped. Let it scale with the viewport under 480px instead. */
@media(max-width:480px){.hero h1{font-size:clamp(1.8rem,8.1vw,2.15rem)}}
/* the form sits in the right-hand hero column now, so it needs real width */
@media(min-width:960px){.hero-grid{grid-template-columns:1fr 1fr}.glass{padding-left:2.6rem;padding-right:2.6rem}}
/* Mobile: headline first, then the form. A visitor needs to know what the page
   is before they meet a form. The hero block is kept tight so the form follows
   as closely as possible. */
@media(max-width:959px){.hero-grid{gap:1.75rem}}
.wins.inline{margin-top:1.5rem}
.verts{margin-top:1.75rem}
.vrow{margin-top:.6rem;display:flex;flex-wrap:wrap;gap:.5rem}
.vchip{white-space:nowrap}
.verts-l{display:block;font-size:.76rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.6)}
@media(max-width:959px){.vrow{justify-content:flex-start}}
.vchip{display:inline-flex;align-items:center;gap:.4rem;padding:.4rem .72rem;border:1px solid rgba(255,255,255,.24);border-radius:100px;font-size:.82rem;font-weight:500;color:#fff;background:rgba(255,255,255,.06)}
.vchip .flag{font-size:1.05em;line-height:1;font-family:"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif}
.hero-logos{margin-top:clamp(2rem,4vw,2.4rem);padding-top:1.25rem}
.hero-logos p{font-size:.84rem;font-weight:500;color:rgba(255,255,255,.62)}
.hero-logos .logos-row{margin-top:1.15rem}
.hero-logos .logos-row img{filter:brightness(0) invert(1);opacity:.66}
.hero-logos .logos-row img:hover{opacity:.95}
/* request form, now in the hero. The card keeps its own white surface so every
   form style below the fold still applies unchanged. */
.hero-media{justify-content:flex-start}
/* .hero sets color:#fff for the navy background. The card is white, so reset the
   inherited colour or every label and reassurance line disappears. */
.hero-media .form-card{margin-top:0;padding:clamp(1.4rem,3vw,1.9rem);color:var(--ink);
  box-shadow:0 40px 80px -40px rgba(0,0,0,.55);border-color:rgba(255,255,255,.14)}
.form-card-head{margin-bottom:1.4rem}
.form-card-head h2{font-size:clamp(1.25rem,2.4vw,1.5rem);line-height:1.25;letter-spacing:-.02em;color:var(--navy)}
.form-card-head p{margin-top:.5rem;font-size:.9rem;line-height:1.5;color:var(--ink-soft)}
.hero-media .progress{margin-bottom:1.4rem}
.hero-media legend{font-size:1.08rem}
.hero-media .stepset + .stepset{margin-top:0}
@media(min-width:960px){.hero-media{height:auto;align-self:start}}
/* how it works: horizontal, two steps */
.steps2{margin-top:2.5rem;display:grid;gap:1.1rem;position:relative}
@media(min-width:760px){.steps2{grid-template-columns:1fr 1fr;gap:1.5rem}}
.scard{background:var(--paper);border:1px solid var(--line);border-radius:var(--r-lg);padding:clamp(1.4rem,3vw,2rem);box-shadow:0 22px 48px -36px rgba(13,20,61,.35);
  display:flex;flex-direction:column;min-height:290px;transition:transform .2s ease,box-shadow .2s ease}
.scard:hover{transform:translateY(-3px);box-shadow:0 18px 38px -28px rgba(13,20,61,.45)}
.scard-top{display:flex;align-items:center;justify-content:space-between;gap:.9rem;margin-bottom:1.5rem}
.scard .step-n{width:48px;height:48px;background:var(--orange-soft);border-color:transparent;color:var(--orange-deep);font-size:1.05rem;font-weight:700}
.scard .step-ico{width:28px;height:28px;color:var(--orange-deep)}
.scard h3{font-size:1.18rem;font-weight:600}
.scard p{margin-top:.6rem;margin-bottom:1.6rem;color:var(--ink-soft);font-size:.985rem}
/* small preview strip pinned to the bottom of each step card */
.step-prev{margin-top:auto;padding:1.05rem 1.1rem;background:var(--mist);border-radius:12px}
.step-prev-lab{display:block;font-size:.69rem;letter-spacing:.07em;text-transform:uppercase;font-weight:600;color:var(--ink-soft);margin-bottom:.55rem}
.step-prev-row{display:flex;align-items:center;gap:.6rem;font-size:.875rem;font-weight:600;color:var(--navy)}
.step-prev-row span:first-child{flex:0 0 auto;display:block;width:18px;height:18px}
.step-prev-row svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.step-prev-row .pv-search{color:var(--orange-deep)}
.step-prev-row .pv-ok{color:#198568}
.outcome{margin-top:1.8rem;display:flex;flex-wrap:wrap;align-items:center;gap:1rem 1.5rem;justify-content:center}
.outcome-pill{display:inline-flex;align-items:center;gap:.55rem;padding:.6rem 1rem;border-radius:100px;background:var(--orange-soft);color:var(--orange-deep);font-weight:600;font-size:.92rem}
.outcome-pill svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
/* what is ready */
.ready-grid{margin-top:2.75rem;display:grid;gap:2rem}
@media(min-width:980px){.ready-grid{grid-template-columns:.92fr 1.08fr;align-items:start;gap:2.5rem}}
.ready-grid .brief{margin-top:1rem}
.ready-grid .bsnap{margin-top:1.3rem}
.bcards{display:grid;gap:1rem}
@media(min-width:620px){.bcards{grid-template-columns:1fr 1fr}}
.bcard{background:var(--paper);border:1px solid var(--line);border-radius:var(--r-md);padding:1.4rem 1.35rem}
.bcard .bsec-ico{margin-bottom:.9rem}
.bcard h3{font-size:1.02rem;font-weight:600;letter-spacing:-.01em;line-height:1.3}
.bcard p{margin-top:.5rem;font-size:.93rem;color:var(--ink-soft)}
.b-head{font-size:clamp(1.3rem,2.6vw,1.6rem);font-weight:600;letter-spacing:-.02em}
.next-pill{display:inline-block;padding:.15rem .55rem;border-radius:7px;background:var(--orange-soft);color:var(--orange-deep);font-size:.82rem;font-weight:600}
/* without / with */
/* section intros: the headline gets the full column so it does not drop a
   single word onto its own line, body text stays at a readable 62ch measure */
.narrow.head-wide{max-width:none}
.narrow.head-wide .lede{max-width:62ch}
.head-center{text-align:center}
.head-center .lede{margin-inline:auto}
h2.stack span{display:block}
.diff-head{margin-inline:auto;text-align:center}
.diff-head .eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange-deep)}
.diff-head h2{margin-top:.6rem}
.diff-head .lede{margin-top:.75rem}
.diff-close{margin:2.25rem auto 0;max-width:46ch;text-align:center;font-size:clamp(1.02rem,1.9vw,1.18rem);font-weight:600;color:var(--ink)}
.diff{margin-top:2.5rem;display:grid;gap:1.1rem}
@media(min-width:760px){.diff{grid-template-columns:1fr 1fr;gap:1.5rem}}
.dcol{border-radius:var(--r-lg);padding:clamp(1.4rem,3vw,2rem)}
/* tinted to match the monitoring diagram: warm red for the old way, blue for Polpo */
.dcol.without{border:1px solid #F3CFC6;background:#FEF5F2}
.dcol.with{border:1px solid #C6D8F2;background:#F1F6FD;box-shadow:0 26px 54px -40px rgba(30,58,138,.45)}
.dcol h3{font-size:1.08rem;font-weight:600}
.dcol.without h3{color:#A3341A}
.dcol.with h3{color:var(--blue)}
.dcol ul{list-style:none;margin:1.1rem 0 0;padding:0;display:grid;gap:.85rem}
.dcol li{display:flex;gap:.7rem;align-items:flex-start;font-size:.97rem;color:var(--ink-soft)}
.dcol li svg{flex:0 0 auto;width:20px;height:20px;margin-top:.15rem;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.dcol.without li svg{stroke:#C4452A}
.dcol.with li svg{stroke:var(--blue)}
.dcol.with li{color:var(--ink)}
.diff-cta{margin-top:1.4rem;text-align:center}
/* The example card is rounded, but .brief-body paints an opaque white square on
   top of the bottom two corners, so the card looked cut off. Round the body's
   bottom instead of clipping the card with overflow:hidden, which would eat the
   EXAMPLE badge sitting above the top edge. */
.brief > :last-child{border-bottom-left-radius:calc(var(--r-lg) - 1px);border-bottom-right-radius:calc(var(--r-lg) - 1px)}
/* form tweaks */
/* Continue, Back and the submit button run the full width of the form card, so
   they line up with the input above them. .stepnav was a wrapping flex row, so
   the buttons stack instead of sitting side by side. Text stays centred. */
.form-card .stepnav{flex-direction:column;align-items:stretch;gap:.65rem}
.form-card .stepnav .btn{width:100%;padding-left:1rem;padding-right:1rem;text-align:center}
.opt-tag{font-weight:400;color:var(--ink-faint);font-size:.88em}
.help{margin-top:.5rem;font-size:.85rem;color:var(--ink-faint)}
/* Two centred lines under the form, replacing the four-tick reassurance grid.
   The perk carries the weight, the privacy note sits quieter below it. The
   grid and border rules in style.css still target .reassure, so reset them. */
.perk{display:flex;align-items:center;justify-content:center;gap:.45rem;
  margin:1.5rem 0 0;padding-top:1.4rem;border-top:1px solid var(--line);
  font-size:.92rem;font-weight:600;color:var(--navy)}
.perk svg{flex:none;color:#167a46}
/* the Flemish line is 0.2px too wide for a 375px card, so it broke onto two
   rows. A hair smaller on phones keeps both languages on one line. */
@media(max-width:420px){.perk{font-size:.85rem;text-align:center}}
.reassure{display:flex;align-items:center;justify-content:center;gap:.38rem;
  margin-top:.5rem;padding-top:0;border-top:0;
  font-size:.82rem;font-weight:400;color:var(--ink-faint)}
.reassure svg{flex:none}
.opts label strong{margin-top:.1rem}
@media(max-width:959px){.hero-cta{justify-content:flex-start}}
@media(max-width:899px){.navright .navlinks{display:none}}
/* .hero-cta used to hold a button next to this link. The button is gone, so the
   link sits flush with the copy above it instead of being centred in a row. */
.hero-cta{margin-left:-.4rem}
"""

JS = r"""
(function(){
  'use strict';
  var T = __I18N__;
  var FORM_ENDPOINT = '__WEBHOOK__';
  var form = document.getElementById('brief-form');
  var bar = document.getElementById('bar'), ptxt = document.getElementById('ptxt');
  var doneBox = document.getElementById('done');
  form.setAttribute('action', FORM_ENDPOINT);

  /* ---------- attribution: UTMs and click ids ----------
     Values from the URL win. Without them we fall back to what this
     visitor arrived with earlier (stored for 30 days), so switching
     between the EN and NL page or coming back later keeps the source.
     Values are only ever written to input.value, capped at 200 chars. */
  var KEYS = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','li_fat_id','gclid','fbclid'];
  function set(id, val){ var el = document.getElementById(id); if (el) el.value = String(val == null ? '' : val).slice(0, 200); }
  var q = new URLSearchParams(location.search), fromUrl = {}, has = false;
  KEYS.forEach(function(k){ var v = q.get(k); if (v) { fromUrl[k] = v; has = true; } });
  var attr = fromUrl, STORE = 'polpo_lp_attr';
  try {
    if (has) {
      localStorage.setItem(STORE, JSON.stringify({ t: Date.now(), v: fromUrl, landing: location.pathname }));
    } else {
      var saved = JSON.parse(localStorage.getItem(STORE) || 'null');
      if (saved && Date.now() - saved.t < 30 * 864e5) attr = saved.v || {};
    }
  } catch (err) {}
  KEYS.forEach(function(k){ set('f-' + k, attr[k] || ''); });
  set('f-url', location.origin + location.pathname);
  set('f-ref', document.referrer);
  set('f-loaded', Date.now());

  /* language switch keeps the query string (and so the UTMs) */
  document.querySelectorAll('[data-keepq]').forEach(function(a){ if (location.search) a.href = a.getAttribute('href') + location.search; });

  /* ---------- reveal on scroll ---------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rises = document.querySelectorAll('.rise');
  if (reduce || !('IntersectionObserver' in window)) {
    rises.forEach(function(n){ n.classList.add('in'); });
    document.querySelectorAll('.draw').forEach(function(n){ n.classList.add('drawn'); });
    document.querySelector('.glass').classList.add('drawn');
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        if (en.target.classList.contains('draw')) en.target.classList.add('drawn');
        io.unobserve(en.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    /* .draw nodes are observed too, not just .rise, so elements that only draw a
       stroke still get their class when they come into view. */
    document.querySelectorAll('.rise,.draw').forEach(function(n){ io.observe(n); });
    requestAnimationFrame(function(){ document.querySelector('.glass').classList.add('drawn'); });
  }

  /* ---------- scroll progress, sticky bar ---------- */
  var fill = document.getElementById('sprog-fill'), sticky = document.getElementById('sticky');
  var ask = document.getElementById('request');
  var hero = document.querySelector('.hero');
  var ticking = false;
  function onScroll(){
    var y = window.pageYOffset || document.documentElement.scrollTop;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    fill.style.transform = 'scaleX(' + (max > 0 ? Math.min(y / max, 1) : 0) + ')';
    var r = ask.getBoundingClientRect();
    var past = y > hero.offsetHeight * 0.8;
    var formVisible = r.top < window.innerHeight * 0.85 && r.bottom > window.innerHeight * 0.15;
    sticky.classList.toggle('up', past && !formVisible);
    ticking = false;
  }
  window.addEventListener('scroll', function(){ if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---------- questionnaire: four steps ----------
     One check per .stepset, in order. Step 2 (context) is optional, so it
     always passes. Keep this array the same length as the fieldsets. */
  var steps = [].slice.call(form.querySelectorAll('.stepset')), TOTAL = steps.length, at = 0;
  function fail(id, msg){ var el = document.getElementById(id); if (el) el.textContent = msg || ''; return !msg; }
  var checks = [
    function(){ return fail('e-dossier', document.getElementById('dossier').value.trim() ? '' : T.e_dossier); },
    function(){ return true; },
    function(){ return fail('e-level', form.querySelectorAll('input[name="policy_level"]:checked').length ? '' : T.e_level); },
    function(){
      var ok = fail('e-name', document.getElementById('full_name').value.trim() ? '' : T.e_name);
      var em = document.getElementById('work_email').value.trim();
      ok = fail('e-email', /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em) ? '' : T.e_email) && ok;
      ok = fail('e-consent', document.getElementById('consent').checked ? '' : T.e_consent) && ok;
      return ok;
    }
  ];
  function show(i, focus){
    at = i;
    steps.forEach(function(s, n){ s.hidden = n !== i; });
    bar.style.transform = 'scaleX(' + ((i + 1) / TOTAL) + ')';
    ptxt.textContent = T.step_of.replace('{n}', i + 1).replace('{t}', TOTAL);
    if (i === TOTAL - 1) {
      var d = document.getElementById('dossier').value.trim(), echo = document.getElementById('echo');
      echo.innerHTML = d ? T.echo_with : T.echo_default;
      if (d) echo.querySelector('b').textContent = d;
    }
    if (focus !== false) {
      var f = steps[i].querySelector('input:not([type=hidden]):not([type=checkbox]):not([type=radio]), textarea');
      if (f) f.focus({ preventScroll: true });
    }
  }
  function go(i){
    if (i > at && !checks[at]()) return;
    show(i);
    var top = ask.getBoundingClientRect().top + window.pageYOffset - 24;
    if (top < window.pageYOffset) window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
  }
  form.addEventListener('click', function(ev){
    var t = ev.target.closest('[data-next],[data-back],[data-fill]');
    if (!t) return;
    if (t.hasAttribute('data-fill')) {
      var inp = document.getElementById('dossier'); inp.value = t.getAttribute('data-fill'); fail('e-dossier', ''); inp.focus();
    } else if (t.hasAttribute('data-back')) { show(Math.max(at - 1, 0)); }
    else { go(Math.min(at + 1, TOTAL - 1)); }
  });
  form.addEventListener('keydown', function(ev){
    if (ev.key !== 'Enter' || ev.target.tagName === 'TEXTAREA') return;
    if (at < TOTAL - 1) { ev.preventDefault(); go(at + 1); }
  });
  form.addEventListener('input', function(ev){
    var map = { dossier: 'e-dossier', full_name: 'e-name', work_email: 'e-email' };
    if (map[ev.target.id]) fail(map[ev.target.id], '');
  });
  form.addEventListener('change', function(ev){
    if (ev.target.name === 'policy_level') fail('e-level', '');
    if (ev.target.id === 'consent') fail('e-consent', '');
  });
  show(0, false);

  form.addEventListener('submit', function(ev){
    ev.preventDefault();
    if (at < TOTAL - 1) { go(at + 1); return; }
    if (!checks[TOTAL - 1]()) return;
    set('f-submitted', new Date().toISOString());
    var btn = document.getElementById('send');
    btn.disabled = true; btn.textContent = T.sending; fail('e-form', '');
    var data = {};
    new FormData(form).forEach(function(v, k){
      if (data[k] === undefined) data[k] = v;
      else if (Array.isArray(data[k])) data[k].push(v);
      else data[k] = [data[k], v];
    });
    fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
    .then(function(r){
      if (!r.ok) throw new Error('bad status');
      form.hidden = true;
      document.querySelector('.progress').style.display = 'none';
      doneBox.hidden = false;
      doneBox.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
      if (window.lintrk) { window.lintrk('track', { conversion_id: 32953169 }); }
    }).catch(function(){
      btn.disabled = false; btn.textContent = T.submit; fail('e-form', T.e_form);
    });
  });
})();
"""


COOKIE_TXT = {
    "en": {"text": "We use cookies, some of them for marketing.", "yes": "Accept", "no": "Decline"},
    "nl-BE": {"text": "We gebruiken cookies, sommige ervan voor marketing.", "yes": "Accepteren", "no": "Weigeren"},
}

COOKIE_JS = r"""
(function(){
  var KEY = 'polpo_cookie_choice', PID = '__LI_PID__';
  var banner = document.getElementById('cookie-banner');
  function get(){ try { return localStorage.getItem(KEY); } catch (err) { return null; } }
  function save(v){ try { localStorage.setItem(KEY, v); } catch (err) {} }
  function loadLinkedIn(){
    if (!PID || window._liLoaded) return;
    window._liLoaded = true;
    window._linkedin_partner_id = PID;
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(PID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://snap.licdn.com/li.lms-analytics/insight.min.js';
    document.body.appendChild(s);
  }
  var choice = get();
  if (choice === 'yes') loadLinkedIn();
  if (choice) return;
  banner.hidden = false;
  banner.querySelector('[data-accept]').addEventListener('click', function(){
    save('yes'); banner.hidden = true; loadLinkedIn();
  });
  banner.querySelector('[data-decline]').addEventListener('click', function(){
    save('no'); banner.hidden = true;
  });
})();
"""
COOKIE_JS_READY = COOKIE_JS.replace("__LI_PID__", LINKEDIN_PARTNER_ID)

COOKIE_CSS = """<style>
.cookie{position:fixed;left:16px;right:16px;bottom:16px;max-width:560px;margin:0 auto;background:var(--paper,#fff);color:var(--ink,#0D143D);border:1px solid var(--line,#E2E7F0);border-radius:var(--r-md,16px);box-shadow:0 18px 40px -16px rgba(13,20,61,.28);padding:18px 20px;font:500 15px/1.5 Poppins,system-ui,sans-serif;z-index:1000}
.cookie[hidden]{display:none}
.cookie p{margin:0 0 14px}
.cookie-btns{display:flex;gap:10px;justify-content:flex-end}
.cookie button{font:600 14px Poppins,system-ui,sans-serif;border-radius:999px;padding:10px 20px;cursor:pointer;min-width:112px;transition:background .2s,color .2s,border-color .2s}
.cookie-no{background:#fff;color:#545C79;border:1px solid #CBD3E3}
.cookie-no:hover{background:#F4F6FA;color:#0D143D;border-color:#646C85}
.cookie-yes{background:#CE3E09;color:#fff;border:1px solid #CE3E09}
.cookie-yes:hover{background:#B33305;border-color:#B33305}
.cookie button:focus-visible{outline:2px solid #CE3E09;outline-offset:2px}
</style>"""


def page(C):
    other_url = SITE + C["other_path"]
    self_url = SITE + C["path"]
    h1 = "".join('<span class="l">%s</span>' % e(x) for x in C["h1"])
    wins = "".join("<li>%s%s</li>" % (CHECK, e(w)) for w in C["wins"])
    verts = "".join('<span class="vchip" title="%s"><span class="flag" aria-hidden="true">%s</span>%s</span>' % (e(full), f, e(v))
                    for f, v, full in C["verts"])
    logos = "".join('<img src="%s%s" alt="%s" width="%d" height="140" style="--s:%s" loading="lazy" decoding="async">' % (ASSET, f, e(a), w, s)
                    for f, a, w, s in LOGOS)
    steps = ""
    for i, (t, b, plab, ptxt) in enumerate(C["steps"]):
        pico = '<span class="pv-search">%s</span>' % BICONS[0] if i == 0 else '<span class="pv-ok">%s</span>' % CHECK
        steps += ('<div class="scard"><div class="scard-top"><div class="step-n">%02d</div><div class="step-ico">%s</div></div>'
                  '<h3>%s</h3><p>%s</p>'
                  '<div class="step-prev"><span class="step-prev-lab">%s</span>'
                  '<div class="step-prev-row">%s<span>%s</span></div></div></div>'
                  ) % (i + 1, STEPICONS[i], e(t), e(b), e(plab), pico, e(ptxt))
    bcards = "".join('<div class="bcard"><div class="bsec-ico">%s</div><h3>%s</h3><p>%s</p></div>' % (BICONS[i], e(t), e(b))
                     for i, (t, b) in enumerate(C["bcards"]))
    v_head = "".join("<span>%s</span>" % e(x) for x in C["v_head"])
    v_body = "".join('<p class="lede">%s</p>' % e(p) for p in C["v_body"])
    rows = ""
    for k, v in C["mock_rows"]:
        rows += "<dt>%s</dt><dd>%s</dd>" % (e(k), e(v))
    tags = "".join('<span class="tag">%s</span>' % e(t) for t in C["mock_tags"][1:])
    wo = "".join("<li>%s%s</li>" % (CROSS, e(x)) for x in C["d_wo"])
    w = "".join("<li>%s%s</li>" % (CHECK, e(x)) for x in C["d_w"])
    sugs = "".join('<button type="button" data-fill="%s">%s</button>' % (e(s), e(s)) for s in C["sugs"])
    lvls = ""
    for code in C["lvl_order"]:
        k = code.lower()
        req = " required" if code == C["lvl_order"][0] else ""
        lvls += ('<input type="radio" id="lvl-%s" name="policy_level" value="%s"%s>'
                 '<label for="lvl-%s">%s<strong>%s</strong></label>') % (k, code, req, k, ICON[k], e(C["lvl"][code]))
    perk = ('<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
            '<circle cx="12" cy="12" r="9"/><path d="m8.4 12.3 2.4 2.4 4.8-5.2"/></svg>'
            '<span>%s</span>') % e(C["perk"])
    reassure = ('<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true" focusable="false">'
                '<path d="M12 1.5a4.5 4.5 0 0 0-4.5 4.5v3H7A2.5 2.5 0 0 0 4.5 11.5v7A2.5 2.5 0 0 0 7 21h10a2.5 2.5 0 0 0 2.5-2.5v-7A2.5 2.5 0 0 0 17 9h-.5V6A4.5 4.5 0 0 0 12 1.5Zm2.5 7.5h-5V6a2.5 2.5 0 0 1 5 0v3Z"/></svg>'
                '<span>%s</span>') % e(C["reassure"])
    faqs = "".join('<details class="faq"><summary>%s</summary><div class="details-body">%s</div></details>' % (e(qq), e(aa)) for qq, aa in C["faq"])
    i18n = {k: C[k] for k in ["step_of", "echo_default", "echo_with", "e_dossier", "e_level", "e_name", "e_email", "e_consent", "e_form", "sending", "submit"]}
    js = JS.replace("__I18N__", json.dumps(i18n, ensure_ascii=False)).replace("__WEBHOOK__", WEBHOOK)

    return f"""<!DOCTYPE html>
<html lang="{C['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(C['title'])}</title>
<meta name="description" content="{e(C['desc'])}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="en" href="{SITE}/">
<link rel="alternate" hreflang="nl-BE" href="{SITE}/nl-be/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="{C['og_locale']}">
<meta property="og:title" content="{e(C['title'])}">
<meta property="og:description" content="{e(C['desc'])}">
<meta property="og:url" content="{self_url}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1000">
<meta property="og:image:height" content="1249">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(C['title'])}">
<meta name="twitter:description" content="{e(C['desc'])}">
<meta name="twitter:image" content="{SITE}/og-image.jpg">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{BASE_CSS}{EXTRA_CSS}</style>
</head>
<body class="no-js">
<script>document.body.classList.remove('no-js');document.body.classList.add('js');</script>
<div class="sprog" aria-hidden="true"><i id="sprog-fill"></i></div>
{SPRITE}

<header class="hero">
  <div class="blob blob-a"></div><div class="blob blob-b"></div><div class="blob blob-c"></div>
  {STARS}
  <div class="wrap">
    <nav class="topbar">
      <a class="logo-link" href="{C['polpo_url']}" aria-label="Polpo"><svg class="logo" viewBox="0 0 171 79" role="img" aria-label="Polpo"><use href="#polpo-white"/></svg></a>
      <div class="navright">
        <div class="navlinks"><a href="#how">{e(C['nav_how'])}</a><a href="#ready">{e(C['nav_ready'])}</a><a href="#faq">{e(C['nav_faq'])}</a></div>
        <div class="langsw"><span aria-current="page">{C['sw_self']}</span><a href="{C['other_path']}" hreflang="{'nl-BE' if C['lang']=='en' else 'en'}" lang="{'nl-BE' if C['lang']=='en' else 'en'}" aria-label="{e(C['sw_other_label'])}" data-keepq>{C['sw_other']}</a></div>
      </div>
    </nav>

    <div class="hero-grid">
      <div class="glass">
        <span class="chip">{e(C['eyebrow'])}</span>
        <h1>{h1}</h1>
        <p class="hero-sub">{e(C['h2'])}</p>
        <!-- No primary button here. The form sits in the next hero column, and on
             mobile right below this block, so a button pointing at #request would
             only scroll the visitor to something already in front of them. The
             form's own Continue button is the primary action. -->
        <p class="hero-cta"><a class="textlink" href="#how">{e(C['cta2'])}<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg></a></p>
        <div class="verts"><span class="verts-l">{e(C['vert_label'])}</span><div class="vrow">{verts}</div></div>
      </div>
      <!-- The request form now lives above the fold. It is the SAME single form
           element as before, moved, not copied: same id, same action, same hidden
           fields, same script. id="request" stays on the wrapper so every existing
           href="#request" CTA still lands on it. -->
      <div class="hero-media" id="request">
        <div class="form-card">
          <div class="form-card-head">
            <h2>{e(C['f_head'])}</h2>
            <p>{e(C['f_intro'])}</p>
          </div>
          <div class="progress" aria-hidden="true">
            <div class="progress-bar"><div class="progress-fill" id="bar"></div></div>
            <span class="progress-txt" id="ptxt"></span>
          </div>
          <!-- FORM ENDPOINT: production n8n webhook. Keep the action attribute and
               FORM_ENDPOINT in the script identical.
               Fields sent (JSON): dossier, context, policy_level (one of EU / NL / BE),
               full_name, work_email, consent, offer, lang, page_url, referrer,
               utm_source, utm_medium, utm_campaign, utm_content, utm_term,
               li_fat_id, gclid, fbclid, submitted_at, ts_loaded,
               hp_company_website (spam trap, must be empty). -->
          <form id="brief-form" action="{WEBHOOK}" method="post" novalidate>
            <fieldset class="stepset" id="st1">
              <legend class="sr-only">{e(C['f_head'])}</legend>
              <div class="field">
                <label for="dossier">{e(C['l_dossier'])} <span class="req" aria-hidden="true">*</span></label>
                <input type="text" id="dossier" name="dossier" required autocomplete="off" enterkeyhint="next" placeholder="{e(C['ph_dossier'])}">
                <p class="err" id="e-dossier"></p>
                <div class="sugs"><span>{e(C['sugs_label'])}</span>{sugs}</div>
              </div>
              <div class="stepnav"><button type="button" class="btn" data-next>{e(C['b_continue'])}</button></div>
            </fieldset>

            <fieldset class="stepset" id="st2">
              <legend class="sr-only">{e(C['l_context'])}</legend>
              <div class="field">
                <label for="context">{e(C['l_context'])} <span class="opt-tag">({e(C['optional'])})</span></label>
                <textarea id="context" name="context" placeholder="{e(C['ph_context'])}" aria-describedby="h-context"></textarea>
                <p class="help" id="h-context">{e(C['help_context'])}</p>
              </div>
              <div class="stepnav">
                <button type="button" class="btn" data-next>{e(C['b_continue'])}</button>
                <button type="button" class="btn btn-ghost" data-back>{e(C['b_back'])}</button>
              </div>
            </fieldset>

            <fieldset class="stepset" id="st3">
              <legend>{e(C['l_level'])} <span class="req" aria-hidden="true">*</span></legend>
              <span class="sr-only">{e(C['sr_pick'])}</span>
              <div class="opts" role="radiogroup" aria-label="{e(C['l_level'])}">{lvls}</div>
              <p class="err" id="e-level"></p>
              <div class="stepnav">
                <button type="button" class="btn" data-next>{e(C['b_continue'])}</button>
                <button type="button" class="btn btn-ghost" data-back>{e(C['b_back'])}</button>
              </div>
            </fieldset>

            <fieldset class="stepset" id="st4">
              <legend class="sr-only">{e(C['l_name'])}</legend>
              <p class="legend-sub" id="echo">{e(C['echo_default'])}</p>
              <div class="field">
                <label for="full_name">{e(C['l_name'])} <span class="req" aria-hidden="true">*</span></label>
                <input type="text" id="full_name" name="full_name" required autocomplete="name" enterkeyhint="next" placeholder="{e(C['ph_name'])}">
                <p class="err" id="e-name"></p>
              </div>
              <div class="field">
                <label for="work_email">{e(C['l_email'])} <span class="req" aria-hidden="true">*</span></label>
                <input type="email" id="work_email" name="work_email" required autocomplete="email" inputmode="email" enterkeyhint="done" placeholder="{e(C['ph_email'])}">
                <p class="err" id="e-email"></p>
              </div>
              <div class="consent">
                <label class="check"><input type="checkbox" name="consent" value="yes" id="consent" required><span>{C['consent']}</span></label>
                <p class="err" id="e-consent"></p>
              </div>
              <div class="stepnav">
                <button type="submit" class="btn btn-wide" id="send">{e(C['submit'])}</button>
                <button type="button" class="btn btn-ghost" data-back>{e(C['b_back'])}</button>
              </div>
              <p class="err" id="e-form"></p>
            </fieldset>

            <div class="trap" aria-hidden="true"><label for="hp">Company website</label><input type="text" id="hp" name="hp_company_website" tabindex="-1" autocomplete="off"></div>
            <input type="hidden" name="offer" value="trial-30d">
            <input type="hidden" name="lang" value="{C['lang']}">
            <input type="hidden" name="submitted_at" id="f-submitted">
            <input type="hidden" name="ts_loaded" id="f-loaded">
            <input type="hidden" name="page_url" id="f-url">
            <input type="hidden" name="referrer" id="f-ref">
            <input type="hidden" name="utm_source" id="f-utm_source">
            <input type="hidden" name="utm_medium" id="f-utm_medium">
            <input type="hidden" name="utm_campaign" id="f-utm_campaign">
            <input type="hidden" name="utm_content" id="f-utm_content">
            <input type="hidden" name="utm_term" id="f-utm_term">
            <input type="hidden" name="li_fat_id" id="f-li_fat_id">
            <input type="hidden" name="gclid" id="f-gclid">
            <input type="hidden" name="fbclid" id="f-fbclid">
          </form>

          <div class="done" id="done" hidden>
            <div class="done-ico">{CHECK}</div>
            <h3>{e(C['done_t'])}</h3>
            <p id="done-msg">{e(C['done_b'])}</p>
          </div>

          <p class="perk">{perk}</p>
          <p class="reassure" id="reassure">{reassure}</p>
        </div>
      </div>
    </div>

    <div class="hero-logos">
      <p>{e(C['logos_cap'])}</p>
      <div class="logos-row">{logos}</div>
    </div>
  </div>
</header>

<main>
<section class="band" id="how">
  <div class="wrap">
    <div class="narrow rise head-wide"><h2>{e(C['p_head'])}</h2></div>
    <div class="steps2 rise">{steps}</div>
    <div class="outcome rise">
      <a class="btn" href="#request">{e(C['cta'])}{SPARK}</a>
    </div>
  </div>
</section>

<section class="band band-mist" id="ready">
  <div class="wrap">
    <div class="narrow rise head-wide head-center"><h2 class="stack">{v_head}</h2>{v_body}</div>
    <div class="ready-grid">
      <div class="brief rise is-preview">
        <span class="preview-tag">{e(C['mock_tags'][0])}</span>
        <div class="brief-head"><h3>{e(C['mock_head'])}</h3><div class="brief-meta">{tags}</div></div>
        <div class="brief-body"><div class="bsnap"><dl>{rows}</dl></div></div>
      </div>
      <div class="rise">
        <h3 class="b-head">{e(C['b_head'])}</h3>
        <div class="bcards" style="margin-top:1.25rem">{bcards}</div>
      </div>
    </div>
  </div>
</section>

<section class="band" id="difference">
  <div class="wrap">
    <div class="narrow rise head-wide head-center diff-head">
      <p class="eyebrow">{e(C['d_eyebrow'])}</p>
      <h2>{e(C['d_head'])}</h2>
      <p class="lede">{e(C['d_sub'])}</p>
    </div>
    <div class="diff rise">
      <div class="dcol without"><h3>{e(C['d_without'])}</h3><ul>{wo}</ul></div>
      <div class="dcol with"><h3>{e(C['d_with'])}</h3><ul>{w}</ul></div>
    </div>
    <p class="diff-close rise">{e(C['d_close'])}</p>
    <div class="diff-cta rise"><a class="btn" href="#request">{e(C['cta'])}{SPARK}</a></div>
  </div>
</section>

<section class="band" id="faq">
  <div class="wrap">
    <div class="narrow rise"><h2>{e(C['faq_head'])}</h2></div>
    <div class="faqs rise">{faqs}</div>
  </div>
</section>

<section class="band band-navy close">
  <div class="wrap rise">
    <h2>{e(C['z_head'])}</h2>
    <p class="lede">{e(C['z_body'])}</p>
    <div class="close-cta"><a class="btn" href="#request">{e(C['cta'])}{SPARK}</a></div>
  </div>
</section>

<div class="sticky" id="sticky">
  <p>{e(C['sticky'])}</p>
  <a class="btn" href="#request">{e(C['cta'])}{SPARK}</a>
</div>
</main>

<footer class="foot">
  <div class="wrap foot-in">
    <a class="logo-link" href="{C['polpo_url']}" aria-label="Polpo"><svg class="logo" viewBox="0 0 225.212 72.477" role="img" aria-label="Polpo"><use href="#polpo-mark"/></svg></a>
    <p>{e(C['foot_tag'])}</p>
    <a href="{C['polpo_url']}">polpo.com</a>
  </div>
</footer>

{COOKIE_CSS}
<div class="cookie" id="cookie-banner" role="dialog" aria-live="polite" hidden>
  <p>{e(COOKIE_TXT[C['html_lang']]['text'])}</p>
  <div class="cookie-btns">
    <button type="button" class="cookie-no" data-decline>{e(COOKIE_TXT[C['html_lang']]['no'])}</button>
    <button type="button" class="cookie-yes" data-accept>{e(COOKIE_TXT[C['html_lang']]['yes'])}</button>
  </div>
</div>
<script>{COOKIE_JS_READY}</script>
<script>{js}</script>
</body>
</html>
"""


os.makedirs(os.path.join(OUT, "nl-be"), exist_ok=True)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page(EN))
open(os.path.join(OUT, "nl-be", "index.html"), "w", encoding="utf-8").write(page(NL))
print("built", OUT)
