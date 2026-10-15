# 55596.com — Phase-wise Build Prompts

Concept: **55596 · Decode any number.** A global number-meaning engine (angel numbers, numerology,
Chinese/Asian cultural readings, internet number slang, math facts) with a B2B lead-generation layer
for lucky/vanity phone numbers, licence plates, addresses and numeric domains.

Stack constraints for every phase: static HTML/CSS/vanilla JS only, no server, no build step required
to serve (a Python generator is allowed to produce the HTML), hostable on the free GitHub Pages plan.
AdSense publisher `ca-pub-6620975821265271` (Auto Ads script in every `<head>`). One contact address
for the whole site, never written in plain text anywhere in the source; forms post via a JS-assembled
FormSubmit endpoint. A top banner on every page links to `https://web.works/contact`.

---

## Phase 0 — Research & positioning
> Research the number "55596" across commerce, business, AI, economy and people. Decompose it
> (555 / 96 / 5-5-5-9-6 / digit sum 30 → 3) and document every meaning layer: angel numerology,
> Thai 555 laughter, Chinese 555 crying, 9 = 久 lasting, 6 = 流 flow, the NANP 555 fictional prefix.
> Rank monetisation models by traffic ceiling, RPM, lead value and AdSense risk. Output: a one-page
> positioning brief, a name, a tagline, and the revenue stack (AdSense, B2B leads, sponsorship,
> donations/pledges, affiliates later).

## Phase 1 — Competitive teardown (25+ sites)
> Audit at least 25 sites across numerology (numerology.com, numerologist.com, worldnumerology.com,
> cafeastrology.com), angel numbers (angelnumber.org, Joanne Sacred Scribes, bustle, crystals.com),
> number facts (numbersaplenty.com, dcode.fr), cultural meaning (Wikipedia, lingoace, thatsmandarin,
> juwai), and B2B number sellers (numberbarn, ringboost, vanitynumbers, didforsale, regtransfers,
> afternic). Record pages, tools, forms, lead capture, monetisation, design, URL patterns and one
> idea to copy from each. Synthesize must-haves, converting lead patterns, IA, design and AdSense
> cautions.

## Phase 2 — Information architecture & design system
> Define the sitemap: Home, Decoder, Number pages (/number/{n}/), Angel numbers hub, Numerology hub,
> Culture hub, Slang dictionary, Tools directory + 8 calculators, Lucky Numbers (B2B lead gen),
> Guides, Videos, Support (donations/pledges), Contests, Careers, Advertise, About, Contact, and the
> legal set (Privacy, Terms, Disclaimer, Cookies, Trademark & Copyright, Editorial standards,
> Affiliate disclosure), Thank-you, 404. Design tokens: cool white base, ink indigo text, saffron /
> jade / rose meaning badges; Bricolage Grotesque display + Atkinson Hyperlegible body. Signature
> element: phone-keypad digit keys (5 = JKL) used for every number display. Mobile-first, sticky
> bottom action bar on phones, visible focus, reduced-motion respected.

## Phase 3 — Number engine (assets/js/numbers.js)
> Build one client-side engine that, for any input up to 15 digits, returns: digit anatomy and
> reduction (master numbers 11/22/33 kept), angel-number reading for repeating/patterned numbers,
> per-digit Chinese reading (Mandarin/Cantonese homophones, lucky/neutral/unlucky), known
> combinations (168, 520, 1314, 518, 250, 2333…), slang matches by language (Thai 555, Chinese 555,
> 2333, 88, 666, Korean 1004, Japanese 39…), math facts (prime, factors, divisor count, square,
> palindrome, bases 2/8/16, Roman, words) and a 0–100 "luck score" for phone/plate/address use with
> better alternatives. Everything runs in the browser — nothing personal is sent anywhere.

## Phase 4 — Core pages & programmatic number pages
> Generate the home page (keypad hero decoder, birthdate quick form, number tile grid, 55596 story,
> lead magnet, B2B CTA, videos, support strip), the decoder page, and ~45 editorial number pages only
> for numbers with real cultural/angel/slang significance. Each page: unique editorial paragraph,
> computed anatomy, culture badges, slang chips, math facts, related-numbers table, prev/next links,
> FAQ with FAQPage schema, breadcrumbs. No thin or near-duplicate pages; long-tail numbers stay in the
> client-side decoder, not as indexable URLs.

## Phase 5 — Tools
> Build 8 calculators on the shared engine: Life Path, Name/Expression (Pythagorean + Chaldean),
> Personal Year, Compatibility, Lucky Phone Number scorer, Lucky Plate scorer, Lucky Address scorer,
> Business Name number. Each result offers a next step (decode the number, get a better number).

## Phase 6 — Lead generation (the revenue engine)
> Build /lucky-numbers.html: a 3-step high-intent form (what you need → preferences & budget →
> contact), plus "Notify me when a pattern is available", "Free valuation of my number/domain", and a
> score-to-lead bridge from every scorer result. Add trust blocks (process, FAQs, what happens next),
> no ads on lead pages. Every form posts through the obfuscated FormSubmit handler and redirects to
> /thank-you.html.

## Phase 7 — Community & funding
> Support page with pledge tiers earmarked for operations, promotions, marketing, hiring talent,
> contests & prizes; a sponsor-a-number program; transparency notes. Contests page (monthly prompts,
> prizes, rules, entry form). Careers page (open roles, application form). Advertise page (packages,
> inquiry form).

## Phase 8 — Content & video
> Write 8 long-form original guides (555 around the world, Chinese lucky numbers in business, life
> path how-to, 555 phone numbers in film, choosing a lucky business number, numeric domains explained,
> internet number slang, the story of 55596). Embed verified YouTube videos with privacy-enhanced
> lite embeds (click-to-load) on the Videos page and inside relevant guides.

## Phase 9 — Compliance, SEO & launch
> AdSense: Auto Ads script on every page, ads.txt, no ads inside forms or next to calculator
> buttons, no deceptive claims (meanings framed as culture and entertainment), sensitive slang
> described mildly. Legal set incl. Trademark & Copyright disclosure. Cookie consent banner.
> SEO: unique titles/descriptions, canonical URLs, Open Graph, JSON-LD (Organization, WebSite
> SearchAction, BreadcrumbList, FAQPage, WebApplication), sitemap.xml, robots.txt, manifest, favicon.
> Verify: no plain-text email anywhere in the build output, every page has the top banner and the
> AdSense script, all internal links resolve. Push to WEBWORKSA1/55596-com and publish on GitHub Pages.
