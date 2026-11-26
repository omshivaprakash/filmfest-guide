# Frequently asked questions

## About the project

**Who made this, and why?**
A film lover who got tired of digging through festival websites, PDF catalogues and old scans to find out what screened where. It is built as a free tool for other film lovers, and as an open, reusable record of film festivals, starting with India. It is the companion to [LitFest Guide](https://omshivaprakash.github.io/litfest-speaker-guide/).

**Is it official? Is it run by a festival?**
No. It is independent and not affiliated with, endorsed by or sponsored by any festival. Each festival's own site is the final word on its programme.

**Does it cost anything? Will it?**
No, and no. There are no ads, no accounts and nothing for sale. It runs on free hosting because it is just a folder of files.

**Can I use the data?**
Yes. The facts are open data under CC BY 4.0: use them for anything, including commercially, with attribution. The code is MIT. Stills, posters, portraits, logos and festival-written synopses belong to their owners. See [LICENSE-DATA.md](../LICENSE-DATA.md).

---

## About accuracy

**Why does an old edition have so few films, or none?**
Its catalogue is a scan, and text pulled from scans misses things. A PDF link in **Past years** means the source exists even when its titles are still to come. See [Data notes](DATA-NOTES.md).

**Why does a film say "Format unlisted"?**
The catalogue did not say whether it is a feature, documentary or short, and we do not guess.

**Why does a person appear twice?**
People are grouped by the exact spelling in the credits, so "S. Kumar" and "S Kumar" count as two. Merging two different real people would be worse, so we keep them apart.

**Why do some country names look different from the catalogue?**
Countries are tidied to one spelling each (`USA` and `United States` become `United States`) so the map can count them.

**A festival on the world list has the wrong type, city or founding year.**
These come from Wikidata. Fixing the item there fixes it for everyone, and the next refresh picks it up. Each festival’s sheet links to its Wikidata item.

**This YouTube link is the wrong film.**
Links are matched by title, year and director, so a mix-up is possible. [Open an issue](https://github.com/omshivaprakash/filmfest-guide/issues/new) and we will fix it.

**How often is the data refreshed?**
Each extractor runs on its own schedule through GitHub Actions; the schedules are listed in [Maintaining](MAINTAINING.md#scheduled-refreshes). The older importers run by hand.

---

## About privacy and use

**Do you track me?**
No. No analytics, no cookies, no accounts. Opening the site makes no requests to anyone but this site.

**Does it work offline?**
Yes, after your first visit. Install it to your home screen for an app-like window.

**I am a festival or filmmaker and want something changed or removed.**
[Open an issue](https://github.com/omshivaprakash/filmfest-guide/issues/new) and say what and where. Requests are taken seriously.
