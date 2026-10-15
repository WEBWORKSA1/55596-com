# 55596.com — Decode any number

A static, AdSense-ready website that decodes any number across angel numerology, numerology,
Chinese/East Asian lucky-number culture, internet slang and math — with a B2B lead-generation layer
for lucky/vanity phone numbers and numeric domains.

- Pure HTML/CSS/vanilla JS. Hosted free on GitHub Pages. No server, no database.
- All calculators run in the visitor's browser (no personal data sent anywhere).
- Forms post through FormSubmit; the destination address is assembled at runtime and never appears in the source.

## Structure
| Path | What |
|---|---|
| `index.html` | Home: keypad hero decoder, featured numbers, tools, lead CTA, videos, newsletter, support |
| `decode.html` | Full client-side decoder (`?n=555`) |
| `number/{n}/` | 49 editorial number guides with computed data and FAQ schema |
| `angel-numbers.html`, `numerology.html`, `culture.html`, `slang.html` | Topic hubs |
| `tools/*.html` | 8 calculators (life path, name, personal year, compatibility, lucky phone/plate/address, business name) |
| `lucky-numbers.html` | 3-step lead form + notify-me + free valuation |
| `support.html`, `contests.html`, `careers.html`, `advertise.html` | Donations/pledges, contests & prizes, hiring, sponsorship |
| `guides/*.html` | 8 long-form original guides |
| Legal | privacy, terms, cookies, disclaimer, trademark-copyright, editorial-standards, affiliate-disclosure |
| `ads.txt`, `robots.txt`, `sitemap.xml`, `site.webmanifest` | Monetisation & SEO files |
| `_src/` | Generator (`python3 _src/build.py`) and all content data |
| `PROMPTS.md` | Phase-wise build prompts |

## Rebuild
```
python3 _src/build.py
```
Edit content in `_src/data.py` (numbers, slang, combos, videos), `_src/pages.py` (pages) and `_src/guides.py` (articles).

## Launch checklist
1. **GitHub Pages:** Settings → Pages → Deploy from branch → `main` / root.
2. **Custom domain:** add `55596.com` under Settings → Pages (this creates the CNAME file), then point DNS:
   A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `www` CNAME → `webworksa1.github.io`. Enable "Enforce HTTPS".
3. **FormSubmit activation:** the first form submission triggers a one-time confirmation email to the site inbox. Click it once; all forms work after that.
4. **AdSense:** add the site in AdSense, keep Auto Ads on, and enable Google's Privacy & messaging consent message for EEA/UK/CH visitors.
5. **Search Console:** submit `https://55596.com/sitemap.xml`.

## Trademark & copyright
"55596" is used as a descriptive numeric domain. The site is not affiliated with any company, product,
telephone service or trademark containing the digits 555, 96 or 55596. Original content © 2026 55596.com.
Embedded videos belong to their creators.
