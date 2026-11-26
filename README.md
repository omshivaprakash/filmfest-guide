# FilmFest Guide

**One free guide to what screens at film festivals, starting with India: the films, the people who made them, the awards, and every past edition we can find.**

Open it here: **https://omshivaprakash.github.io/filmfest-guide/**
Works on any phone or laptop. No account, no ads, no app store. You can install it like an app, and it keeps working without internet after your first visit.

It is the companion to **[LitFest Guide](https://omshivaprakash.github.io/litfest-speaker-guide/)** (literature festivals) and is built the same way.

---

## Why this exists (the short, honest version)

If you love cinema, a film festival is a feast. But planning for one, or looking back at one, is oddly hard.

- Every festival publishes its programme **in its own way**: a website, a PDF catalogue, a printed booklet, a press release.
- Last year's catalogue quietly disappears when the new one goes up, and older ones survive only as scans.
- You cannot easily answer simple questions like:
  - *"What won at Bengaluru ten years ago?"*
  - *"Has this director shown work at more than one Indian festival?"*
  - *"Which languages and countries does this festival actually screen?"*
  - *"Which film festivals exist near me, or for documentaries, shorts or animation?"*

**FilmFest Guide puts all of it side by side**, in one clean place, built for a thumb on a phone. It was built by a film lover, for film lovers. It is free, it will stay free, and it is not run by any festival.

---

## What you can do with it

| You want to… | Where to go |
|---|---|
| See every festival in the guide, the world map and award-winning films | **Home** (the **All** chip) |
| Open a festival: latest edition, films per edition, where to start | Festival chip, **Discover** tab |
| Browse the films, search by title, name, language or award, filter by format | **Films** tab |
| Browse everyone credited (directors, writers, actors, crew) | **People** tab |
| See the awards and who won them | **Awards** tab |
| See where a festival's films come from | A festival's **Map** tab |
| See every edition, with its catalogue PDF and archive documents | **Past years** tab |
| Look up a film or person across every festival | **Search** (top bar) |
| Map films, people or festivals worldwide | **Explore → Map** |
| See which festivals are on now, over or coming next | **Explore → Calendar**, or the strips on the home page |
| See which languages the films are in | **Explore → Languages** |
| Find filmmakers who return across festivals and editions | **Explore → Across festivals** |
| Browse 8,000+ film festivals worldwide by region, country or type (documentary, short, animation, LGBTQ+…) | **Explore → World festivals** |
| Watch a trailer or full film where one is on YouTube | A film's sheet, or **Films → On YouTube** |
| Use the site in Kannada (ಕನ್ನಡ) or Hindi (हिन्दी) | The language buttons on the home page or in **About** |

Every view fits one screen and pages instead of scrolling. Links are shareable: `?f=biffes` opens a festival and `#films`, `#people`, `#awards` or `#years` opens a tab.

Detailed steps are in the **[User guide](docs/USER-GUIDE.md)**.

**Languages (beta).** Menus, tabs, headings, captions and calendar statuses can be shown in Kannada or Hindi; the choice is remembered in your browser. Film titles, names, descriptions and other festival data stay in the language they were published in, and are never machine-translated. The translations live in [`i18n.js`](i18n.js) and **still need review by native speakers**: corrections are welcome as a GitHub issue or pull request.

---

## Festivals covered

**With films, credits and awards (4):** Bengaluru International Film Festival (BIFFes, 17 editions, 2006 to 2026) · International Film Festival of India, Goa (IFFI, 2024 and 2025) · International Film Festival of Kerala (IFFK, 2024 and 2025) · International Documentary and Short Film Festival of Kerala (IDSFFK, 2024)

**Listed and waiting to be added:** about 8,100 film festivals worldwide from Wikidata, including Cannes, Berlinale, Venice, Busan, Sundance, MAMI and FESPACO, each with its city, country, founding year, official site and, where available, a Wikipedia description and a logo. 55 of them are hand-checked with their usual month. They sit in 163 countries and are tagged with 16 festival types.

**By the numbers:** 2,907 films, about 6,700 credited people and 22 editions, plus about 1,300 Wikipedia descriptions and about 440 festival logos for the world list.

How complete each festival is differs. The picture for each one is in **[docs/DATA-NOTES.md](docs/DATA-NOTES.md)**.

---

## Open data

The facts behind the guide are open data under **CC BY 4.0**: `catalog.json` (festivals, editions, films, credits, awards) and `data/world-festivals/world-festivals.json` (the world list). The world list comes from Wikidata (CC0); Wikipedia descriptions are CC BY-SA 4.0. Cite it as *FilmFest Guide (omshivaprakash), https://omshivaprakash.github.io/filmfest-guide/, CC BY 4.0*. Details in [LICENSE-DATA.md](LICENSE-DATA.md) and [CITATION.cff](CITATION.cff). What each field means is in the **[Data dictionary](docs/DATA-DICTIONARY.md)**.

---

## Can I trust it?

Mostly, with care. Please read this part.

- **Titles, credits, sections and awards** come from each festival's own catalogues and announcements. Every film links to its source page. The festival's own site is always the final word.
- **Older catalogues are scans.** Text pulled out of a scan can miss films or garble a name. A PDF link on an edition means the source exists even when its titles are not indexed yet.
- **People** are built from credits by spelling, so a spelling variant counts as two people, and two people with the same name count as one.
- **Countries** are tidied to one spelling per country (`USA`, `Usa` and `United States` become `United States`).
- **Festival types** on the world list are read from Wikidata classes plus words in a festival's name and description. Treat them as a guide.
- **YouTube links** are the videos Wikidata records for a film, matched by title, year and director. A wrong match is possible; report it.

**Is it affiliated with any festival?** No. It is an independent project for **education and research**. Stills, posters, portraits and logos belong to their owners and are shown only to identify a film, person or festival; images from Wikimedia Commons keep their own licence and are credited. If you are a festival, filmmaker or photographer and want something corrected or removed, [open an issue](https://github.com/omshivaprakash/filmfest-guide/issues/new) and say what and where.

---

## Your privacy

- No sign-up, no tracking, no analytics, no cookies.
- The site makes **no requests to outside services** when a page loads. Fonts, images and data are all served from this repository. Festival sites and YouTube open only when you tap a link.

---

## How it works, in plain words

- It is a **website made of plain files**: one page, a few data files, and images. There is **no server, no database and no login**, which is why it is free to run and hard to break.
- A set of small scripts (the *tools*) reads festival catalogues, Wikidata and other public sources and writes those data files.
- **Extractors refresh the data on a schedule.** Each extractor has its own GitHub Actions workflow that runs it, validates the result and commits any change. See *Staying up to date* below.
- After your first visit, the site saves itself to your device, so it opens even without internet.

The longer version, with a diagram, is in **[docs/HOW-IT-WORKS.md](docs/HOW-IT-WORKS.md)**.

---

## Staying up to date

Each data source has an **extractor** in `tools/extractors/<name>/` that writes its own shard under `data/<name>/`, and a short workflow in `.github/workflows/<name>.yml` that runs it on a schedule through the shared [`extract.yml`](.github/workflows/extract.yml). A run validates the data with `node check-catalog.mjs` and commits only if something changed. The home page's **Data freshness** panel shows when each source last changed, from `sync.json`. The schedule for each extractor, and how to run one on your own computer, are in **[docs/MAINTAINING.md](docs/MAINTAINING.md#scheduled-refreshes)**.

---

## For the curious and the helpful

| I want to… | Read |
|---|---|
| Learn how to use every feature | [User guide](docs/USER-GUIDE.md) |
| Understand how it is built, without jargon | [How it works](docs/HOW-IT-WORKS.md) |
| Know what each data field means | [Data dictionary](docs/DATA-DICTIONARY.md) |
| Add a festival, run an extractor or refresh data | [Maintaining](docs/MAINTAINING.md) |
| See festival-by-festival notes and gaps | [Data notes](docs/DATA-NOTES.md) |
| Read or correct the worldwide festival research | [Research](docs/research/README.md) |
| Ask "why does it say…?" | [FAQ](docs/FAQ.md) |
| Report a mistake, suggest a festival, or help | [Contributing](docs/CONTRIBUTING.md) |

**Run it on your own computer:** download the folder, open a terminal in it, run `python3 -m http.server 8000`, and visit `http://localhost:8000`. (Opening `index.html` by double-click will not work, because browsers block loading data files that way.) After editing, run `node --check app.js && node check-catalog.mjs`; GitHub runs the same check on every push.

**Deploy:** GitHub Pages serves the repository root from `main`, so a merge to `main` is a release. Bump `VERSION` in `sw.js` when the page shell changes, so installed copies refresh.

**Licences:** the **code** is MIT ([LICENSE](LICENSE)). The **facts** are open data under **CC BY 4.0** ([LICENSE-DATA.md](LICENSE-DATA.md)). Stills, posters, portraits, logos and festival-written text stay with their owners and are not covered.

**Built by** [omshivaprakash](https://omshivaprakash.github.io/). To reach out, use the GitHub issues on this repository.
