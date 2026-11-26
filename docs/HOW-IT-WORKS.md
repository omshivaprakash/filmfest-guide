# How it works (without jargon)

This page explains how FilmFest Guide is put together. You do not need to be a programmer to follow it.

## The big idea

> A website can be just **files**: a page, some lists, some pictures. If nothing needs to be calculated on a computer somewhere, you do not need a server, and it costs nothing to keep running.

FilmFest Guide is exactly that. When you open it, your own phone or laptop reads the files and draws the screens. Nothing is sent back.

```
 Sources                        Extractors (scripts)            The repo (this folder)           You
 ─────────────────────          ─────────────────────          ───────────────────────        ──────────────
 festival catalogues,   ──►     read the public files   ──►    data files + images     ──►    your phone or
 schedules, Wikidata,           and tidy them up               + one web page                  laptop shows it
 Internet Archive

        ▲                                                                                        │
        └──────  GitHub Actions run each extractor on a schedule and commit any change  ─────────┘
```

## The pieces

### 1. The page: `index.html`, `style.css`, `app.js`, `geo.js`, `calendar.js`
These files are the whole app: the screens, the colours and the logic. `geo.js` holds the world map outlines and a position for each country. `calendar.js` works out, from today's date in the browser, whether each festival is on now, over or coming next: exact dates come from edition `dates`; without them it uses the last edition's dates or the usual `month` and labels the result "usually", so no date is invented. There is no framework and no build step.

### 2. The guide's data: `catalog.json`
One file with five lists: `festivals` (with their editions), `films` (with credits and awards), `honors` (awards given to a person rather than a film), `portraits` (credited photos of people) and `worldFestivals` (55 hand-checked festivals still to add). The People directory, the maps and the language counts are worked out from this file when the page loads.

### 3. The world list: `data/world-festivals/world-festivals.json` and `data/world-festivals/world-about.json`
About 8,100 film festivals from Wikidata. The list loads after the first screen so the page opens fast. The longer Wikipedia descriptions sit in `data/world-festivals/world-about.json` and load only when you open a festival.

### 4. Images: `images/`
Film stills and posters from the catalogues, portraits, and festival logos from Wikimedia Commons in `data/world-festivals/logos/`. Each image records its source and, where it has one, its licence.

### 5. The tools: `tools/`
Small Python scripts that collect the data. The older importers (`tools/import-*.py`) read one source each and write into `catalog.json`. The world list and YouTube links, and all new sources, go in `tools/extractors/<name>/` and write a shard under `data/<name>/`, one per source, so extractors never fight over the same file. They are only needed when updating data, never to *use* the site. See [Maintaining](MAINTAINING.md).

### 6. The offline copy: `sw.js` and `manifest.webmanifest`
A small helper (a "service worker") saves the site on your device after your first visit, so it opens without internet. The manifest lets you install it to your home screen.

### 7. The checks: `check-catalog.mjs` and `.github/workflows/`
- `check-catalog.mjs` checks the data: film ids are unique, every film belongs to a real edition, every link is `https`, every festival has coordinates, and every world logo has a file and a licence.
- GitHub runs it (and `node --check app.js`) on every push and pull request, so a mistake is caught before visitors see it.
- Each extractor has its own scheduled workflow that refreshes its data and runs the same check before committing.

## How the derived fields are made

Everything shown comes from a source. A few things are worked out by simple rules, never by an AI that makes things up:

| Field | Rule |
|---|---|
| **People** | Every name in a film's credits, grouped by exact spelling. |
| **Country** | The catalogue's country, tidied to one spelling per country. |
| **Language** | The catalogue's language field, split on commas. |
| **Across festivals** | People whose name appears at more than one festival or edition. |
| **Festival types** | Wikidata classes and genres, plus words in the festival's name and description. |
| **Region** | Worked out from the country (India is its own region). |
| **YouTube** | Wikidata's YouTube video ID for a film, matched by title, year within two and director. |

## Why images and fonts are inside the repository

So that the site makes **no requests to outside companies** when it loads. It is faster, works offline, and cannot leak your visit to anyone.

## Where it is hosted

On **GitHub Pages**, a free service that publishes a folder of files as a website. It serves the repository root from `main`, so every merge updates the site.

## What it deliberately does *not* do

- No accounts, no sign-up, no comments.
- No tracking or analytics.
- No server that could go down or be hacked.
- No selling of anything.
