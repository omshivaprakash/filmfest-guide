# Contributing

Thank you for wanting to help. You do not need to be a programmer for most of this.

## The easiest ways to help (no code)

1. **Report a mistake.** [Open an issue](https://github.com/omshivaprakash/filmfest-guide/issues/new) and tell us:
   - *What* (the film, person or festival)
   - *Which festival and year*
   - *What is wrong, and what is right* (with a link to the source if you have one)
2. **Suggest a festival, or a source for one.** The best suggestions point to an official catalogue, schedule or award list, ideally for several years.
3. **Point us to old catalogues.** Scans on the Internet Archive or a festival's own archive fill the Past years tab.
4. **Fix a wrong YouTube link or festival type.** These come from Wikidata, so fixing them there helps everyone; tell us and we will refresh.
5. **Correct the research.** The [worldwide festival research](research/README.md) has many unchecked facts. Fix any line with a source link.
6. **Check the Kannada and Hindi labels.** They are new and need review by native speakers. Switch language on the home page, and if a label reads oddly, open an issue with the English text and your better wording, or edit the dictionary in [`i18n.js`](../i18n.js) directly.
7. **If you represent a festival, filmmaker or photographer:** tell us if anything should be corrected, updated or removed. We will act on it.

## If you are a developer

- Read [How it works](HOW-IT-WORKS.md), then [Maintaining](MAINTAINING.md).
- Fork the repo, make a change, and open a pull request.
- Before you do, run:
  ```
  node --check app.js && node check-catalog.mjs
  python3 -m http.server 8000
  ```
  and click through the views you touched on a phone-sized window and a laptop-sized one.
- Keep these house rules (the same as LitFest Guide):
  - **No screen may scroll the page.** Each view fits one screen and pages through content.
  - **No outside requests at load.** Keep images, fonts and data inside the repo.
  - **Every record links to its source.** Only add what a festival or open database has published.
  - **Say when something is derived.** Never present a guess as fact.
  - **Stay plain.** No framework, no build step.
  - **One extractor, one shard.** A new source gets its own folder in `tools/extractors/`, its own output in `data/`, and its own scheduled workflow.
- Bump `VERSION` in `sw.js` after changing the page shell, so installed copies refresh.

## Respecting the people listed

Credits, stills and portraits come from public festival material and open databases and belong to their owners. Please keep it that way: credit the source, and keep each image's licence with it.

## Code of conduct

Be kind. Assume good faith. This is a small, free project built out of love for cinema.

## License

By contributing you agree your code is released under the MIT licence (see [LICENSE](../LICENSE)) and your data changes under CC BY 4.0 (see [LICENSE-DATA.md](../LICENSE-DATA.md)).
