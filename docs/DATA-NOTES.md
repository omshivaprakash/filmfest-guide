# Data notes, festival by festival

How complete each festival is, where its data comes from, and the known gaps. Counts are what `catalog.json` holds on `main` as of 26 November 2026; `node check-catalog.mjs` prints the current totals.

## Bengaluru International Film Festival (BIFFes)

17 editions on record, from the 1st (2006) to the 17th (2026), with **2,415 films**.

| Edition | Year | Films | Notes |
|---|---|---|---|
| 17th | 2026 | 242 | From the official catalogue, with stills |
| 16th | 2025 | 203 | Official catalogue, with stills and award winners |
| 15th | 2024 | 165 | Official catalogue, with stills |
| 14th | 2023 | 164 | Screening schedule from the Internet Archive |
| 13th | 2022 | 227 | Screening schedule from the Internet Archive |
| 12th | 2020 | 216 | Catalogue and retrospective awards |
| 11th | 2019 | 232 | Catalogue |
| 10th | 2018 | 213 | Catalogue |
| 9th | 2017 | 87 | Searchable PDF from the Internet Archive; partial |
| 8th | 2016 | 231 | Catalogue |
| 7th | 2014 | 172 | Catalogue |
| 6th | 2013 | 166 | Catalogue |
| 5th | 2012 | 3 | Award winners only; the catalogue is linked |
| 4th | 2011 | 94 | OCR of the Internet Archive scan; partial |
| 3rd, 2nd, 1st | 2009, 2008, 2006 | 0 | Catalogues linked as PDFs; titles still to come |

- Older catalogues are scans, so films can be missing and names garbled. Index-only entries carry the printed page number.
- Most Bengaluru films have no format in the catalogue and show as "Format unlisted".
- The **Archive documents** menu links the Servants of Knowledge scans on the Internet Archive.

## International Film Festival of India, Goa (IFFI)

56th (2025, 54 films) and 55th (2024, 48 films). Coverage is the **Indian Panorama** (feature and non-feature) from the Press Information Bureau, plus selected award winners. The international sections are not in yet.

## International Film Festival of Kerala (IFFK)

30th (2025, 206 films) from the screening schedule, and 29th (2024, 33 films) from three section selections. Earlier editions are still to come.

## International Documentary and Short Film Festival of Kerala (IDSFFK)

16th (2024, 151 films) from OCR of the official selection, with documentary, short film and music video formats.

## World festivals (work in progress)

- **About 8,100 festivals** in `world-festivals.json`, from Wikidata items that are an instance of "film festival" or a common subclass, excluding single editions. Only festivals with a name and a country are kept. Retrieved 26 November 2026.
- **163 countries**, grouped into regions (India is its own region).
- **About 1,300** have a description from the opening of their English Wikipedia article (`world-about.json`).
- **About 440** have a logo or image from Wikimedia Commons in `images/world/`, each with its licence and credit.
- **16 types**, from Wikidata classes and genres plus words in the name and description: Short film, LGBTQ+, Documentary, Environment and nature, Horror fantasy and sci-fi, Animation, Children and youth, Music and dance, Student and first films, Women, Experimental and art, Human rights and social, Mobile and online, Food sport and travel, Jewish, Indigenous. Many festivals have no type.
- **55 hand-checked** festivals in `catalog.json` → `worldFestivals` add the usual month.
- Films and people for these festivals are still to come.

## YouTube

33 films link to a trailer or full film on YouTube, from Wikidata's YouTube video ID. More will appear as Wikidata grows and as more films are matched.
