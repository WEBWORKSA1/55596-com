# -*- coding: utf-8 -*-
from build import layout, esc, faq_html, faq_schema, video_card, lead_cta, keys, VIDEOS

V = {v["id"]: v for v in VIDEOS}

GUIDES = [
("555-around-the-world", "What 555 means around the world", "Laughter in Thailand, tears in China, change in angel numerology and fiction in Hollywood: one number, four meanings.",
 "kWx4epOcLd4", """
<p>Few numbers travel as far — or change meaning as completely — as 555. Type it to a friend in Bangkok and you've laughed. Type it to a friend in Shanghai and you might be crying. Show it to someone who follows angel numbers and they'll tell you change is coming. Show it to an American screenwriter and they'll see a phone number that doesn't ring anyone.</p>
<h2>Thailand: 555 is laughter</h2>
<p>The Thai word for five is ห้า, pronounced <em>hâa</em>. Say it three times and you have 'ha ha ha'. Typing three 5s is faster than spelling laughter in Thai script, so 555 became the Thai equivalent of LOL in the texting era and never left. The convention scales: 55 is a chuckle, 55555 is a proper laugh, and 555+ means you can't stop. Neighbouring Laos, whose word for five sounds almost the same, uses it too.</p>
<h2>China: 555 is crying</h2>
<p>In Mandarin, five is 五 (<em>wǔ</em>). Three of them sound like 呜呜呜 (<em>wū wū wū</em>), the sound of sobbing. On Chinese social media, 555 signals sadness or mock self-pity — 'I lost my keys again 555'. It's a perfect example of why number slang can't be translated by digits alone: the same string means the opposite thing on either side of a border.</p>
<h2>Japan: 555 means 'go, go, go'</h2>
<p>Japanese has several ways to read each digit. Five can be read <em>go</em>, so 555 becomes 'go-go-go' — a quick way to rally teammates in online games.</p>
<h2>Angel numbers: 555 means change</h2>
<p>In the modern angel-number tradition, which reads repeating digits as spiritual prompts, 5 stands for change, freedom and movement. Tripled, it becomes one of the most-searched angel numbers of all: readers interpret 555 as a sign that a significant transition is under way, in work, relationships or where you live. It's a belief system rather than a scientific claim, but it's a large one.</p>
<h2>North America: 555 is fiction</h2>
<p>Since the 1960s, film and TV producers in the US and Canada have used 555 phone numbers so that viewers don't call real people. Today only 555-0100 to 555-0199 are formally reserved for fiction; the wider 555 range was opened for assignment in the 1990s, though it was rarely used. Read <a href="~/guides/why-movies-use-555-phone-numbers.html">why movies use 555 numbers</a>.</p>
<h2>Numerology: 555 reduces to 6</h2>
<p>Add the digits — 5 + 5 + 5 = 15 — then 1 + 5 = 6. Numerology reads 6 as care, home and responsibility, which gives 555 an interesting twist: lots of change that ends in a settled place.</p>
<h2>So which meaning is right?</h2>
<p>All of them, depending on the reader. That's the whole idea behind 55596: before you put a number on a product, a price tag, a wedding invitation or a business card, check what it says in every language your audience speaks. <a href="~/decode.html?n=555">Decode 555</a> to see every layer at once.</p>
""", [["What does 555 mean in Thai?", "Hahaha — five is pronounced 'hâa'."], ["What does 555 mean in Chinese?", "Crying, from the sound 呜呜呜."], ["What does angel number 555 mean?", "In angel-number tradition, major change and freedom."]]),

("chinese-lucky-numbers-for-business", "Chinese lucky numbers for business: prices, phones and addresses", "How 8, 6, 9 and 168 can lift a brand in Chinese-speaking markets — and why 4 and 250 can sink a price tag.",
 "pT52hREAf18", """
<p>If you sell to customers who speak Mandarin or Cantonese — in China, Hong Kong, Taiwan, Singapore, Malaysia or the diaspora communities of Vancouver, Sydney and London — numbers are part of your branding whether you plan it or not. Here's a practical guide.</p>
<h2>The four digits that matter most</h2>
<ul><li><strong>8 (八, bā)</strong> sounds like 发 (fā), to prosper. It's the most valuable digit in phone numbers, plates and addresses.</li><li><strong>6 (六, liù)</strong> sounds like 流, smooth flow — 'business goes smoothly'.</li><li><strong>9 (九, jiǔ)</strong> sounds like 久, long-lasting — ideal for anniversaries and long-term relationships.</li><li><strong>4 (四, sì)</strong> sounds like 死, death. Avoid it wherever you can.</li></ul>
<h2>Prices</h2>
<p>Price points like 88, 168, 188, 288, 688 and 888 feel generous and auspicious. Avoid 4 in the last digit and avoid 250, which is slang for a fool. For gift and red-packet amounts, 520 (I love you) and 1314 (a lifetime) are popular for couples; 666 and 888 for business partners. Even amounts are preferred for gifts, with 4 the exception.</p>
<h2>Phone numbers</h2>
<p>A phone number ending in 8, 68, 88, 168 or 888 is an easy upgrade, and carriers in Chinese-speaking markets auction premium numbers for exactly that reason. Avoid 14 (sounds like 'want to die') and multiple 4s. Use our <a href="~/tools/lucky-phone-number.html">lucky phone number score</a> to check yours, then see <a href="~/guides/how-to-choose-a-lucky-business-phone-number.html">how to choose a lucky business phone number</a>.</p>
<h2>Addresses and floors</h2>
<p>Many buildings in East Asia skip the 4th, 14th and 24th floors. Estate agents serving Chinese buyers routinely note the address digits, and some homeowners have successfully applied to change a house number to remove a 4 before selling. If you're opening a store, a unit number with 8 or 6 is a small marketing gift.</p>
<h2>Dates</h2>
<p>Launches, signings and weddings cluster on dates with 6, 8 and 9 — the Beijing Olympics famously opened at 8:08 pm on 8 August 2008. May 20 (520) is an unofficial lovers' day and a big retail moment.</p>
<h2>Keep it respectful</h2>
<p>Not every Chinese customer cares about lucky numbers, and overdoing it can feel like a gimmick. Use lucky digits where a number has to exist anyway — a price, a phone line, an address — and avoid the clear negatives.</p>
""", [["What is the luckiest number for business in China?", "8, often in combinations such as 88, 168 or 888."], ["What prices should I avoid?", "Endings in 4, and 250."]]),

("how-to-calculate-life-path-number", "How to calculate your life path number (with examples)", "Step-by-step method, master numbers 11, 22 and 33, and the mistakes most online calculators make.",
 "I7KY9fdcuoQ", """
<p>Your life path number is the starting point of numerology. It comes from your full date of birth and is read as the central theme of your life. The maths is simple, but there's one detail many calculators get wrong.</p>
<h2>The method</h2>
<ol><li><strong>Reduce the month</strong> to a single digit (or master number). October = 10 → 1 + 0 = 1.</li><li><strong>Reduce the day.</strong> 29 → 2 + 9 = 11. Stop: 11 is a master number.</li><li><strong>Reduce the year.</strong> 1987 → 1 + 9 + 8 + 7 = 25 → 2 + 5 = 7.</li><li><strong>Add the three results</strong> and reduce: 1 + 11 + 7 = 19 → 1 + 9 = 10 → 1.</li></ol>
<p>Life path 1 — independence and leadership.</p>
<h2>Why reduce each part first?</h2>
<p>If you simply add every digit of the date in one go, you can hide master numbers. Reducing month, day and year separately is the convention used by most numerology authors, and it's what our <a href="~/tools/life-path-calculator.html">life path calculator</a> does.</p>
<h2>Master numbers</h2>
<p>When a total lands on 11, 22 or 33, numerologists keep it rather than reducing to 2, 4 or 6. They're described as intensified versions of their root: 11 the intuitive 'illuminator', 22 the 'master builder', 33 the 'master teacher'.</p>
<h2>What each life path means</h2>
<ul><li><a href="~/number/1/">1</a> leadership · <a href="~/number/2/">2</a> partnership · <a href="~/number/3/">3</a> expression · <a href="~/number/4/">4</a> structure · <a href="~/number/5/">5</a> freedom</li><li><a href="~/number/6/">6</a> care · <a href="~/number/7/">7</a> insight · <a href="~/number/8/">8</a> ambition · <a href="~/number/9/">9</a> compassion</li><li><a href="~/number/11/">11</a>, <a href="~/number/22/">22</a>, <a href="~/number/33/">33</a> master numbers</li></ul>
<h2>A healthy way to use it</h2>
<p>Numerology is symbolic. Many people find their life path a useful prompt for reflection — 'am I using my strengths?' — rather than a rule. Treat it like a horoscope: interesting, sometimes uncanny, never binding.</p>
""", [["Is the life path the same as a birthday number?", "No. The birthday number uses only the day of birth; the life path uses the full date."], ["What if I get 11?", "Keep it — 11 is a master number."]]),

("why-movies-use-555-phone-numbers", "Why movies use 555 phone numbers", "The story of the 555 exchange, the 555-0100 to 0199 fiction range, and what happened when films used real numbers.",
 "_LPw1hlMCaA", """
<p>Pay attention to phone numbers in American films and TV and you'll notice a pattern: 555, again and again. It isn't laziness. It's a long-standing industry convention to protect real people.</p>
<h2>The problem</h2>
<p>Whenever a real number appears on screen, someone calls it. Comic strips, songs and films have all caused floods of calls to unsuspecting households. One well-known case: a 2003 comedy showed a seven-digit number without an area code, and people across the US who had that number in their own area codes were bombarded with calls.</p>
<h2>The solution</h2>
<p>In the North American Numbering Plan, 555 was historically used for directory assistance (555-1212) and little else, which made it a safe 'exchange' for fiction. Phone companies encouraged studios to use it, and by the 1960s and 1970s it was standard. Older productions sometimes used the letter-style equivalent, 'KLondike 5', because the 5 key carries J, K and L.</p>
<h2>What's actually reserved today</h2>
<p>In the 1990s, the numbering administration opened most of the 555 range for real assignment, intended for information services. That idea never really took off. The range formally set aside for fiction today is <strong>555-0100 to 555-0199</strong>. Screenwriters who want to be completely safe use those.</p>
<h2>Other countries do it too</h2>
<p>The UK regulator reserves specific ranges for drama, and Australia and other countries have their own fictional ranges. The idea is universal; only the digits change.</p>
<h2>Fun fact: 555 is also laughter</h2>
<p>To a Thai viewer, a 555 number on screen reads as 'ha ha ha'. See <a href="~/guides/555-around-the-world.html">what 555 means around the world</a>.</p>
""", [["Are all 555 numbers fake?", "No. Only 555-0100 to 555-0199 are reserved for fiction; 555-1212 has long been directory assistance."], ["Can I call a 555 number?", "Most are unassigned; a call usually won't connect."]]),

("how-to-choose-a-lucky-business-phone-number", "How to choose a lucky (and memorable) business phone number", "A practical checklist: patterns that people remember, digits that sell in Asian markets, and how to get the number.",
 None, """
<p>A business phone number is a small asset that shows up everywhere — ads, vans, receipts, Google listings. A memorable or 'lucky' number costs little extra and keeps paying back in recall and goodwill.</p>
<h2>1. Start with memorability</h2>
<ul><li><strong>Repeats</strong>: xxx-888-8888, xxx-555-5555.</li><li><strong>Round numbers</strong>: endings like 0000 or 1000 are among the most valuable vanity patterns.</li><li><strong>Sequences</strong>: 1234, 6789.</li><li><strong>Words</strong>: vanity spellings using the letters on the keypad (5 = J K L).</li></ul>
<h2>2. Check cultural meaning</h2>
<p>If any of your customers speak Chinese, Japanese or Korean, avoid 4s and especially 14 and 44. Prefer endings in 8, 6 or 9 and combinations like 168 or 518. Our <a href="~/tools/lucky-phone-number.html">lucky phone score</a> checks this in a second.</p>
<h2>3. Match the area code to your market</h2>
<p>A local area code builds trust for local services; toll-free numbers suit national brands. In vanity markets, a prestigious area code can multiply a number's value.</p>
<h2>4. Make sure it's portable</h2>
<p>In most countries you can port a number between carriers, so buy a number you can keep even if you change providers. Confirm porting rules before you pay.</p>
<h2>5. Budget realistically</h2>
<p>Simple patterns can be inexpensive. Premium numbers in big cities, all-8 endings or famous patterns can cost thousands. Ask for several options at different price points.</p>
<h2>6. Put it everywhere — consistently</h2>
<p>Use the same number format across your website, Google Business Profile and printed material so customers and search engines connect it to you.</p>
<h2>Get help</h2>
<p>Tell us your market, preferred digits and budget and we'll come back with available numbers: <a href="~/lucky-numbers.html">request a lucky number</a>.</p>
""", [["Can I get a number with lots of 8s?", "Often yes, especially outside the busiest area codes. Premium patterns cost more."], ["Is a vanity number worth it?", "For brands that advertise their phone number, memorability usually pays for itself."]]),

("numeric-domain-names-explained", "Numeric domain names explained", "Why short number .com domains are valued, how buyers in Asia see them, and what to check before buying one.",
 None, """
<p>Numeric domains — names made only of digits, like 55596.com — are a niche but serious corner of the domain market. They're especially popular with buyers in China and across Asia, where digits are easier to type and remember than Latin-letter brand names.</p>
<h2>Why numbers make good domains</h2>
<ul><li><strong>Universal.</strong> Digits read the same in every script; no spelling or translation issues.</li><li><strong>Memorable when patterned.</strong> Repeats (888), sequences (123) and meaningful codes (520, 168) stick.</li><li><strong>Meaning.</strong> In Chinese, a numeric domain can 'say' something: 518 is 'I will prosper', 1314 is 'a lifetime'.</li><li><strong>Scarcity.</strong> Every three-digit .com and four-digit .com has long been registered, and short numeric .com domains trade as a recognisable asset class.</li></ul>
<h2>What drives value</h2>
<ol><li>Length — shorter is scarcer.</li><li>Extension — .com dominates.</li><li>Lucky digits (8, 6, 9) and no 4s for Chinese buyers.</li><li>Patterns — repeats, mirrors and meaningful codes.</li><li>Existing use — traffic and history.</li></ol>
<h2>Five-digit domains</h2>
<p>Five-digit .coms like 55596 sit in the middle of the market: far more of them exist than four-digit names, so value depends heavily on pattern and meaning. 55596 has a triple-5 run (memorable, and globally meaningful as Thai laughter and an angel number), no 4s, and a 9-6 ending that reads as 'lasting, smooth' in Chinese.</p>
<h2>Before you buy</h2>
<ul><li>Check for trademarks that use the same digits in your field.</li><li>Check the domain's history for spam or penalties.</li><li>Use an escrow service for any significant purchase.</li></ul>
<p>Want a numeric domain valued, or looking for one? <a href="~/lucky-numbers.html?need=domain">Talk to us</a>.</p>
""", [["Are numeric domains good for SEO?", "Rankings come from content and links; a numeric domain is neutral. Its strength is memorability and cross-language use."], ["Why do Chinese buyers like numeric domains?", "Digits are easy to type and remember, and they can carry lucky meanings."]]),

("internet-number-slang", "Internet number slang: how the world writes with digits", "From Thai 555 to Chinese 520, Korean 1004 and Arabizi 7777 — why people turn numbers into words.",
 None, """
<p>Every language that got online found its own way to write with numbers. Some codes are about speed, some fill in missing letters, and some are wordplay that only works when you say the digits aloud.</p>
<h2>Sound-alike codes</h2>
<p>Chinese is rich in these because many syllables share sounds. 520 (<em>wǔ èr líng</em>) is close to 我爱你, 'I love you'. 1314 echoes 一生一世, 'a whole lifetime'. 88 sounds like 'bye-bye'. 7456 sounds like 'I'm so angry'. Japanese goroawase does the same: 39 is 'thank you' and 4649 is <em>yoroshiku</em>. Korean has 1004 (<em>cheon-sa</em>, angel) and 8282 (<em>pal-i pal-i</em>, hurry up).</p>
<h2>Laughter codes</h2>
<p>Thai uses 555 because five is 'hâa'. Chinese uses 233 or 2333, from a laughing emoticon on an early forum. Arabizi writers use 7 for the letter ح, so 7777 sounds like laughter too.</p>
<h2>Letter-count codes</h2>
<p>English pager slang counted letters: 143 is I (1) love (4) you (3), and 831 is '8 letters, 3 words, 1 meaning'.</p>
<h2>Borrowed codes</h2>
<p>Some numbers become slang by association: 404 (the web's 'not found' error) means clueless, 411 means information, and 86 means to cancel or remove.</p>
<h2>Watch out for collisions</h2>
<p>The same digits can mean opposite things: 555 is laughter in Thai and crying in Chinese; 666 is praise in Chinese gaming and ominous in Western tradition. If you're using a number in a campaign, check every reading in the <a href="~/decode.html">decoder</a>, and browse the full <a href="~/slang.html">slang dictionary</a>.</p>
""", [["Why do Chinese people use numbers as words?", "Many digits sound like words, so number codes are quick, playful and sometimes discreet."], ["What is Arabizi?", "Arabic written with Latin letters and digits, such as 3 for ع and 7 for ح."]]),

("why-you-keep-seeing-repeating-numbers", "Why you keep seeing repeating numbers", "Angel numbers, the frequency illusion and the psychology of patterns — a balanced look.",
 None, """
<p>You glance at the clock: 11:11. A receipt totals 5.55. The car in front has 333 on the plate. If this keeps happening, you're in good company — and there are two very different ways to think about it.</p>
<h2>The spiritual reading</h2>
<p>In the angel-number tradition, repeating digits are messages: 111 for new beginnings, 222 for balance, 333 for support, 444 for protection, 555 for change, and so on up to 999 for completion. People use them as prompts — a moment to pause and ask what they're focused on. See our <a href="~/angel-numbers.html">angel numbers guide</a>.</p>
<h2>The psychological reading</h2>
<p>Psychologists point to the <strong>frequency illusion</strong> (also called the Baader–Meinhof phenomenon): once something catches your attention, you notice it everywhere, while ignoring the thousands of times you saw non-repeating numbers. Our brains are pattern detectors; repeating digits are visually striking, so they stand out.</p>
<p>There's also simple probability. Clocks show 11:11, 12:12 and similar twice a day, receipts and odometers roll through repeats constantly, and with dozens of numbers crossing your vision every hour, repeats are guaranteed.</p>
<h2>Can both be true?</h2>
<p>You can know the psychology and still find the prompt useful. Plenty of people treat 11:11 as a cue to set an intention without believing the clock is sending a message. The healthy line is simple: use it for reflection, never as a reason to make a big decision you'd otherwise avoid.</p>
<h2>What to do when you see one</h2>
<ul><li>Note what you were thinking about.</li><li>Look up the pattern if you're curious — <a href="~/decode.html">decode it</a> to see every cultural reading too.</li><li>Then carry on with your day.</li></ul>
""", [["Is seeing 11:11 a sign?", "Spiritually, many believe so; psychologically, it's the frequency illusion. Both readings can be useful."], ["Why do I see the same number everywhere?", "Attention plus probability: once a pattern matters to you, you notice it more."]]),
]

def build_all():
    tiles = "".join(f'<a class="tile" href="~/guides/{s}.html"><h3>{esc(t)}</h3><p>{esc(d)}</p></a>' for s, t, d, *_ in GUIDES)
    layout("guides.html", "Guides to number meanings, lucky numbers and numerology | 55596",
           "In-depth guides: 555 around the world, Chinese lucky numbers for business, life path calculation, 555 phone numbers in film, lucky business numbers, numeric domains and number slang.",
           f'<section class="wrap page-head"><h1>Guides</h1><p>Long reads that explain where number meanings come from and how to use them well.</p></section><section class="wrap section"><div class="grid g2">{tiles}</div>{lead_cta()}</section>',
           crumbs=[("Guides", None)], active="guides.html")
    for i, (slug, title, desc, vid, body, faq) in enumerate(GUIDES):
        others = "".join(f'<li><a href="~/guides/{s}.html">{esc(t)}</a></li>' for s, t, *_ in GUIDES if s != slug)
        video = f'<div class="mt2">{video_card(V[vid])}</div>' if vid else ""
        html_ = f'''<article class="wrap"><header class="page-head"><h1>{esc(title)}</h1><p>{esc(desc)}</p><p class="hint">By 55596 Editorial · Updated October 15, 2026</p></header>
<div class="split"><div><div class="prose">{body}</div>{video}<div class="prose mt2"><h2>Questions</h2></div>{faq_html(faq)}{lead_cta()}</div>
<aside class="stack sticky"><div class="panel"><h3>Decode a number</h3><form class="decode-form" action="~/decode.html" method="get" role="search"><label class="skip" for="g-n">Number</label><input id="g-n" name="n" inputmode="numeric" placeholder="Any number"><button class="btn" type="submit">Decode</button></form></div><div class="panel"><h3>More guides</h3><ul>{others}</ul></div></aside></div></article>'''
        layout(f"guides/{slug}.html", f"{title} | 55596", desc, html_, crumbs=[("Guides", "guides.html"), (title, None)], og_type="article",
               schema=[faq_schema(faq), {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "datePublished": "2026-10-15", "dateModified": "2026-10-15", "author": {"@type": "Organization", "name": "55596 Editorial"}, "publisher": {"@type": "Organization", "name": "55596"}}])
