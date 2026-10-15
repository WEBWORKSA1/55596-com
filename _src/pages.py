# -*- coding: utf-8 -*-
from build import (layout, keys, esc, faq_html, faq_schema, video_card, lead_cta, form_field, consent_box,
                   simple_form, write_raw, DIGITS, KEYPAD, MASTER, COMBOS, SLANG, NUMBERS, NUMBER_ORDER, VIDEOS, DOMAIN, PUB)

# ---------- helpers ----------
def dsum(s): return sum(int(c) for c in s)
def reduce(n, keep=True):
    steps = [n]
    while n > 9 and not (keep and n in (11, 22, 33)):
        n = dsum(str(n)); steps.append(n)
    return n, steps
def root_text(n): return MASTER.get(str(n)) or DIGITS[str(n)]["num"]
def factor(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f
def roman(n):
    if not 0 < n < 4000: return "—"
    m = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    r = ""
    for v, s in m:
        while n >= v: r += s; n -= v
    return r
def math_facts(s):
    n = int(s); out = []
    out.append(("Digits", len(s)))
    if n >= 2:
        f = factor(n); c = {}
        for p in f: c[p] = c.get(p, 0) + 1
        out.append(("Prime?", "Yes" if len(f) == 1 else "No"))
        out.append(("Prime factors", " × ".join(f"{p}^{k}" if k > 1 else str(p) for p, k in c.items())))
        nd = 1
        for k in c.values(): nd *= k + 1
        out.append(("Divisors", nd))
    out += [("Binary", bin(n)[2:]), ("Hexadecimal", hex(n)[2:].upper()), ("Roman", roman(n)),
            ("Palindrome", "Yes" if len(s) > 1 and s == s[::-1] else "No"), ("Even or odd", "Even" if n % 2 == 0 else "Odd")]
    return out
def luck_score(s):
    W = {"8": 6, "6": 4, "9": 4, "2": 2, "3": 1, "5": 0, "1": 0, "0": 0, "7": -1, "4": -7}
    sc = 50 + round(sum(W[c] for c in s) * (7 / max(len(s), 7)) * 1.6)
    if s[-1] in "869": sc += 6
    if s[-1] == "4": sc -= 8
    if "14" in s: sc -= 5
    if "250" in s: sc -= 4
    for c in ["168", "518", "888", "666", "999", "1314", "520"]:
        if c in s: sc += 5
    import re
    for r in re.findall(r"((\d)\2{2,})", s):
        sc += -4 if r[1] == "4" else 4 + (len(r[0]) - 3) * 2
    return max(0, min(100, sc))

def decode_form(value="", big=True, autofocus=False):
    return (f'<form class="decode-form" action="~/decode.html" method="get" role="search">'
            f'<label class="skip" for="hero-n">Number to decode</label>'
            f'<input id="hero-n" name="n" inputmode="numeric" pattern="[0-9 ]*" maxlength="18" placeholder="Type any number…" value="{esc(value)}"{" autofocus" if autofocus else ""}>'
            f'<button class="btn" type="submit">Decode</button></form>')

def chips(nums):
    return '<div class="chip-row">' + "".join(f'<a class="chip" href="~/number/{n}/">{n}</a>' for n in nums) + "</div>"

def numgrid(nums):
    return '<div class="numgrid">' + "".join(f'<a href="~/number/{n}/">{n}<small>{esc(NUMBERS[n]["tag"])}</small></a>' for n in nums) + "</div>"

# ---------- pages ----------
def home():
    body = f'''
<section class="hero"><div class="wrap hero-grid">
 <div>
  <h1>What does your number really mean?</h1>
  <p class="lede">One number, every reading: angel numbers, numerology, Chinese and Asian lucky-number culture, internet slang in a dozen languages, and hard math facts. Free, instant, and private — it all runs in your browser.</p>
  {decode_form()}
  <p class="hint">Try a few: <a href="~/decode.html?n=555">555</a>, <a href="~/decode.html?n=520">520</a>, <a href="~/decode.html?n=1314">1314</a>, <a href="~/decode.html?n=8888">8888</a>, or your own phone number.</p>
 </div>
 <aside class="panel">
  {keys("55596")}
  <p class="eq">5 + 5 + 5 + 9 + 6 = 30 → <strong>3</strong></p>
  <p class="mt0">Laughter in Thai. Tears in Chinese chat. Change in angel numerology. Then 9 for 'long-lasting' and 6 for 'smooth flow'. That's the number this site is named after.</p>
  <a href="~/number/55596/">Read the story of 55596</a>
 </aside>
</div></section>

<section class="section alt"><div class="wrap">
 <div class="section-head"><div><h2>Start with a famous number</h2><p>Each guide combines a written explanation with computed facts and cultural readings.</p></div><a class="btn ghost small" href="~/numbers.html">See the full index</a></div>
 {numgrid(["555","888","520","111","444","1314","666","168","1111","8888","233","1004"])}
</div></section>

<section class="section"><div class="wrap grid g3">
 <a class="tile" href="~/tools/life-path-calculator.html"><h3>Life path calculator</h3><p>Your core numerology number from your date of birth, with master numbers kept.</p></a>
 <a class="tile" href="~/tools/lucky-phone-number.html"><h3>Lucky phone number score</h3><p>A 0–100 score using Chinese homophone tradition and memorability, plus luckier variations.</p></a>
 <a class="tile" href="~/tools/name-number-calculator.html"><h3>Name number</h3><p>Expression, soul urge and personality numbers — Pythagorean or Chaldean.</p></a>
 <a class="tile" href="~/tools/lucky-plate-number.html"><h3>Lucky plate checker</h3><p>Score a licence plate, letters included.</p></a>
 <a class="tile" href="~/tools/lucky-address-number.html"><h3>Lucky address checker</h3><p>House numbers, unit and floor numbers — what buyers from different cultures will see.</p></a>
 <a class="tile" href="~/tools/compatibility-calculator.html"><h3>Compatibility</h3><p>Compare two life path numbers and their number families.</p></a>
</div></section>

<section class="section alt"><div class="wrap split">
 <div>
  <h2>Why the same number means different things</h2>
  <p>Numbers carry meaning through sound. In Mandarin, 8 sounds like 'prosper' and 4 sounds like 'death', so a phone number full of 8s can sell for thousands while a 4th floor gets skipped. In Thai, 5 sounds like 'ha', so 555 is a laugh. In Japanese, 39 sounds like 'thank you'. Numerology adds a separate layer by reducing every number to a single root, and angel-number readers look for repeating patterns.</p>
  <p>55596 puts all of these side by side, so you can see which meaning a reader from each culture would take — useful for a wedding date, a product price, a business phone line or a new domain name.</p>
  <p><a href="~/guides/555-around-the-world.html">Read: what 555 means around the world</a></p>
 </div>
 <div class="panel" id="daily-number"><p>Today's universal number loads here.</p></div>
</div></section>

<section class="section"><div class="wrap">
 <div class="cta-band"><div><h2>Turn a number into a business asset</h2><p>Lucky and memorable numbers convert: callers recall them, buyers trust them, and in Chinese-speaking markets they carry real price premiums. Tell us what you need — a phone number with 8s, a 168 ending, a numeric .com — and we'll source options.</p></div><div><a class="btn gold" href="~/lucky-numbers.html">Request a lucky number</a></div></div>
</div></section>

<section class="section alt"><div class="wrap">
 <div class="section-head"><div><h2>Watch: numbers explained</h2><p>Hand-picked videos on fictional 555 phone numbers, Chinese lucky numbers and number theory.</p></div><a class="btn ghost small" href="~/videos.html">All videos</a></div>
 <div class="grid g3">{"".join(video_card(v) for v in VIDEOS[:3])}</div>
</div></section>

<section class="section"><div class="wrap grid g2">
 <div class="panel">
  <h2>Get the number of the week</h2>
  <p>One number, decoded across every culture, each Monday. No spam; unsubscribe any time.</p>
  <form class="form" data-form="newsletter" data-subject="Newsletter signup" novalidate>
   {form_field("Email", "Email address", "email", auto="email", ph="you@example.com")}
   {form_field("Birthday (optional)", "Birthday — for your personal year reading", "date", req=False)}
   {consent_box("I agree to receive the 55596 newsletter and accept the privacy policy.")}
   <p class="form-status" role="status" aria-live="polite"></p>
   <div><button class="btn" type="submit">Subscribe</button></div>
  </form>
 </div>
 <div class="panel gold">
  <h2>Keep 55596 free</h2>
  <p>We're independent and ad-supported. Your support funds new tools, translations into more languages, monthly contests with prizes, and hiring writers who know their culture's number traditions first-hand.</p>
  <p><a class="btn" href="~/support.html">Support the project</a> <a class="btn ghost" href="~/contests.html">Enter this month's contest</a></p>
 </div>
</div></section>'''
    schema = [{"@context": "https://schema.org", "@type": "WebSite", "name": "55596", "url": DOMAIN + "/",
               "potentialAction": {"@type": "SearchAction", "target": DOMAIN + "/decode.html?n={search_term_string}", "query-input": "required name=search_term_string"}}]
    layout("index.html", "55596 — Decode any number: angel numbers, numerology, lucky numbers & slang",
           "Free number decoder: see what any number means in angel numerology, Chinese and Asian lucky-number culture, internet slang and math — plus life path, lucky phone and plate calculators.",
           body, schema=schema)

def decode_page():
    body = f'''
<section class="page-head wrap" id="decoder">
 <h1>Number decoder</h1>
 <p>Enter up to 15 digits. You'll get the numerology root, angel-number reading, a digit-by-digit Chinese reading with known combinations, slang matches, a luck score and math facts. Nothing you type leaves your device.</p>
 <form class="decode-form" id="decode-form" role="search"><label class="skip" for="decode-input">Number to decode</label><input id="decode-input" inputmode="numeric" maxlength="18" placeholder="Type any number…"><button class="btn" type="submit">Decode</button></form>
 <div id="decode-out" class="result" aria-live="polite"><noscript><p class="note">The decoder needs JavaScript. You can still browse the <a href="~/numbers.html">number index</a>.</p></noscript></div>
</section>
<section class="wrap section"><div class="split">
 <div class="prose">
  <h2>How the decoder works</h2>
  <p><strong>Numerology root.</strong> We add the digits and keep adding until one digit remains, except for the master numbers 11, 22 and 33, which numerologists keep intact.</p>
  <p><strong>Angel reading.</strong> Repeating numbers (555), mirror pairs (1212) and sequences (1234) get a pattern reading; other numbers are read by their dominant digit.</p>
  <p><strong>Culture.</strong> Each digit is shown with its Chinese character and the word it sounds like. We also search the number for well-known combinations such as 168, 520, 1314 and 14.</p>
  <p><strong>Luck score.</strong> A transparent 0–100 score built from digit weights (8, 6 and 9 up; 4 down), the ending digit, unlucky pairs and memorable runs. It reflects tradition and memorability, not destiny.</p>
  <p><strong>Math.</strong> Prime test, factorisation, divisors, binary, hexadecimal, Roman numerals and the number in words.</p>
 </div>
 <aside class="panel sticky"><h3>Popular right now</h3>{chips(["555","444","111","888","1111","520","666","1004","233","7777"])}<p class="mt2"><a href="~/numbers.html">Browse every guide</a></p></aside>
</div>
{lead_cta()}
</section>'''
    layout("decode.html", "Number decoder — what does any number mean? | 55596",
           "Decode any number up to 15 digits: numerology root, angel number meaning, Chinese lucky reading, internet slang, luck score and math facts. Free and private.",
           body, crumbs=[("Decoder", None)], active="decode.html",
           schema={"@context": "https://schema.org", "@type": "WebApplication", "name": "55596 Number Decoder", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}})

def related(n):
    rel = set()
    s = n
    root, _ = reduce(dsum(s))
    if str(root) in NUMBERS: rel.add(str(root))
    for d in set(s):
        for k in (d, d * 2, d * 3, d * 4):
            if k in NUMBERS: rel.add(k)
    for c in COMBOS:
        if c["code"] in s and c["code"] in NUMBERS: rel.add(c["code"])
    rel.discard(n)
    return sorted(rel, key=lambda x: (len(x), x))[:10]

def number_pages():
    order = NUMBER_ORDER
    for i, n in enumerate(order):
        d = NUMBERS[n]
        total = dsum(n); root, steps = reduce(total)
        zh_rows = "".join(f'<tr><td><strong>{c}</strong></td><td>{DIGITS[c]["zh"]["char"]} {DIGITS[c]["zh"]["py"]}</td><td>{esc(DIGITS[c]["zh"]["sounds"])}</td><td><span class="badge {DIGITS[c]["zh"]["status"]}">{DIGITS[c]["zh"]["status"]}</span></td></tr>'
                          for c in dict.fromkeys(n))
        combo_hits = [c for c in COMBOS if c["code"] in n]
        combos_html = "".join(f'<li><span class="badge {c["status"]}">{c["code"]}</span> <strong>{esc(c["region"])}:</strong> {esc(c["reading"])} — {esc(c["meaning"])}</li>' for c in combo_hits) or "<li>No widely known combinations inside this number.</li>"
        sl = [s for s in SLANG if s["code"] == n]
        slang_html = ("<ul>" + "".join(f'<li><strong>{esc(s["lang"])}:</strong> {esc(s["meaning"])}. <span class="muted">{esc(s["note"])}</span></li>' for s in sl) + "</ul>") if sl else '<p>This exact number isn\'t a common slang code. See the <a href="~/slang.html">slang dictionary</a> for the codes people use.</p>'
        facts = "".join(f'<li><span>{k}</span><b>{esc(v)}</b></li>' for k, v in math_facts(n))
        rel = related(n)
        prev_n, next_n = order[i - 1] if i else None, order[i + 1] if i + 1 < len(order) else None
        sc = luck_score(n)
        body = f'''
<article class="wrap">
 <header class="page-head">
  <h1>{n}: {esc(d["tag"])}</h1>
  <p>{esc(d["lead"])}</p>
  <p class="hint">Updated {"October 15, 2026"} · Reviewed under our <a href="~/editorial-standards.html">editorial standards</a></p>
 </header>
 <div class="split">
  <div>
   <div class="panel">
    {keys(n)}
    <p class="eq">{" + ".join(n)} = {total}{(" → " + " → ".join(str(x) for x in steps[1:])) if len(steps) > 1 else ""} &nbsp;<strong>Root {root}</strong></p>
    <p class="mt0">Numerology root {root}: {esc(root_text(root))}.</p>
   </div>
   <div class="prose mt2">
    <h2>What {n} means</h2>
    {"".join(f"<p>{esc(p)}</p>" for p in d["body"])}
    <h2>{n} in Chinese and East Asian number culture</h2>
    <div class="table-wrap"><table class="table"><thead><tr><th>Digit</th><th>Character</th><th>Sounds like</th><th>Reputation</th></tr></thead><tbody>{zh_rows}</tbody></table></div>
    <h3>Combinations inside {n}</h3>
    <ul>{combos_html}</ul>
    <h2>{n} as internet slang</h2>
    {slang_html}
    <h2>Math facts about {n}</h2>
   </div>
   <ul class="facts">{facts}</ul>
   <div class="prose mt2">
    <h2>Is {n} a lucky number for a phone or plate?</h2>
    <p>Using Chinese homophone tradition and pattern memorability, {n} scores <strong>{sc}/100</strong> on our luck scale. <a href="~/decode.html?n={n}">Open {n} in the decoder</a> for the full breakdown and luckier variations.</p>
    <h2>Frequently asked questions</h2>
   </div>
   {faq_html(d["faq"])}
   <nav class="pager" aria-label="Previous and next numbers">
    {f'<a class="btn ghost small" href="~/number/{prev_n}/">Previous: {prev_n}</a>' if prev_n else '<span></span>'}
    {f'<a class="btn ghost small" href="~/number/{next_n}/">Next: {next_n}</a>' if next_n else '<span></span>'}
   </nav>
  </div>
  <aside class="stack sticky">
   <div class="panel"><h3>Decode another number</h3>{decode_form()}</div>
   <div class="panel"><h3>Related numbers</h3>{chips(rel) if rel else "<p>See the <a href='~/numbers.html'>full index</a>.</p>"}</div>
   <div class="panel gold"><h3>Want {n} in your phone number?</h3><p>We help businesses find lucky and vanity numbers and numeric domains.</p><a class="btn" href="~/lucky-numbers.html?need=phone&amp;digits={n}">Ask about {n}</a></div>
  </aside>
 </div>
</article>'''
        layout(f"number/{n}/index.html", f"{n} meaning: {d['tag']} — angel, Chinese, slang & math | 55596",
               f"What does {n} mean? {d['lead']} Numerology root {root}, Chinese reading, slang and math facts.",
               body, crumbs=[("Numbers", "numbers.html"), (n, None)],
               schema=[faq_schema(d["faq"]), {"@context": "https://schema.org", "@type": "Article", "headline": f"{n}: {d['tag']}", "datePublished": "2026-10-15", "dateModified": "2026-10-15", "author": {"@type": "Organization", "name": "55596 Editorial"}, "publisher": {"@type": "Organization", "name": "55596"}}],
               og_type="article")

def numbers_index():
    groups = [("Single digits", [n for n in NUMBER_ORDER if len(n) == 1]),
              ("Two-digit numbers", [n for n in NUMBER_ORDER if len(n) == 2]),
              ("Three-digit numbers", [n for n in NUMBER_ORDER if len(n) == 3]),
              ("Four digits and more", [n for n in NUMBER_ORDER if len(n) >= 4])]
    body = '<section class="wrap page-head"><h1>Number index</h1><p>Every number with a full written guide. For any other number, use the <a href="~/decode.html">decoder</a> — it works on numbers up to 15 digits.</p>' + decode_form() + "</section>"
    for t, ns in groups:
        body += f'<section class="wrap section"><h2>{t}</h2>{numgrid(ns)}</section>'
    body += '<section class="wrap">' + lead_cta() + "</section>"
    layout("numbers.html", "Number meanings index — every number guide | 55596", "Browse guides to the most meaningful numbers: 0–9, master numbers, angel numbers 111–999, Chinese lucky numbers 168, 520, 1314, 8888 and slang codes.", body, crumbs=[("Numbers", None)])

def angel_hub():
    reps = ["111","222","333","444","555","666","777","888","999","1010","1111","1212"]
    rows = "".join(f'<tr><td><a href="~/number/{n}/">{n}</a></td><td>{esc(NUMBERS[n]["tag"])}</td></tr>' for n in reps)
    faq = [["Are angel numbers real?", "Angel numbers are a modern spiritual practice, not a scientific claim. Many people use them as prompts for reflection. We present them as tradition and entertainment."],
           ["Why do I keep seeing the same number?", "Clocks, receipts and plates show repeating digits often, and our brains are wired to notice patterns (the frequency illusion). Whether you read meaning into it is personal."],
           ["How do I read a number that isn't repeating?", "Look for the digit that appears most, then read the others as supporting themes. The decoder does this automatically."]]
    body = f'''<section class="wrap page-head"><h1>Angel numbers</h1><p>Repeating numbers like 111, 555 and 1111 are read in modern spirituality as small prompts to pay attention. Here's what each pattern is said to mean, and how the same digits read in other cultures.</p>{decode_form()}</section>
<section class="wrap section"><div class="split"><div>
 <div class="table-wrap"><table class="table"><thead><tr><th>Number</th><th>Common reading</th></tr></thead><tbody>{rows}</tbody></table></div>
 <div class="prose mt2"><h2>The digits behind every angel number</h2>
 <ul>{"".join(f"<li><strong>{d}</strong> — {esc(DIGITS[d]['angel'])}</li>" for d in "0123456789")}</ul>
 <h2>A note on context</h2><p>Angel-number meanings are Western and spiritual. The same digits can mean the opposite elsewhere: 444 is 'protection' in angel-number guides but triple 'death' in East Asian homophone tradition; 666 is ominous in Christian tradition and high praise in Chinese gaming chat. If a number matters for business, check every reading.</p>
 <h2>Questions</h2></div>{faq_html(faq)}</div>
 <aside class="stack sticky"><div class="panel"><h3>Calculate your own number</h3><p>Your life path number is the numerology number most people start with.</p><a class="btn" href="~/tools/life-path-calculator.html">Life path calculator</a></div><div class="panel"><h3>Watch</h3>{video_card(VIDEOS[3])}</div></aside></div>
{lead_cta()}</section>'''
    layout("angel-numbers.html", "Angel numbers 111 to 1212 — meanings and patterns | 55596", "Angel number meanings for 111, 222, 333, 444, 555, 666, 777, 888, 999, 1111 and 1212, with how the same digits read in Chinese and other cultures.", body, crumbs=[("Angel numbers", None)], schema=faq_schema(faq), active="angel-numbers.html")

def numerology_hub():
    rows = "".join(f'<tr><td><a href="~/number/{d}/">{d}</a></td><td>{esc(DIGITS[d]["num"])}</td></tr>' for d in "123456789") + "".join(f'<tr><td><a href="~/number/{m}/">{m}</a></td><td>{esc(MASTER[m])}</td></tr>' for m in MASTER)
    py = "".join(f"<td>{chr(97+i).upper()}</td>" for i in range(26))
    faq = [["Pythagorean or Chaldean — which is right?", "They're different traditions. Pythagorean assigns 1–9 in alphabet order and is most common in the West; Chaldean uses 1–8 based on sound and is older. Our name calculator offers both."],
           ["Why are 11, 22 and 33 not reduced?", "Numerologists treat them as 'master numbers' with an intensified meaning, so they're kept when they appear as a total."],
           ["Is numerology scientific?", "No. It's a symbolic tradition. People use it for reflection and fun; treat it as you would a horoscope."]]
    body = f'''<section class="wrap page-head"><h1>Numerology</h1><p>Numerology reduces dates and names to single digits and reads each digit as a personality theme. It's symbolic, not scientific — and a lot of fun when you know how the calculation works.</p></section>
<section class="wrap section"><div class="split"><div class="prose">
 <h2>The core numbers</h2>
 <ul><li><strong>Life path</strong> — from your full date of birth. <a href="~/tools/life-path-calculator.html">Calculate</a></li>
 <li><strong>Expression (destiny)</strong> — from every letter of your full birth name. <a href="~/tools/name-number-calculator.html">Calculate</a></li>
 <li><strong>Soul urge</strong> — vowels only; your inner motivation.</li>
 <li><strong>Personality</strong> — consonants only; how others see you.</li>
 <li><strong>Personal year</strong> — your birth month and day plus the current year. <a href="~/tools/personal-year-calculator.html">Calculate</a></li></ul>
 <h2>What each number means</h2>
</div><aside class="panel sticky"><h3>Today's universal number</h3><div id="daily-number"></div></aside></div>
<div class="table-wrap"><table class="table"><thead><tr><th>Number</th><th>Theme</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="prose mt2"><h2>How a life path is calculated</h2><p>Take a birthday of 23 August 1990. Reduce each part separately: month 8 → 8; day 23 → 2+3 = 5; year 1990 → 1+9+9+0 = 19 → 1+9 = 10 → 1. Then add: 8 + 5 + 1 = 14 → 1+4 = 5. Life path 5 — change and freedom. Reducing each part first is the method most numerologists use, because it preserves master numbers that a single long sum can hide.</p>
<h2>Questions</h2></div>{faq_html(faq)}{lead_cta("Match your brand to your number", "Picking a business name, phone line or domain? We'll help you find numbers that fit your numerology and your customers' culture.")}</section>'''
    layout("numerology.html", "Numerology guide: life path, expression & master numbers | 55596", "Learn how numerology works: life path, expression, soul urge, personality and personal year numbers, master numbers 11, 22, 33, and free calculators.", body, crumbs=[("Numerology", None)], schema=faq_schema(faq), active="numerology.html")

def culture_hub():
    zh = "".join(f'<tr><td><a href="~/number/{d}/">{d}</a></td><td>{DIGITS[d]["zh"]["char"]} {DIGITS[d]["zh"]["py"]}</td><td>{esc(DIGITS[d]["zh"]["sounds"])}</td><td><span class="badge {DIGITS[d]["zh"]["status"]}">{DIGITS[d]["zh"]["status"]}</span></td></tr>' for d in "0123456789")
    combos = "".join(f'<tr><td>{"<a href=\"~/number/" + c["code"] + "/\">" + c["code"] + "</a>" if c["code"] in NUMBERS else c["code"]}</td><td>{esc(c["region"])}</td><td>{esc(c["reading"])}</td><td>{esc(c["meaning"])}</td><td><span class="badge {c["status"]}">{c["status"]}</span></td></tr>' for c in COMBOS)
    faq = [["What is the luckiest number in Chinese culture?", "8, because 八 (bā) sounds like 发 (fā), to prosper."],
           ["Which number should businesses avoid in East Asia?", "4, which sounds like 'death' in Mandarin, Cantonese, Japanese and Korean. 14 and 44 are worse."],
           ["Is 7 lucky everywhere?", "No. It's the West's favourite lucky number but has a mixed reputation in Chinese."]]
    body = f'''<section class="wrap page-head"><h1>Lucky numbers by culture</h1><p>Most lucky-number beliefs come from sound: a digit is lucky when its name sounds like a good word. This page collects the readings that matter most for gifts, prices, addresses, phone numbers and dates.</p></section>
<section class="wrap section"><h2>Chinese digits 0–9</h2><div class="table-wrap"><table class="table"><thead><tr><th>Digit</th><th>Character</th><th>Sounds like</th><th>Reputation</th></tr></thead><tbody>{zh}</tbody></table></div>
<div class="grid g3 mt3">
 <div class="panel"><h3>Japan</h3><p>4 (shi) sounds like death and 9 (ku) like suffering, so both are avoided in hospitals and gifts. Goroawase wordplay turns numbers into words: 39 = thank you, 4649 = yoroshiku.</p></div>
 <div class="panel"><h3>Korea</h3><p>4 (sa) shares the death sound; lifts often show 'F' instead of 4. Yet 1004 (cheon-sa) means 'angel', and 8282 (pal-i pal-i) means 'hurry'.</p></div>
 <div class="panel"><h3>Thailand</h3><p>5 is 'hâa', so 555 is laughter. 9 (gâo) sounds like 'step forward' and is considered lucky; plate auctions favour 9s.</p></div>
 <div class="panel"><h3>India and South Asia</h3><p>108 is sacred in Hindu and Buddhist practice. Many Muslims in the region use 786 as a numeric blessing. Numerology based on birth dates is widely used for names and business launches.</p></div>
 <div class="panel"><h3>The West</h3><p>7 is the favourite lucky number; 13 is avoided (many buildings skip floor 13). 666 has a dark biblical association. In Italy, 17 is the unlucky one.</p></div>
 <div class="panel"><h3>Arabic chat</h3><p>In Arabizi, digits stand for letters: 3 is ع and 7 is ح, so 7777 reads as laughter.</p></div>
</div>
<h2 class="mt3">Combinations and codes</h2><div class="table-wrap"><table class="table"><thead><tr><th>Number</th><th>Region</th><th>Reading</th><th>Meaning</th><th>Reputation</th></tr></thead><tbody>{combos}</tbody></table></div>
<div class="grid g2 mt3"><div>{video_card(VIDEOS[2])}</div><div class="prose"><h2>Why this matters in business</h2><p>Lucky numbers influence real prices. Property listings change house numbers to attract buyers, plate auctions pay premiums for 8s, and retailers set prices like 88, 168 and 888 while avoiding 4 and 250. If your customers include Chinese, Japanese or Korean speakers, check your phone number, address and price points with the <a href="~/decode.html">decoder</a>.</p></div></div>
<h2 class="mt3">Questions</h2>{faq_html(faq)}{lead_cta()}</section>'''
    layout("culture.html", "Lucky and unlucky numbers by culture — China, Japan, Korea, Thailand, India | 55596", "Chinese digits 0–9 and their homophones, Japanese and Korean number superstitions, Thai 555, Indian sacred numbers and the famous combinations 168, 520, 1314, 250.", body, crumbs=[("Culture", None)], schema=faq_schema(faq), active="culture.html")

def slang_page():
    langs = sorted(set(s["lang"] for s in SLANG))
    rows = "".join(f'<tr data-lang="{esc(s["lang"])}"><td><strong>{"<a href=\"~/number/" + s["code"] + "/\">" + s["code"] + "</a>" if s["code"] in NUMBERS else esc(s["code"])}</strong></td><td>{esc(s["lang"])}</td><td>{esc(s["reading"])}</td><td>{esc(s["meaning"])}</td><td class="muted">{esc(s["note"])}</td></tr>' for s in SLANG)
    body = f'''<section class="wrap page-head"><h1>Number slang dictionary</h1><p>How people write words with digits — from Thai laughter to Chinese love codes, Japanese wordplay, Korean shortcuts and Arabizi. Filter by language or search for a code.</p></section>
<section class="wrap section">
 <div class="form panel"><div class="row"><div><label for="slang-filter">Search</label><input id="slang-filter" type="search" placeholder="e.g. love, 520, laugh"></div><div><label for="slang-lang">Language</label><select id="slang-lang"><option value="">All languages</option>{"".join(f"<option>{esc(l)}</option>" for l in langs)}</select></div></div></div>
 <div class="table-wrap mt2"><table class="table" id="slang-table"><thead><tr><th>Code</th><th>Language</th><th>Reading</th><th>Meaning</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table></div>
 <div class="prose mt3"><h2>Why do people write words with numbers?</h2><p>Three reasons come up again and again. Speed: typing 555 is faster than ฮ่าฮ่าฮ่า. Missing letters: early phones had no Arabic keyboard, so 7 stood in for ح. Wordplay: in Chinese and Japanese, numbers sound like syllables, so 520 and 39 became affectionate shortcuts that also slip past filters and look playful. Read our <a href="~/guides/internet-number-slang.html">guide to number slang</a>.</p>
 <p>Know a code we're missing? <a href="~/contests.html">Submit it in our monthly contest</a> — the best entries win prizes.</p></div>
</section>'''
    layout("slang.html", "Number slang dictionary — 555, 520, 2333, 1004, 39, 7777 | 55596", "What numbers mean in internet slang: Thai 555 laughter, Chinese 520 and 1314, 2333, 88, Korean 1004 and 8282, Japanese 39 and 4649, Arabizi 7777.", body, crumbs=[("Slang", None)], active="slang.html",
           schema={"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Number slang dictionary", "hasDefinedTerm": [{"@type": "DefinedTerm", "name": s["code"], "description": f'{s["lang"]}: {s["meaning"]}'} for s in SLANG]})

TOOLS = [
 ("life-path-calculator", "Life path calculator", "Your core numerology number from your date of birth.", "life-path",
  '<div><label for="t-dob">Date of birth</label><input id="t-dob" type="date" name="dob" required></div>',
  "We reduce your birth month, day and year separately, then add them and reduce again, keeping master numbers 11, 22 and 33. This is the method most numerology books use.",
  [["What is a life path number?", "The numerology number derived from your full birth date, read as your central life theme."], ["Can my life path be 11?", "Yes. 11, 22 and 33 are master numbers and aren't reduced further."]]),
 ("name-number-calculator", "Name number calculator", "Expression, soul urge and personality numbers from a name.", "name-number",
  '<div><label for="t-name">Full name at birth</label><input id="t-name" name="name" required autocomplete="name"></div><div><label for="t-sys">System</label><select id="t-sys" name="system"><option value="pythagorean">Pythagorean</option><option value="chaldean">Chaldean</option></select></div>',
  "Each letter gets a value (Pythagorean: A=1 … I=9, J=1 …; Chaldean: by sound, 1–8). We total all letters for expression, vowels for soul urge and consonants for personality.",
  [["Should I use my nickname?", "Traditional numerology uses the full birth name; many people compare both."], ["Which system should I choose?", "Pythagorean is most common today; Chaldean is older. Try both."]]),
 ("personal-year-calculator", "Personal year calculator", "The numerology theme of any year for you.", "personal-year",
  '<div class="row"><div><label for="t-dob2">Date of birth</label><input id="t-dob2" type="date" name="dob" required></div><div><label for="t-year">Year</label><input id="t-year" type="number" name="year" min="1900" max="2200" value="2026"></div></div>',
  "Add your birth month and day digits to the digits of the chosen year, then reduce to 1–9. Personal years run in a nine-year cycle.",
  [["When does a personal year start?", "Most numerologists use 1 January; some start it on your birthday."]]),
 ("compatibility-calculator", "Numerology compatibility", "Compare two life path numbers.", "compatibility",
  '<div class="row"><div><label for="t-a">Your date of birth</label><input id="t-a" type="date" name="dob1" required></div><div><label for="t-b">Their date of birth</label><input id="t-b" type="date" name="dob2" required></div></div>',
  "We calculate both life paths and compare them using the classic numerology families 1-5-7, 2-4-8 and 3-6-9.",
  [["Does a 'growth pairing' mean we're incompatible?", "No — it's a symbolic reading that you balance each other through difference. Real relationships depend on people, not digits."]]),
 ("lucky-phone-number", "Lucky phone number score", "Score any phone number from 0 to 100.", "lucky-phone",
  '<div><label for="t-ph">Phone number</label><input id="t-ph" name="value" inputmode="tel" required placeholder="+1 555 0168"></div>',
  "We weight each digit by its Chinese homophone (8, 6, 9 up; 4 down), reward lucky endings and memorable runs or sequences, and penalise unlucky pairs like 14 and 250. The score is cultural tradition plus memorability, not a prediction.",
  [["Does a lucky number really help a business?", "Memorable numbers measurably help recall; in Chinese-speaking markets, lucky digits also carry real price premiums and customer goodwill."], ["Is my number stored?", "No. The calculation runs in your browser."]]),
 ("lucky-plate-number", "Lucky licence plate checker", "Score a plate, letters and digits included.", "lucky-plate",
  '<div><label for="t-pl">Plate</label><input id="t-pl" name="value" required placeholder="e.g. 8KL 168"></div>',
  "Letters are converted with the Pythagorean table (A=1 … I=9), then the full sequence is scored like a phone number.",
  [["Why do 8s cost more at plate auctions?", "Because 8 sounds like 'prosper' in Chinese; plates such as '8' and '88' have sold for millions in Hong Kong."]]),
 ("lucky-address-number", "Lucky address checker", "House, unit and floor numbers through different cultural lenses.", "lucky-address",
  '<div><label for="t-ad">House or unit number</label><input id="t-ad" name="value" required placeholder="e.g. 1608"></div>',
  "We score the digits, flag 4s and 14s that some buyers avoid, and show the numerology root of the address.",
  [["Can I change my house number?", "Sometimes, through your local council or municipality. Rules vary; ask before you rely on it."]]),
 ("business-name-number", "Business name number", "The numerology number of a brand or company name.", "business-name",
  '<div><label for="t-bn">Business name</label><input id="t-bn" name="name" required></div><div><label for="t-sys2">System</label><select id="t-sys2" name="system"><option value="pythagorean">Pythagorean</option><option value="chaldean">Chaldean</option></select></div>',
  "We total the letters of the name and reduce to a root, keeping master numbers. Many naming consultants favour 1, 3, 8 or 9 for commercial brands.",
  [["Should I rename my company for numerology?", "Only if it fits your brand too. Numerology is one input among many."]]),
]

def tools_pages():
    tiles = "".join(f'<a class="tile" href="~/tools/{slug}.html"><h3>{esc(t)}</h3><p>{esc(d)}</p></a>' for slug, t, d, *_ in TOOLS)
    body = f'''<section class="wrap page-head"><h1>Number tools</h1><p>Free calculators for numerology and lucky numbers. Every calculation runs in your browser.</p></section>
<section class="wrap section"><div class="grid g3"><a class="tile" href="~/decode.html"><h3>Number decoder</h3><p>Every reading of any number up to 15 digits.</p></a>{tiles}</div>{lead_cta()}</section>'''
    layout("tools.html", "Free numerology and lucky number calculators | 55596", "Life path, name number, personal year, compatibility, lucky phone, plate, address and business name calculators — free and private.", body, crumbs=[("Tools", None)], active="tools.html")
    for slug, title, desc, tool, fields, how, faq in TOOLS:
        others = "".join(f'<li><a href="~/tools/{s}.html">{esc(t)}</a></li>' for s, t, *_ in TOOLS if s != slug)
        body = f'''<section class="wrap page-head"><h1>{esc(title)}</h1><p>{esc(desc)} Free, instant and private.</p></section>
<section class="wrap"><div class="split"><div>
 <form class="form panel" data-tool="{tool}">{fields}<div><button class="btn" type="submit">Calculate</button></div></form>
 <div data-out class="result" aria-live="polite"></div>
 <div class="prose mt2"><h2>How it works</h2><p>{esc(how)}</p><p class="muted">Results reflect numerology and cultural tradition. They're for reflection and entertainment, not financial, legal or life advice.</p><h2>Questions</h2></div>
 {faq_html(faq)}
</div><aside class="stack sticky"><div class="panel"><h3>More tools</h3><ul>{others}</ul></div><div class="panel gold"><h3>Need a better number?</h3><p>We source lucky phone numbers, plates-style numbers and numeric domains.</p><a class="btn" href="~/lucky-numbers.html">Request one</a></div></aside></div></section>'''
        layout(f"tools/{slug}.html", f"{title} — free & private | 55596", f"{desc} {how[:110]}", body, crumbs=[("Tools", "tools.html"), (title, None)],
               schema=[faq_schema(faq), {"@context": "https://schema.org", "@type": "WebApplication", "name": title, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}])

def lucky_numbers():
    needs = [("phone", "Phone number", "Local, mobile or toll-free"), ("domain", "Numeric domain", ".com and other extensions"),
             ("plate", "Plate-style number", "Guidance for auctions"), ("address", "Address / unit advice", "Property and retail"),
             ("brand", "Brand & price numbers", "Prices, launch dates, SKUs"), ("sell", "Sell or value mine", "Free valuation")]
    choice = "".join(f'<label><input type="radio" name="need" value="{v}" required><span>{esc(t)}</span><small>{esc(s)}</small></label>' for v, t, s in needs)
    faq = [["How much does a lucky number cost?", "It depends on the market, the pattern and the area code. Simple patterns can cost under US$100; premium 8-heavy or repeating numbers in major cities can run into the thousands. We quote options at different budgets."],
           ["Do you sell phone service?", "No. We help you find and acquire the number; it's then activated with a licensed carrier or VoIP provider of your choice."],
           ["Which markets do you cover?", "North America, the UK, India, Southeast Asia, Australia and Chinese-speaking markets, plus numeric domain names worldwide."],
           ["What happens after I submit?", "We review your brief within two business days and reply with available options, prices and next steps. There's no obligation."]]
    body = f'''<section class="hero"><div class="wrap hero-grid">
 <div><h1>Get a number people remember — and want</h1>
 <p class="lede">Lucky and vanity numbers get remembered, dialled and trusted. Tell us what you need and we'll come back with real, available options at your budget.</p>
 <ul class="stack"><li><strong>Phone numbers</strong> with 8s, 168, 518, repeating runs or words.</li><li><strong>Numeric domains</strong> — short, pronounceable, cross-cultural.</li><li><strong>Brand numbers</strong> — prices, launch dates and addresses that work in every market.</li><li><strong>Free valuation</strong> of a number or numeric domain you already own.</li></ul>
 <p class="hint">Reply within 2 business days · No obligation · Your details stay private</p></div>
 <div>
 <form class="form panel" data-form="lucky-number-lead" data-subject="Lucky number request" novalidate>
  <ol class="steps"><li>1. What you need</li><li>2. Preferences</li><li>3. Contact</li></ol>
  <fieldset data-step="1"><legend class="skip">What do you need?</legend><div class="choice">{choice}</div><div class="mt1"><button class="btn" type="button" data-next>Continue</button></div></fieldset>
  <fieldset data-step="2"><legend class="skip">Preferences</legend>
   {form_field("digits", "Digits or pattern you want", req=False, ph="e.g. ends in 888, contains 168, 55596")}
   <div class="row">{form_field("Country / market", "Country or market", "select", opts=["United States","Canada","United Kingdom","India","China / Hong Kong / Taiwan","Singapore / Malaysia","Thailand","Australia","UAE / Middle East","Worldwide / domain","Other"])}{form_field("Area code / city", "Area code or city", req=False)}</div>
   <div class="row">{form_field("Budget", "Budget", "select", opts=["Under US$100","US$100–500","US$500–2,000","US$2,000–10,000","US$10,000+","Not sure yet"])}{form_field("Timeline", "When do you need it?", "select", opts=["This week","This month","Within 3 months","Just exploring"])}</div>
   {form_field("Details", "Anything else?", "textarea", req=False, ph="Industry, language of your customers, numbers to avoid, a domain you'd like valued…")}
   <div class="mt1"><button class="btn ghost" type="button" data-back>Back</button> <button class="btn" type="button" data-next>Continue</button></div></fieldset>
  <fieldset data-step="3"><legend class="skip">Contact</legend>
   <div class="row">{form_field("Name", "Your name", auto="name")}{form_field("Email", "Email", "email", auto="email")}</div>
   <div class="row">{form_field("Company", "Company", req=False, auto="organization")}{form_field("Phone", "Phone (optional)", "tel", req=False, auto="tel")}</div>
   {consent_box()}
   <p class="form-status" role="status" aria-live="polite"></p>
   <div><button class="btn ghost" type="button" data-back>Back</button> <button class="btn gold" type="submit">Send my request</button></div></fieldset>
 </form></div>
</div></section>
<section class="section alt"><div class="wrap grid g3">
 <div><h2>Why it pays</h2><p>Memorable numbers lift recall in ads, on vans and on the radio. In Chinese-speaking markets, numbers with 8s and 168 endings carry price premiums — airlines and retailers have paid six figures for 8888 patterns.</p></div>
 <div><h2>How it works</h2><ol><li>Tell us your market, pattern and budget.</li><li>We search carrier inventories, marketplaces and private owners.</li><li>You pick a number; we guide the transfer or purchase.</li></ol></div>
 <div><h2>Not sure what's lucky?</h2><p>Score your current number first with the <a href="~/tools/lucky-phone-number.html">lucky phone tool</a>, or decode a pattern in the <a href="~/decode.html">decoder</a>.</p></div>
</div></section>
<section class="section"><div class="wrap grid g2">
 <div><h2>Notify me when a pattern is available</h2><p>Waiting for an all-8s ending, a 168 in your area code or a specific numeric domain? We'll alert you once.</p>
 {simple_form("notify-me", "Pattern availability alert", [form_field("Pattern", "Pattern or number", ph="e.g. xxx-888-8888 or 5-digit .com"), form_field("Market", "Country / area code"), form_field("Email", "Email", "email", auto="email")], "Alert me")}</div>
 <div><h2>Free valuation</h2><p>Own a memorable phone number or a numeric domain? Get a no-cost estimate and, if you want, help selling it.</p>
 {simple_form("valuation", "Valuation request", [form_field("Asset", "Number or domain"), form_field("Type", "Type", "select", opts=["Phone number","Numeric domain","Other"]), form_field("Name", "Your name", auto="name"), form_field("Email", "Email", "email", auto="email")], "Get my valuation")}</div>
</div>
<div class="wrap mt3"><h2>Questions</h2>{faq_html(faq)}</div></section>'''
    layout("lucky-numbers.html", "Lucky & vanity phone numbers, numeric domains and valuations | 55596", "Request a lucky or vanity phone number, numeric domain or brand number for your market — with 8s, 168, 518 or repeating patterns. Free valuation of numbers you own.", body, crumbs=[("Lucky numbers", None)], schema=faq_schema(faq))

def support():
    tiers = [("5", "Coffee", ["Keeps the servers and tools free"]), ("25", "Supporter", ["Funds one new number guide", "Name on the supporters page (optional)"]),
             ("100", "Patron", ["Funds a translation into a new language", "Early access to new tools"]), ("500", "Sponsor a number", ["Your brand on one number page for 12 months", "Clearly labelled as a sponsor"])]
    cards = "".join(f'<div class="panel tier"><h3 class="mt0">{t}</h3><span class="amt">${a}</span><ul>{"".join(f"<li>{esc(x)}</li>" for x in b)}</ul><a class="btn{" gold" if a == "100" else ""}" href="#pledge" data-amount="{a}" onclick="var i=document.querySelector(\'[name=&quot;Amount (USD)&quot;]\');if(i)i.value=\'{a}\'">Choose ${a}</a></div>' for a, t, b in tiers)
    body = f'''<section class="wrap page-head"><h1>Support 55596</h1><p>55596 is independent. Ads cover hosting; your support pays for everything that makes it better — and every contribution is earmarked.</p></section>
<section class="wrap section"><div class="grid g4">{cards}</div>
<div class="grid g3 mt3">
 <div class="panel"><h3>Operations</h3><p>Hosting, tools, data checking, and accessibility work.</p></div>
 <div class="panel"><h3>Promotion &amp; marketing</h3><p>Getting accurate number culture in front of people who'd otherwise only find spam.</p></div>
 <div class="panel"><h3>Hiring talent</h3><p>Native-speaker writers and translators for Chinese, Japanese, Korean, Thai, Hindi and Arabic content.</p></div>
 <div class="panel"><h3>Contests &amp; prizes</h3><p>Monthly prizes for the best number stories, slang finds and designs.</p></div>
 <div class="panel"><h3>New tools</h3><p>Next up: date-picker for lucky wedding days and a bulk phone-number scorer for businesses.</p></div>
 <div class="panel"><h3>Transparency</h3><p>We publish a yearly summary of how support was spent.</p></div>
</div>
<div class="split mt3" id="pledge"><div>
 <h2>Make a pledge</h2><p>Tell us the amount and purpose. We'll reply with a secure payment link for card, PayPal or bank transfer — we never ask for card details by email or form.</p>
 {simple_form("donation-pledge", "Donation pledge", [
   '<div class="row">' + form_field("Amount (USD)", "Amount (USD)", "number", ph="25") + form_field("Frequency", "Frequency", "select", opts=["One-time","Monthly","Yearly"]) + '</div>',
   form_field("Purpose", "Earmark for", "select", opts=["Where it's needed most","Operations","Promotion & marketing","Hiring talent","Contests & prizes","New tools","Sponsor a number"]),
   '<div class="row">' + form_field("Name", "Your name", auto="name") + form_field("Email", "Email", "email", auto="email") + '</div>',
   form_field("Public credit", "Show my name on the supporters list?", "select", opts=["Yes","No, keep it anonymous"]),
   form_field("Message", "Message (optional)", "textarea", req=False)], "Send my pledge", "Contributions to 55596 are not tax-deductible.")}
</div><aside class="panel sticky"><h3>Corporate sponsorship</h3><p>Brands can sponsor a section, a tool or a contest prize pool.</p><a class="btn" href="~/advertise.html">See sponsor packages</a></aside></div></section>'''
    layout("support.html", "Support 55596 — donate, pledge or sponsor a number", "Support independent number culture: one-time or monthly pledges earmarked for operations, marketing, hiring writers, contests and prizes, or sponsor a number page.", body, crumbs=[("Support", None)])

def contests():
    body = f'''<section class="wrap page-head"><h1>Contests &amp; prizes</h1><p>A new prompt every month, with prizes for the best entries. Free to enter.</p></section>
<section class="wrap section"><div class="grid g3">
 <div class="panel"><h3>Number story of the month</h3><p>Tell us about a number that changed something for you — a lucky plate, a wedding date, a phone number with a story. 300 words max.</p><p><strong>Prize:</strong> US$100 gift card + feature on 55596.</p></div>
 <div class="panel"><h3>Slang hunter</h3><p>Find a number code from your language we haven't listed. Include how it's read and an example.</p><p><strong>Prize:</strong> US$50 gift card per accepted entry (up to 5 a month) + credit in the dictionary.</p></div>
 <div class="panel"><h3>Design the keypad</h3><p>Design a poster or wallpaper around a meaningful number. Original work only.</p><p><strong>Prize:</strong> US$150 + your design printed for our next campaign.</p></div>
</div>
<div class="split mt3"><div>
 <h2>Enter now</h2>
 {simple_form("contest-entry", "Contest entry", [
   form_field("Contest", "Which contest?", "select", opts=["Number story of the month","Slang hunter","Design the keypad"]),
   '<div class="row">' + form_field("Name", "Your name", auto="name") + form_field("Email", "Email", "email", auto="email") + '</div>',
   form_field("Country", "Country", req=False),
   form_field("Entry", "Your entry", "textarea", ph="Your story or slang code. For designs, paste a link to the image (Drive, Dropbox, Behance…)."),
   '<label class="check"><input type="checkbox" name="Original work" value="Yes" required><span>This is my original work and I am 18+ (or have a parent&#39;s permission).</span></label>'], "Submit my entry")}
</div><aside class="prose"><h2>Rules</h2><ul><li>Entries close on the last day of each month at 23:59 UTC.</li><li>Winners are chosen by the 55596 editorial team for originality, accuracy and clarity, and announced within 14 days.</li><li>No purchase necessary. Void where prohibited.</li><li>By entering you allow 55596 to publish your entry with credit. You keep your copyright.</li><li>One entry per person per contest each month.</li><li>Prizes are paid as digital gift cards or bank transfer and can't be exchanged.</li></ul>
<p>Want to fund a prize pool? <a href="~/advertise.html">Sponsor a contest</a>.</p></aside></div></section>'''
    layout("contests.html", "Monthly contests and prizes — number stories, slang, design | 55596", "Enter free monthly contests: number story of the month, slang hunter and keypad design. Cash and gift-card prizes, clear rules.", body, crumbs=[("Contests", None)])

def careers():
    roles = [("Native-speaker contributor (Chinese, Japanese, Korean, Thai, Hindi, Arabic)", "Freelance · Remote", "Write and fact-check number culture from your own language."),
             ("SEO & content editor", "Part-time · Remote", "Plan, edit and publish guides that answer real questions better than anyone else."),
             ("Front-end developer (static sites, vanilla JS)", "Contract · Remote", "Build new tools on our in-browser number engine."),
             ("Partnerships & sales (telecom, domains)", "Commission · Remote", "Bring in carriers, number brokers and registrars as partners."),
             ("Video creator", "Freelance · Remote", "Short explainers on number culture for YouTube and Shorts.")]
    body = f'''<section class="wrap page-head"><h1>Careers at 55596</h1><p>We're a small, remote team building the best reference for what numbers mean. We hire people who know their culture's traditions first-hand.</p></section>
<section class="wrap section"><div class="grid g2">{"".join(f'<div class="panel"><h3>{esc(t)}</h3><p class="muted">{esc(k)}</p><p>{esc(d)}</p></div>' for t, k, d in roles)}</div>
<div class="split mt3"><div><h2>Apply</h2>{simple_form("job-application", "Job application", [
  form_field("Role", "Role", "select", opts=[r[0] for r in roles] + ["Something else"]),
  '<div class="row">' + form_field("Name", "Your name", auto="name") + form_field("Email", "Email", "email", auto="email") + '</div>',
  '<div class="row">' + form_field("Languages", "Languages you speak", req=False) + form_field("Portfolio", "Portfolio or LinkedIn link", "url", req=False, ph="https://") + '</div>',
  form_field("Why you", "Tell us about yourself", "textarea")], "Send application")}</div>
<aside class="prose"><h2>How we hire</h2><ol><li>Send your application.</li><li>A short paid test task for shortlisted candidates.</li><li>A video call, then an offer.</li></ol><p>We welcome applicants from every country and background.</p></aside></div></section>'''
    layout("careers.html", "Careers — writers, editors, developers, partnerships | 55596", "Join 55596: native-speaker writers, SEO editors, front-end developers, partnerships and video creators. Remote roles.", body, crumbs=[("Careers", None)])

def advertise():
    packs = [("Sponsor a number page", "From US$500 / year", "Your brand on a high-intent number page, clearly labelled as sponsored."),
             ("Tool sponsorship", "From US$1,000 / quarter", "'Presented by' credit on a calculator such as the lucky phone score."),
             ("Newsletter feature", "From US$250 / issue", "One clearly marked sponsor slot in the number-of-the-week email."),
             ("Contest prize pool", "From US$300 / month", "Fund a monthly prize and get named credit on the contest page."),
             ("Lead partnership", "Revenue share", "Carriers, number brokers and registrars: receive qualified lucky-number leads."),
             ("Domain & site acquisition", "Make an offer", "Interested in 55596.com itself? Talk to us.")]
    body = f'''<section class="wrap page-head"><h1>Advertise, sponsor or partner</h1><p>Reach people who care about numbers: business owners picking phone lines, couples choosing dates, investors in numeric domains and readers across Asia, the Americas and Europe.</p></section>
<section class="wrap section"><div class="grid g3">{"".join(f'<div class="panel"><h3>{esc(t)}</h3><p><strong>{esc(p)}</strong></p><p>{esc(d)}</p></div>' for t, p, d in packs)}</div>
<div class="split mt3"><div><h2>Send an inquiry</h2>{simple_form("advertising-inquiry", "Advertising / partnership inquiry", [
  form_field("Interest", "I'm interested in", "select", opts=[p[0] for p in packs] + ["Something else"]),
  '<div class="row">' + form_field("Name", "Your name", auto="name") + form_field("Email", "Email", "email", auto="email") + '</div>',
  '<div class="row">' + form_field("Company", "Company", auto="organization") + form_field("Website", "Website", "url", req=False, ph="https://") + '</div>',
  form_field("Budget", "Budget", "select", req=False, opts=["Under US$500","US$500–2,000","US$2,000–10,000","US$10,000+"]),
  form_field("Message", "Message", "textarea")], "Send inquiry")}</div>
<aside class="prose"><h2>Our rules</h2><ul><li>Sponsored content is always labelled.</li><li>We don't accept ads for gambling, adult content, predatory loans or 'guaranteed luck' products.</li><li>Sponsors never edit our editorial readings.</li></ul><p>For the domain itself and broader partnerships you can also use <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p></aside></div></section>'''
    layout("advertise.html", "Advertise and partner with 55596", "Sponsor a number page or tool, feature in the newsletter, fund a contest, partner on lucky-number leads, or inquire about acquiring 55596.com.", body, crumbs=[("Advertise", None)])

def videos():
    groups = [("555 phone numbers", "555"), ("Lucky numbers and culture", "culture"), ("Numerology", "numerology"), ("Number facts", "math")]
    body = '<section class="wrap page-head"><h1>Videos</h1><p>The best explainers we have found, chosen for accuracy and clarity. Videos load from YouTube only when you press play.</p></section>'
    for t, k in groups:
        vs = [v for v in VIDEOS if v["topic"] == k]
        body += f'<section class="wrap section"><h2>{t}</h2><div class="grid g3">{"".join(video_card(v) for v in vs)}</div></section>'
    body += '<section class="wrap"><p class="muted">Videos are embedded from YouTube and belong to their creators. Creators: <a href="~/contact.html">suggest a video</a>.</p></section>'
    layout("videos.html", "Videos about numbers — 555 phone numbers, lucky numbers, numerology | 55596", "Watch explainers on why films use 555 phone numbers, Chinese lucky numbers, numerology basics and famous numbers like Graham's number and perfect numbers.", body, crumbs=[("Videos", None)],
           schema=[{"@context": "https://schema.org", "@type": "VideoObject", "name": v["title"], "description": f'{v["title"]} by {v["channel"]}', "thumbnailUrl": f'https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg', "uploadDate": "2026-10-15", "embedUrl": f'https://www.youtube-nocookie.com/embed/{v["id"]}'} for v in VIDEOS])

def about():
    body = f'''<section class="wrap page-head"><h1>About 55596</h1></section>
<section class="wrap"><div class="split"><div class="prose">
<p>55596 started with a simple observation: the same five digits mean completely different things depending on who reads them. To a Thai reader, 555 is laughter. To a Chinese reader, it's crying. To someone who follows angel numbers, it's a sign of change. Add 9 (long-lasting) and 6 (smooth flow), and 55596 becomes a small lesson in how culture shapes numbers.</p>
<p>Most number-meaning sites cover one tradition, and many are thin pages written to rank rather than to inform. We wanted one place that shows every reading side by side — numerology, angel numbers, East Asian homophones, internet slang and plain mathematics — with clear explanations of how each is calculated.</p>
<h2>What we believe</h2>
<ul><li><strong>Context over hype.</strong> Meanings are traditions, not guarantees. We never promise luck, money or health.</li><li><strong>Show the working.</strong> Every calculator explains its method.</li><li><strong>Privacy by design.</strong> Dates of birth and phone numbers are processed in your browser.</li><li><strong>Native voices.</strong> We're hiring writers from the cultures we cover.</li></ul>
<h2>How we make money</h2><p>Display advertising through Google AdSense, sponsorships that are always labelled, and helping businesses source lucky or memorable numbers. None of these influence our readings. See our <a href="~/affiliate-disclosure.html">advertising disclosure</a>.</p>
</div><aside class="panel sticky">{keys("55596", "sm")}<p class="mt1">Questions, corrections or partnership ideas?</p><a class="btn" href="~/contact.html">Contact us</a></aside></div></section>'''
    layout("about.html", "About 55596 — decode any number", "Why 55596 exists: one place for every reading of a number — numerology, angel numbers, cultural lucky numbers, slang and math — with transparent methods.", body, crumbs=[("About", None)])

def contact():
    body = f'''<section class="wrap page-head"><h1>Contact</h1><p>Questions, corrections, partnerships or press — send a message and we'll reply within two business days.</p></section>
<section class="wrap"><div class="split"><div>{simple_form("contact", "Contact form", [
  form_field("Topic", "Topic", "select", opts=["General question","Correction to a number page","Lucky number request","Advertising / sponsorship","Partnership","Interested in buying this domain/website","Press","Other"]),
  '<div class="row">' + form_field("Name", "Your name", auto="name") + form_field("Email", "Email", "email", auto="email") + '</div>',
  form_field("Message", "Message", "textarea")], "Send message")}</div>
<aside class="stack"><div class="panel"><h3>Domain, sponsorship or partnership</h3><p>Interested in this website, the 55596.com domain, sponsorship, advertising or partnership?</p><a class="btn" href="https://web.works/contact" target="_blank" rel="noopener">Contact via web.works</a></div>
<div class="panel"><h3>Faster answers</h3><ul><li><a href="~/lucky-numbers.html">Request a lucky number</a></li><li><a href="~/advertise.html">Advertising packages</a></li><li><a href="~/careers.html">Apply for a role</a></li></ul></div></aside></div></section>'''
    layout("contact.html", "Contact 55596", "Contact the 55596 team for questions, corrections, lucky number requests, advertising, partnerships or press.", body, crumbs=[("Contact", None)])

def thank_you():
    body = '''<section class="wrap page-head" data-thanks><h1>Thank you — we've got it</h1><p>Your message has been sent. We reply within two business days. While you wait, decode a number or try a calculator.</p><p><a class="btn" href="~/decode.html">Open the decoder</a> <a class="btn ghost" href="~/tools.html">Browse tools</a></p></section>'''
    layout("thank-you.html", "Thank you | 55596", "Your message has been sent.", body, robots="noindex,follow")

def not_found():
    body = f'''<section class="wrap page-head">{keys("404")}<h1 class="mt2">404 — this page isn't here</h1><p>Fittingly, 404 is also internet slang for 'clueless'. The page may have moved. Try the decoder or the number index.</p>{decode_form()}<p><a href="~/index.html">Go to the home page</a> · <a href="~/numbers.html">Number index</a></p></section>'''
    # 404 must use absolute root paths on GitHub Pages because it is served at any depth
    layout("404.html", "Page not found | 55596", "This page doesn't exist.", body, robots="noindex,follow")

LEGAL = {
 "privacy": ("Privacy policy", "How 55596 handles personal data, cookies, advertising and forms.", """
<p><em>Last updated: October 15, 2026</em></p>
<h2>Who we are</h2><p>55596.com ("55596", "we") is an independent publication. You can reach us through our <a href="~/contact.html">contact form</a>.</p>
<h2>What we collect</h2><ul><li><strong>Calculator inputs</strong> (dates of birth, names, phone numbers, plates, addresses) are processed in your browser and are not sent to us.</li><li><strong>Form submissions</strong> (name, email and the details you enter) are delivered to us by FormSubmit, a form-forwarding service, so we can reply.</li><li><strong>Usage data</strong> collected by Google and our hosting provider (GitHub Pages), such as IP address, browser and pages viewed.</li></ul>
<h2>Advertising</h2><p>We use Google AdSense. Google and its partners use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>. Learn more in <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses data from partner sites</a>.</p>
<h2>Cookies and storage</h2><p>We store your theme and cookie choice in your browser's local storage. See our <a href="~/cookies.html">cookie policy</a>.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube in privacy-enhanced mode and only load after you press play.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under GDPR, UK GDPR, PIPEDA or CCPA/CPRA), you may request access to, correction of or deletion of personal data we hold, and object to processing. Use the <a href="~/contact.html">contact form</a>.</p>
<h2>Retention</h2><p>We keep form messages only as long as needed to respond and for our records, normally no longer than 24 months.</p>
<h2>Children</h2><p>55596 is not directed at children under 13, and we don't knowingly collect their data.</p>
<h2>Changes</h2><p>We'll post updates on this page with a new date.</p>"""),
 "terms": ("Terms of use", "The rules for using 55596.com.", """
<p><em>Last updated: October 15, 2026</em></p>
<h2>Using the site</h2><p>You may use 55596 for personal and business reference. Don't scrape the site at volumes that affect performance, or republish our content without permission.</p>
<h2>No advice</h2><p>Numerology, angel-number and cultural readings are traditions shared for education and entertainment. They are not financial, legal, medical or psychological advice, and we don't guarantee any outcome. See the <a href="~/disclaimer.html">disclaimer</a>.</p>
<h2>Lucky number requests</h2><p>Quotes we provide are estimates. Any purchase is a separate agreement with the seller, carrier or registrar. We don't provide telephone service.</p>
<h2>Contests</h2><p>Contests are governed by the rules on the <a href="~/contests.html">contests page</a>.</p>
<h2>Pledges and sponsorships</h2><p>Pledges are voluntary and not tax-deductible. Sponsorships are governed by the written terms we agree with each sponsor.</p>
<h2>User content</h2><p>When you submit content, you confirm it's yours and grant us a non-exclusive licence to publish it with credit.</p>
<h2>Liability</h2><p>The site is provided "as is". To the extent permitted by law, we aren't liable for losses arising from using it.</p>
<h2>Changes</h2><p>We may update these terms; continued use means you accept the updated terms.</p>"""),
 "cookies": ("Cookie policy", "Which cookies and storage 55596 uses.", """
<p><em>Last updated: October 15, 2026</em></p>
<h2>Essential storage</h2><p>Local storage remembers your light/dark theme and your cookie choice.</p>
<h2>Advertising cookies</h2><p>Google AdSense may set cookies to show and measure ads, including personalised ads where permitted. If you choose "Essential only", we request non-personalised ads. Visitors in the EEA, UK and Switzerland also see Google's consent message where required.</p>
<h2>Third parties</h2><p>Google Fonts serves our typefaces; YouTube sets cookies only after you start a video.</p>
<h2>Managing cookies</h2><p>Clear site data in your browser to reset your choice, or opt out at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>.</p>"""),
 "disclaimer": ("Disclaimer", "Meanings on 55596 are cultural and spiritual traditions, not predictions or advice.", """
<p>Number meanings on 55596 describe beliefs, traditions and wordplay from numerology, angel-number practice, Chinese and other East Asian homophone culture, religious traditions and internet slang. We present them for education and entertainment.</p>
<ul><li>No reading predicts the future or guarantees luck, wealth, health or relationships.</li><li>Luck scores reflect tradition and memorability only.</li><li>Cultural readings vary by dialect, region and person; we note differences where we can.</li><li>Nothing here is financial, legal, medical or psychological advice.</li><li>We may earn money from advertising, sponsorships and lucky-number services; see our <a href="~/affiliate-disclosure.html">advertising disclosure</a>.</li></ul>"""),
 "trademark-copyright": ("Trademark & copyright", "Trademark and copyright disclosure for 55596.com.", """
<h2>Trademark disclosure</h2><p>"55596" is used on this site as a descriptive numeric domain name. 55596.com is an independent publication and is <strong>not affiliated with, endorsed by or sponsored by</strong> any company, product, brand, telephone service, postal code, model number or trademark that contains the digits 555, 96 or 55596, including any products sold under "555" names (such as cigarettes, timer chips, watches or batteries) or any telephone numbering administrator. Any third-party names mentioned are used for identification and commentary only and remain the property of their owners.</p>
<p>Numbers themselves can't be owned. Cultural meanings, numerology methods and slang codes described here are traditional knowledge in the public domain; our descriptions of them are original writing.</p>
<h2>Copyright</h2><p>All original text, tools, code, design and graphics on 55596.com are © 2026 55596.com. You may quote short excerpts with a link back. Embedded videos are owned by their creators and shown via YouTube's embedding feature. Facts sourced from third parties are paraphrased and credited.</p>
<h2>Notices and takedown</h2><p>If you believe content on this site infringes your rights, send a notice through our <a href="~/contact.html">contact form</a> with the URL, the work you own, and your contact details. We review notices promptly and remove infringing material.</p>"""),
 "editorial-standards": ("Editorial standards", "How 55596 researches, writes and corrects number guides.", """
<ul><li><strong>Sourcing.</strong> Cultural claims are checked against encyclopaedic, academic or established language-learning sources; numerology methods follow widely published conventions.</li><li><strong>Framing.</strong> Beliefs are described as beliefs. We never claim a number will cause an outcome.</li><li><strong>Sensitive codes.</strong> Some number slang has crude or offensive readings; we describe these mildly or omit them.</li><li><strong>Original writing.</strong> We don't copy other sites. Quotes are short and attributed.</li><li><strong>Corrections.</strong> Spot an error? Use the <a href="~/contact.html">contact form</a>; we fix confirmed errors and update the page date.</li><li><strong>Independence.</strong> Advertisers and sponsors never edit readings.</li></ul>"""),
 "affiliate-disclosure": ("Advertising disclosure", "How 55596 earns money.", """
<p>55596 is funded by display ads (Google AdSense), labelled sponsorships, voluntary pledges, and fees from helping businesses source lucky or memorable numbers. If we ever add affiliate links, they'll be marked and listed here. Ads are placed automatically by Google and are separate from our content; we don't endorse advertised products.</p>"""),
}

def legal_pages():
    for slug, (t, d, html_) in LEGAL.items():
        body = f'<section class="wrap page-head"><h1>{esc(t)}</h1></section><section class="wrap"><div class="prose">{html_}</div></section>'
        layout(f"{slug}.html", f"{t} | 55596", d, body, crumbs=[(t, None)])

def static_files():
    write_raw("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    write_raw("ads.txt", f"google.com, {PUB.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    write_raw(".nojekyll", "")
    write_raw("site.webmanifest", '{"name":"55596 — Decode any number","short_name":"55596","start_url":"./index.html","display":"standalone","background_color":"#F5F7FB","theme_color":"#151936","icons":[{"src":"assets/img/favicon.svg","sizes":"any","type":"image/svg+xml"}]}\n')
    write_raw("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="4" y="6" width="56" height="52" rx="12" fill="#151936"/><rect x="4" y="50" width="56" height="8" rx="4" fill="#F2A900"/><text x="32" y="42" font-family="Arial Black,Arial,sans-serif" font-size="34" font-weight="900" text-anchor="middle" fill="#fff">5</text></svg>\n')

def build_all():
    home(); decode_page(); number_pages(); numbers_index(); angel_hub(); numerology_hub(); culture_hub(); slang_page()
    tools_pages(); lucky_numbers(); support(); contests(); careers(); advertise(); videos(); about(); contact(); thank_you(); not_found(); legal_pages(); static_files()
