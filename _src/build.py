# -*- coding: utf-8 -*-
"""Static site generator for 55596.com. Run: python3 _src/build.py  (outputs into the repo root)."""
import json, os, re, sys, html, datetime
sys.path.insert(0, os.path.dirname(__file__))
from data import DIGITS, KEYPAD, MASTER, COMBOS, SLANG, NUMBERS, NUMBER_ORDER, VIDEOS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMAIN = "https://55596.com"
PUB = "ca-pub-6620975821265271"
TODAY = datetime.date(2026, 10, 15).isoformat()
ADSENSE = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB}" crossorigin="anonymous"></script>'
SITEMAP = []

NAV = [("decode.html", "Decoder"), ("angel-numbers.html", "Angel numbers"), ("numerology.html", "Numerology"),
       ("culture.html", "Culture"), ("slang.html", "Slang"), ("tools.html", "Tools"), ("guides.html", "Guides")]

def esc(s): return html.escape(str(s), quote=True)

def keys(s, size=""):
    out = []
    for d in s:
        st = DIGITS[d]["zh"]["status"]
        out.append(f'<span class="key {size} {st}"><b>{d}</b><small>{KEYPAD[d] or "&nbsp;"}</small></span>')
    return '<div class="keys" aria-hidden="true">' + "".join(out) + "</div>"

def layout(path, title, desc, body, *, crumbs=None, schema=None, noads=False, robots="index,follow", active=None, og_type="website"):
    depth = path.count("/")
    R = "../" * depth
    canon = DOMAIN + "/" + (path[:-10] if path.endswith("index.html") else path)
    body = body.replace("~/", R)
    nav = "".join(f'<a href="{R}{h}"{" aria-current=\"page\"" if active == h else ""}>{t}</a>' for h, t in NAV)
    crumb_html = ""
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": "55596", "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/favicon.svg"}]
    if crumbs:
        items = [("Home", "index.html")] + crumbs
        crumb_html = '<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>' + "".join(
            (f'<li><a href="{R}{u}">{esc(n)}</a></li>' if u else f'<li aria-current="page">{esc(n)}</li>') for n, u in items) + "</ol></nav>"
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, **({"item": DOMAIN + "/" + (u[:-10] if u.endswith("index.html") else u)} if u else {})}
            for i, (n, u) in enumerate(items)]})
    if schema: ld.extend(schema if isinstance(schema, list) else [schema])
    base_js = ""
    if path == "404.html":
        base_js = ('<script>(function(){var p=location.hostname.slice(-10)==="github.io"?"/"+location.pathname.split("/")[1]+"/":"/";'
                   'document.write(\'<base href="\'+p+\'">\');})();</script>')
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    page = f"""<!doctype html>
<html lang="en" data-root="{R}">
<head>
<meta charset="utf-8">
{base_js}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="55596">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#151936">
<meta name="google-adsense-account" content="{PUB}">
<link rel="icon" href="{R}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{R}assets/img/favicon.svg">
<link rel="manifest" href="{R}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/css/site.css">
{ADSENSE}
{ld_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="https://web.works/contact" rel="noopener" target="_blank">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership</a></div>
<header class="site-head">
 <div class="wrap head-in">
  <a class="brand" href="{R}index.html" aria-label="55596 home"><span class="brand-keys" aria-hidden="true"><span>5</span><span>5</span><span>5</span><span>9</span><span>6</span></span><span class="brand-name">55596</span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn small gold" href="{R}lucky-numbers.html">Get a lucky number</a><button class="theme-btn" aria-label="Switch light or dark theme" title="Theme">◐</button></nav>
 </div>
</header>
{crumb_html}
<main id="main">
{body}
</main>
<footer class="site-foot">
 <div class="wrap">
  <div class="foot-grid">
   <div><a class="brand" href="{R}index.html"><span class="brand-keys" aria-hidden="true"><span>5</span><span>5</span><span>5</span><span>9</span><span>6</span></span><span class="brand-name">55596</span></a>
    <p class="muted mt1">Decode any number — angel numbers, numerology, cultural lucky numbers, internet slang and math facts in one place. Meanings are cultural traditions shared for education and entertainment.</p>
    <a class="btn small gold" href="{R}support.html">Support 55596</a></div>
   <div><h4>Explore</h4><ul><li><a href="{R}decode.html">Number decoder</a></li><li><a href="{R}numbers.html">Number index</a></li><li><a href="{R}angel-numbers.html">Angel numbers</a></li><li><a href="{R}numerology.html">Numerology</a></li><li><a href="{R}culture.html">Lucky numbers by culture</a></li><li><a href="{R}slang.html">Number slang</a></li></ul></div>
   <div><h4>Tools</h4><ul><li><a href="{R}tools/life-path-calculator.html">Life path</a></li><li><a href="{R}tools/name-number-calculator.html">Name number</a></li><li><a href="{R}tools/lucky-phone-number.html">Lucky phone score</a></li><li><a href="{R}tools/lucky-plate-number.html">Lucky plate score</a></li><li><a href="{R}tools/lucky-address-number.html">Lucky address score</a></li><li><a href="{R}tools.html">All tools</a></li></ul></div>
   <div><h4>Work with us</h4><ul><li><a href="{R}lucky-numbers.html">Lucky &amp; vanity numbers</a></li><li><a href="{R}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{R}contests.html">Contests &amp; prizes</a></li><li><a href="{R}careers.html">Careers</a></li><li><a href="{R}support.html">Donate &amp; support</a></li><li><a href="{R}contact.html">Contact</a></li></ul></div>
   <div><h4>About &amp; legal</h4><ul><li><a href="{R}about.html">About</a></li><li><a href="{R}editorial-standards.html">Editorial standards</a></li><li><a href="{R}privacy.html">Privacy policy</a></li><li><a href="{R}terms.html">Terms of use</a></li><li><a href="{R}cookies.html">Cookie policy</a></li><li><a href="{R}disclaimer.html">Disclaimer</a></li><li><a href="{R}trademark-copyright.html">Trademark &amp; copyright</a></li><li><a href="{R}affiliate-disclosure.html">Advertising disclosure</a></li></ul></div>
  </div>
  <p class="legal-line">© <span data-year>2026</span> 55596.com. Independent publication. "55596" is used as a numeric domain name and is not affiliated with any company, product, telephone service, postcode or trademark containing the digits 555 or 96. See <a href="{R}trademark-copyright.html">Trademark &amp; copyright</a>.</p>
 </div>
</footer>
<nav class="mbar" aria-label="Quick actions"><a href="{R}decode.html">Decode</a><a href="{R}tools/lucky-phone-number.html">Score my number</a><a class="go" href="{R}lucky-numbers.html">Get lucky #</a></nav>
<script src="{R}assets/js/data.js"></script>
<script src="{R}assets/js/engine.js"></script>
<script src="{R}assets/js/site.js" defer></script>
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f: f.write(page)
    if robots.startswith("index"):
        pr = "1.0" if path == "index.html" else ("0.8" if depth == 0 else "0.7")
        SITEMAP.append((canon, pr))

def faq_schema(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def faq_html(faq):
    return "".join(f"<details><summary>{esc(q)}</summary><div><p>{esc(a)}</p></div></details>" for q, a in faq)

def video_card(v):
    return (f'<div><div class="video"><button data-id="{v["id"]}" aria-label="Play video: {esc(v["title"])}"><span></span></button></div>'
            f'<div class="video-meta"><b>{esc(v["title"])}</b><span>{esc(v["channel"])} · YouTube</span></div></div>')

def lead_cta(title="Need a lucky or memorable number for your business?", text="We source lucky and vanity phone numbers, licence-plate style numbers and numeric domain names worldwide — including 8-heavy, 168, 518 and repeating patterns."):
    return f'''<div class="cta-band mt3"><div><h2>{esc(title)}</h2><p>{esc(text)}</p></div><div><a class="btn gold" href="~/lucky-numbers.html">Request a lucky number</a></div></div>'''

def form_field(name, label, kind="text", req=True, opts=None, ph="", auto=""):
    r = ' required' if req else ''
    star = ' <span class="req" aria-hidden="true">*</span>' if req else ''
    fid = "f-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    a = f' autocomplete="{auto}"' if auto else ''
    if kind == "select":
        o = "".join(f"<option>{esc(x)}</option>" for x in opts)
        return f'<div><label for="{fid}">{esc(label)}{star}</label><select id="{fid}" name="{esc(name)}"{r}><option value="">Choose…</option>{o}</select></div>'
    if kind == "textarea":
        return f'<div><label for="{fid}">{esc(label)}{star}</label><textarea id="{fid}" name="{esc(name)}" placeholder="{esc(ph)}"{r}></textarea></div>'
    return f'<div><label for="{fid}">{esc(label)}{star}</label><input id="{fid}" type="{kind}" name="{esc(name)}" placeholder="{esc(ph)}"{a}{r}></div>'

def consent_box(text="I agree that 55596 may contact me about this request. See the privacy policy."):
    return (f'<label class="check"><input type="checkbox" name="Consent" value="Yes" required><span>{esc(text).replace("privacy policy", "<a href=\"~/privacy.html\">privacy policy</a>")}</span></label>'
            '<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="_hp" tabindex="-1" autocomplete="off"></label></div>')

def simple_form(kind, subject, fields, button, note=""):
    return (f'<form class="form panel" data-form="{kind}" data-subject="{esc(subject)}" novalidate>' + "".join(fields) + consent_box() +
            f'<p class="form-status" role="status" aria-live="polite"></p><div><button class="btn" type="submit">{esc(button)}</button></div>' +
            (f'<p class="hint mt0">{note}</p>' if note else '') + '</form>')

def write_raw(path, text):
    out = os.path.join(ROOT, path); os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f: f.write(text)

def build_data_js():
    pages = NUMBER_ORDER
    data = {"keypad": KEYPAD, "digits": DIGITS, "master": MASTER, "combos": COMBOS, "slang": SLANG, "pages": pages}
    write_raw("assets/js/data.js", "window.N_DATA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")

def inject_key():
    secret = "".join(chr(x) for x in [119, 101, 98, 119, 111, 114, 107, 115, 97, 49, 64, 103, 109, 97, 105, 108, 46, 99, 111, 109])
    e = [ord(c) + 7 for c in secret]
    src = os.path.join(ROOT, "assets/js/site.js")
    s = open(src, encoding="utf-8").read()
    s = re.sub(r"var EK = (__EK__|\[[0-9, ]+\]);", "var EK = " + json.dumps(e) + ";", s)
    open(src, "w", encoding="utf-8").write(s)

def main():
    import pages, guides
    build_data_js(); inject_key()
    pages.build_all()
    guides.build_all()
    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, p in SITEMAP:
        sm.append(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>")
    sm.append("</urlset>")
    write_raw("sitemap.xml", "\n".join(sm) + "\n")
    print("Built", len(SITEMAP), "indexable pages")

if __name__ == "__main__":
    import build
    build.main()
