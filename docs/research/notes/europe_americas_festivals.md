# Major International Film Festivals of Europe and the Americas: Reference Data (as of 26 Nov 2026)

Legend for reliability, used throughout:
- **[V]**: verified this session from the cited 2026 source.
- **[BG]**: background or reference knowledge (founding year, venues, market names, URLs, approximate coordinates). Stable and widely documented, but **not re-fetched this session**. The cited URL is the official site where the field should be checked before loading into the app.
- Coordinates are approximate (to about 3 decimals) for the main venue, always [BG].
- Submission platforms, fees and deadlines were **not verified** this session (see Gaps). Treat them as indicative only.

---

## Q1. What is the current (2026) FIAPF accredited list for these regions?

### Takeaway
In 2026 FIAPF ran its biggest reform since 2007. It dropped the old four-category system (competitive, specialised competitive, non-competitive, documentary/short) and replaced it with **one unified accredited list of 49 festivals in 29 countries**. Within that list, **17 festivals carry a new "A-Festival" label**. Of the 17, 11 are in Europe or the Americas: Cannes, Berlin, Venice, Locarno, San Sebastián, Karlovy Vary, Warsaw, Tallinn Black Nights, Annecy, Clermont-Ferrand, Toronto and Mar del Plata (12 counting Toronto and Mar del Plata separately, as listed below). **The old "competitive / specialised / non-competitive / doc-short" category field is obsolete for 2026.** The app should store `fiapf_accredited: bool` and `fiapf_a_festival: bool` instead.

### Cited Findings
- FIAPF classified 17 festivals as "A" festivals, in "the biggest reform of the accreditation process" since 2007. The 'A' label had been dropped about 20 years earlier. The reform replaces the previous four-category system with one unified list. Accredited festivals rise to 49 in 29 countries. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- The 17 A-festivals are Cannes, Berlin, Venice, Locarno, San Sebastián, Annecy (new), Clermont-Ferrand (new), Busan (new), Toronto (new), Mar del Plata, Shanghai, Cairo, IFFI Goa, Tokyo, Warsaw, Karlovy Vary and Tallinn Black Nights. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- Six festivals were newly accredited: Golden Apricot Yerevan, Herceg Novi, Festival du Nouveau Cinéma (Montréal), Hot Docs (Toronto), Annecy and Punto de Vista (Pamplona). — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- **Conflict:** the Screen Daily table also ticks Golden Apricot, FNC, Hot Docs, Herceg Novi and Punto de Vista in its "A-List" column, which contradicts its own count of 17. The FIAPF 2026 calendar PDF asterisks only the 17 (see table). **Use the FIAPF PDF.** — [FIAPF 2026 calendar PDF (dated 11 Mar 2026)](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf)

**Official FIAPF 2026 accredited list, Europe + Americas subset** (dates from the FIAPF calendar PDF; ★ = A-Festival) — [FIAPF PDF](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf) [V]

| # | Festival | Country | 2026 dates (FIAPF) | A? |
|---|---|---|---|---|
| 1 | Festival de Cine Global Santo Domingo | Dominican Rep. | 28 Jan – 4 Feb | |
| 2 | Clermont-Ferrand Int'l Short Film Festival | France | 30 Jan – 7 Feb | ★ |
| 3 | Berlinale | Germany | 12 – 22 Feb | ★ |
| 4 | Tampere Film Festival | Finland | 4 – 8 Mar | |
| 5 | Málaga Film Festival | Spain | 6 – 15 Mar | |
| 6 | Sofia IFF | Bulgaria | 12 – 22 Mar | |
| 7 | Punto de Vista (Pamplona) | Spain | 20 – 25 Apr | (new) |
| 8 | Hot Docs (Toronto) | Canada | 23 Apr – 3 May | (new) |
| 9 | Oberhausen Int'l Short Film Festival | Germany | 28 Apr – 3 May | |
| 10 | Festival de Cannes | France | 12 – 23 May | ★ |
| 11 | Krakow Film Festival | Poland | 31 May – 7 Jun | |
| 12 | Transilvania IFF (Cluj) | Romania | 12 – 21 Jun | |
| 13 | Cinema Jove (Valencia) | Spain | 19 – 27 Jun | |
| 14 | Annecy Int'l Animation Film Festival | France | 21 – 27 Jun | ★ (new) |
| 15 | Karlovy Vary IFF | Czech Rep. | 3 – 11 Jul | ★ |
| 16 | Golden Apricot Yerevan IFF | Armenia (transcontinental; often grouped with Europe) | 12 – 19 Jul | (new) |
| 17 | Cinedays (Skopje) | North Macedonia | TBA | |
| 18 | Locarno Film Festival | Switzerland | 5 – 15 Aug | ★ |
| 19 | Herceg Novi Film Festival | Montenegro | 22 – 28 Aug | (new) |
| 20 | Venice IFF (Mostra) | Italy | 2 – 12 Sep | ★ |
| 21 | Toronto IFF (TIFF) | Canada | 10 – 20 Sep | ★ |
| 22 | Fantastic Fest (Austin) | USA | 17 – 24 Sep | |
| 23 | San Sebastián IFF | Spain | 18 – 26 Sep | ★ |
| 24 | Festival du Nouveau Cinéma (Montréal) | Canada | 7 – 18 Oct | (new) |
| 25 | Sitges Int'l Fantastic Film Festival of Catalonia | Spain | 8 – 18 Oct | |
| 26 | Warsaw IFF | Poland | 9 – 18 Oct | ★ |
| 27 | Rome Film Fest | Italy | 14 – 25 Oct | |
| 28 | Viennale | Austria | 22 Oct – 3 Nov | |
| 29 | Molodist Kyiv IFF | Ukraine | TBA | |
| 30 | Mar del Plata IFF | Argentina | 5 – 15 Nov | ★ |
| 31 | Mostra de València – Cinema del Mediterrani | Spain | 5 – 15 Nov | |
| 32 | Kitzbühel Film Festival | Austria | TBA | |
| 33 | Antalya Golden Orange | Türkiye (transcontinental) | TBA | |
| 34 | Tallinn Black Nights (PÖFF) | Estonia | 6 – 22 Nov | ★ |
| 35 | Gijón/Xixón IFF (FICX) | Spain | 13 – 21 Nov | |
| 36 | Zinebi (Bilbao, doc & short) | Spain | 20 – 27 Nov | |
| 37 | Torino Film Festival | Italy | 24 Nov – 2 Dec | |
| 38 | Noir in Festival (Milan/Como) | Italy | TBA | |

Non-Euro-American FIAPF festivals, for completeness: Bengaluru, Sydney, Shanghai★, Eurasia (Kazakhstan), Busan★, Tokyo★, Kolkata, Cairo★, IFFI Goa★, Fajr, IFFK Kerala. — [FIAPF PDF](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf)

### Inferences
- Several "top-tier" festivals are **not** FIAPF-accredited: Sundance, Rotterdam (IFFR), Tribeca, SXSW, Telluride, NYFF, BFI London, IDFA, CPH:DOX, Morelia, Guadalajara, BAFICI, Cartagena, Havana, Gramado and Festival do Rio. None of them appears in the 2026 PDF. The app should rank prestige separately from FIAPF status.
- In the Americas, only Toronto and Mar del Plata are A-festivals. The other FIAPF festivals there are Hot Docs, FNC, Fantastic Fest and Santo Domingo Global.
- Former FIAPF members that are absent from the 2026 list (from the PDF; earlier status is [BG], unverified): Moscow IFF (likely dropped after 2022), Thessaloniki, Stockholm, Kyiv Molodist (still listed, dates TBA) and Bratislava. Do not tag any of these as FIAPF in 2026.

### Gaps
- fiapf.org itself could not be fetched (robots.txt unreachable). The list above relies on FIAPF's own PDF, which is authoritative, plus Screen Daily. The exact date of the reform announcement was not given in the article; it appears to be early 2026 (PDF dated 11 Mar 2026).
- The PDF gives no cities. The cities in the app table are [BG].

---

## Q2. What were the 2026 top prize winners at the biggest festivals?

### Takeaway
2026 top prizes:
- Cannes: *Fjord* (Cristian Mungiu, his second Palme)
- Berlin: *Yellow Letters* (İlker Çatak)
- Venice: *Woman Unknown* (May el-Toukhy)
- TIFF People's Choice: *La bola negra* (Javier Calvo & Javier Ambrossi)
- Sundance US Dramatic: *Josephine* (Beth de Araújo)
- Locarno: *You Don't Belong Here* (Florin Șerban)
- San Sebastián: *Tender Loving Care* (Mike Leigh)
- Karlovy Vary: *Fruit Gathering* (Aung Phyoe)
- Rotterdam Tiger: *Variations on a Theme* (Jason Jacobs & Devon Delmar)

Two patterns stand out: Romanian directors won both Cannes and Locarno, and *La bola negra* won both Cannes Best Director and the TIFF audience award.

### Cited Findings

**Cannes (79th, 12–23 May 2026; jury president Park Chan-wook; opener *The Electric Kiss*, Pierre Salvadori)**
- Palme d'Or: *Fjord* (Cristian Mungiu). Grand Prix: *Minotaur* (Andrey Zvyagintsev). Jury Prize: *The Dreamed Adventure* (Valeska Grisebach).
- Best Actress: Virginie Efira and Tao Okamoto (*All of a Sudden*). Best Actor: Emmanuel Macchia and Valentin Campagne (*Coward*). Screenplay: Emmanuel Marre (*A Man of His Time*).
- Un Certain Regard Prize: *Everytime* (Sandra Wollner). Short Film Palme: *For the Opponents* (Federico Luis).
- Sources: [Wikipedia: 2026 Cannes](https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival); [Euronews](https://euronews.com/culture/2026/05/23/cannes-2026-cristian-mungius-political-drama-fjord-wins-the-palme-dor) [V]
- Best Director, shared: Javier Ambrossi & Javier Calvo (*La Bola Negra*) and Paweł Pawlikowski (*Fatherland*). — [Euronews](https://euronews.com/culture/2026/05/23/cannes-2026-cristian-mungius-political-drama-fjord-wins-the-palme-dor). The Wikipedia extract did not name the director winner.
- Caméra d'Or: not confirmed. Wikipedia lists *A Girl Unknown* (Zou Jing) among the first-feature awards without labelling it. Treat as a gap.

**Berlinale (76th, 12–22 Feb 2026; jury president Wim Wenders)**
- Golden Bear: *Yellow Letters* (İlker Çatak, German-Turkish).
- Silver Bear Grand Jury Prize: *Salvation* (Emin Alper). Silver Bear Jury Prize: *Queen at Sea* (Lance Hammer).
- Silver Bear Best Director: Grant Gee (*Everybody Digs Bill Evans*).
- Silver Bear Best Lead Performance: Sandra Hüller (*Rose*). Supporting Performance: Anna Calder-Marshall & Tom Courtenay (*Queen at Sea*).
- Screenplay: Geneviève Dulude-De Celles (*Nina Roza*). Outstanding Artistic Contribution: Anna Fitch & Banker White (*Yo (Love Is a Rebellious Bird)*).
- Sources: [Outlook India](https://www.outlookindia.com/art-entertainment/berlinale-2026-full-winners-list-out); dates from the [FIAPF PDF](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf) [V]
- The festival was overshadowed by a Gaza-related controversy. — [Times of Israel](https://www.timesofisrael.com/berlin-film-festival-closes-after-being-beset-by-stormy-seas-of-gaza-war/); [Dawn](https://www.dawn.com/news/1974925)

**Venice (83rd, 2–12 Sep 2026; jury president Maggie Gyllenhaal)**
- Golden Lion: *Woman Unknown* (May el-Toukhy, Denmark-set).
- Silver Lion Grand Jury Prize: *Possible Love* (Lee Chang-dong). Silver Lion Best Director: Ilya Khrzhanovsky (*Dau*; the source spells it "Krzhanovsky"). Special Jury Prize: *NAZA* (Yuval Abraham & Rachel Szor).
- Volpi Cup Best Actor: John Malkovich (*Wild Horse Nine*, dir. Martin McDonagh). Best Actress: Mathilde Arcel (*Woman Unknown*).
- Screenplay: Stéphane Brizé (*A Good Little Soldier*). Marcello Mastroianni Award: Malou Khebizi (*15/18 (A Place to Heal)*, Cédric Kahn).
- Sources: [Euronews](https://www.euronews.com/culture/2026/09/12/venice-film-festival-2026-woman-unknown-of-may-el-toukhy-wins-the-golden-lion); [AV Club](https://www.avclub.com/venice-film-festival-winners-2026) [V]
- Orizzonti winners were not retrieved (gap).

**TIFF (51st, 10–20 Sep 2026; opener *Being Heumann*, Sian Heder)**
- People's Choice: *La bola negra* (Javier Calvo & Javier Ambrossi). Runners-up: *I Play Rocky* (Peter Farrelly), *Being Heumann*.
- International People's Choice: *Elsinore* (Simon Stone). Documentary People's Choice: *Darlene Love: I Know Where I've Been* (Barry Avrich). Midnight Madness People's Choice: *Ladies and Gentlemen, Brian Mulroney* (Matthew Rankin).
- Platform Prize: *Angh* (Theja Rio). Best Canadian Feature: *Sunburn* (Serville Poblete). FIPRESCI: *Ancestors* (David Turpin). NETPAC: *Thirteen in Gaza* (Hosam Abu Dan).
- Sources: [Wikipedia: 2026 TIFF](https://en.wikipedia.org/wiki/2026_Toronto_International_Film_Festival); [TheWrap](https://thewrap.com/industry-news/awards/la-bola-negra-wins-tiff-peoples-choice-award) [V]
- 2026 venues: Princess of Wales, Roy Thomson Hall, Royal Alexandra, TIFF Lightbox, Scotiabank Theatre, and the John Bassett Theatre at the Metro Toronto Convention Centre (new). A **new TIFF film market** ran at the Metro Toronto Convention Centre. — [Wikipedia](https://en.wikipedia.org/wiki/2026_Toronto_International_Film_Festival) [V]

**Sundance (22 Jan – 1 Feb 2026, Park City & Salt Lake City; the final Utah edition, moving to Boulder, Colorado in 2027)**
- Grand Jury Prizes: US Dramatic *Josephine* (Beth de Araújo; it also won the US Dramatic Audience Award). US Documentary *Nuisance Bear* (Gabriela Osio Vanden & Jack Weisman). World Dramatic *Shame and Money* (Visar Morina). World Documentary *To Hold a Mountain* (Biljana Tutorov & Petar Glomazić). Short Film *The Baddest Speechwriter of All* (Ben Proudfoot & Stephen Curry).
- Audience Awards: US Documentary *American Pachuco: The Legend of Luis Valdez*. World Dramatic *Hold Onto Me (Κράτα Με)*. World Documentary *One in a Million*.
- Alfred P. Sloan Prize: *In the Blink of an Eye* (Andrew Stanton).
- Sources: [Sundance.org](https://www.sundance.org/blogs/the-complete-list-of-2026-sundance-film-festival-award-winners/); [Wikipedia: 2026 Sundance](https://en.wikipedia.org/wiki/2026_Sundance_Film_Festival) [V]

**Locarno (79th, 5–15 Aug 2026)**
- Pardo d'oro: *You Don't Belong Here* / *Nu e locul tău aici* (Florin Șerban, Romania). Special Jury Prize: *The Riverbank* (Matheus Farias & Enock Carvalho). Best Direction: Hong Sang-soo (*Nowhere to Lay My Eyes*).
- Cineasti del presente Golden Leopard: *The Illusion of an Everlasting Summer* (Alessandra Sanguinetti).
- Leopard of Honour: Darren Aronofsky. Pardo alla Carriera: James Gray.
- Sources: [Wikipedia: 79th Locarno](https://en.wikipedia.org/wiki/79th_Locarno_Film_Festival); [Romania Insider](https://www.romania-insider.com/florin-serban-top-prize-locarno-film-festival-2026) [V]
- **Conflict:** Wikipedia's performance-award listing was garbled. Sorrisi reports Monica Bellucci as Best Actress at Locarno 79. — [Sorrisi](https://www.sorrisi.com/cinema/attori-attrici/monica-bellucci-miglior-attrice-a-locarno-79/). Verify before loading.

**San Sebastián (74th, 18–26 Sep 2026; jury president Ira Sachs)**
- Golden Shell: *Tender Loving Care* (Mike Leigh, UK; also Best Screenplay). Special Jury Prize: *Border* (China). Silver Shell Best Director: Amanda Kernell (*Brace Your Heart*).
- Best Lead Performance, shared: Kate O'Flynn (*Tender Loving Care*) and the lead of *Growth of the Soil*. Best Cinematography: *Growth of the Soil* (Hans Petter Moland). Supporting: Javier Cámara (*5 minutos más*).
- Audience Award: *La bola negra* (outside the Official Section).
- Sources: [Ara](https://en.ara.cat/culture/indisputable-golden-shell-to-mike-leigh-for-the-extraordinary-tender-loving-care_1_5862038.html); [Screen Daily headline](https://www.screendaily.com/news/mike-leighs-tender-loving-care-wins-golden-shell-at-san-sebastian/5220797.article) [V]

**Karlovy Vary (60th, 3–11 Jul 2026)**
- Crystal Globe: *Fruit Gathering* (Aung Phyoe; Myanmar–Czech–France). Special Jury Prize and Best Director: *The Guest* (Mads Mengel, Denmark).
- Best Actor: Ghassan Saad (*Pipes*). Best Actress: Anna Schinz (*A Happy Family*).
- Proxima Grand Prix: *Lover, Not a Fighter* (Martina Buchelová, Slovakia–Czechia). Audience Award: *Bára – Diary of a Rockstar* (Helena Třeštíková).
- **2027 (61st): 2–10 July 2027.**
- Source: [KVIFF official](https://www.kviff.com/en/news/6023-the-crystal-globe-goes-to-fruit-gathering-lover-not-a-fighter-wins-the-proxima-competition) [V]

**IFFR Rotterdam (55th, late Jan – early Feb 2026)**
- Tiger Award (€40,000): *Variations on a Theme* (Jason Jacobs & Devon Delmar; South Africa/Netherlands/Qatar). Big Screen Award: *Master* (Rezwan Shahriar Sumit, Bangladesh).
- Tiger Special Jury Awards: *La belle année* (Angelica Ruffier) and *Supporting Role* (Ana Urushadze; also FIPRESCI).
- Source: [IFFR official](https://iffr.com/en/blog-iffr-2026-tiger-big-screen-award-winners) [V]. The 2026 dates were not stated (gap).

**Other 2026 winners found**
- Annecy (50th edition per Unifrance): Cristal for a Feature *The Violinist* (Ervin Han & Raúl García; Singapore/Spain/Italy). Contrechamp Grand Prix *Blaise* (Dimitri Planchon & Jean-Paul Guigue). Cristal for a Short *Paper Trail* (Don Hertzfeldt). — [Cartoon Brew](https://www.cartoonbrew.com/festivals/annecy-winners-2026-violinist-iron-boy-paper-trail-263799.html); [Unifrance](https://en.unifrance.org/news/17471/l-animation-francaise-recompensee-au-50e-festival-d-annecy) [V]
- Mar del Plata (41st, 5–15 Nov 2026; awards 14 Nov): the top international prize went to *The Night Arezou Disappeared* (Arian Vazirdaftari, Iran). Best Actor: Andrew Scott (*Elsinore*). Best Argentine Feature: *Cebar, frenar, llorar* (Gerardo Tassan). Best Latin American Feature: *El pez que fuma* (Luis Fernández). — [Otros Cines](https://www.otroscines.com/post/festival-de-mar-del-plata-2026-todos-los-premios) [V]. The source calls the prize "Premio Astor Piazzolla"; it is traditionally the Astor de Oro.
- Morelia FICM (24th, Oct 2026): Best Mexican Feature *6 meses en el edificio rosa con azul* (Bruno Santamaría Razo). Best Mexican Documentary *Forensita* (Pablo Vaca). — [Chilango](https://www.chilango.com/cine-y-tv/peliculas/ficm-2026-lista-completa-de-ganadores/) [V]
- Gramado (54th, Aug 2026): Kikito for Best Brazilian Feature *Nosso Segredo*. *Feito Pipa* won four Kikitos. — [Jornal do Comércio](https://www.jornaldocomercio.com/cultura/2026/08/1260657-nosso-segredo-recebe-o-kikito-de-melhor-filme-no-54-festival-de-cinema-de-gramado.html); [O Hoje](https://ohoje.com/2026/08/24/nosso-segredo-vence-festival-de-gramado-e-feito-pipa-leva-quatro-kikitos/) [V, from headlines]
- BAFICI (27th, April 2026): the international competition was won by Argentine directors Ezequiel Salinas & Ramiro Sonzini. — [Unidiversidad](https://www.unidiversidad.com.ar/los-argentinos-ezequiel-salinas-y-ramiro-sonzini-ganadores-del-bafici-internacional) [headline only; film title not retrieved]
- CPH:DOX 2026: *Whispers in May* (Dongnan Chen) "wins big". — [Screen Daily headline](https://www.screendaily.com/news/dongnan-chens-coming-of-age-story-whispers-in-may-wins-big-at-cphdox-2026/5215063.article) [headline only; DOX:AWARD not confirmed]

### Inferences
- *La bola negra* won Cannes Best Director (shared), the TIFF People's Choice and the San Sebastián audience prize. It is the year's crossover title and an Oscar-path film, per [AP via Local10](https://www.local10.com/entertainment/2026/09/20/la-bola-negra-wins-tiffs-people-choice-award-putting-it-on-oscar-path/).
- *Elsinore* (Simon Stone) won both the TIFF International People's Choice and the Mar del Plata audience award.

### Gaps
- Not retrieved: Cannes Caméra d'Or, Venice Orizzonti, a clean Locarno performance list, the Clermont-Ferrand 2026 Grand Prix (the search returned only sports results), Hot Docs 2026 Best International Feature, Tribeca 2026 winners (press release exists at [Tribeca](https://tribecafilm.com/press-center/festival/press-releases/2026-tribeca-festival-announces-winners) but was not fetched), SXSW, NYFF (non-competitive) and IDFA 2026 (runs 12–22 Nov; results may be just out).

---

## Q3. Which festivals attach markets/co-production forums, and what are they called?

### Takeaway
Most A-tier festivals run a market or co-production forum. In 2026 TIFF added a formal **film market** at the Metro Toronto Convention Centre [V]. All other market names below are [BG] and stable, but not re-verified this session.

### Cited Findings
- TIFF launched a new film market in 2026 at the Metro Toronto Convention Centre. — [Wikipedia: 2026 TIFF](https://en.wikipedia.org/wiki/2026_Toronto_International_Film_Festival) [V]
- IDFA runs IDFA Forum (co-financing) alongside IDFA Docs for Sale. — [IDFA Professionals](https://professionals.idfa.nl/markets/co-producing-co-financing/attend-idfa-forum/) [V, from page title]
- Market and forum names [BG]; check each on its official site (URLs in the master table):

| Festival | Market / forum / lab |
|---|---|
| Cannes | Marché du Film (incl. Cannes Docs, Cannes Next, Producers Network); La Fabrique Cinéma |
| Berlin | European Film Market (EFM); Berlinale Co-Production Market; Berlinale Talents; World Cinema Fund |
| Venice | Venice Production Bridge (Gap-Financing Market, Book Adaptation Rights Market); Biennale College Cinema; Final Cut in Venice |
| TIFF | TIFF Industry Conference; new 2026 film market (above) |
| Sundance | Sundance Institute labs (year-round); informal sales market |
| Locarno | Locarno Pro (Match Me!, Heritage Online, First Look); Open Doors; BaseCamp |
| San Sebastián | Europe-Latin America Co-Production Forum; WIP Latam; WIP Europa; Ikusmira Berriak; Elías Querejeta Zine Eskola |
| Karlovy Vary | KVIFF Eastern Promises Industry Days (Works in Progress, First Cut+) |
| IFFR | CineMart; Rotterdam Lab; Hubert Bals Fund; Rotterdam Pro |
| Annecy | MIFA (Marché International du Film d'Animation) |
| Clermont-Ferrand | Marché du Film Court (Short Film Market) |
| IDFA | IDFA Forum; Docs for Sale; IDFA Bertha Fund |
| CPH:DOX | CPH:FORUM; CPH:CONFERENCE; CPH:MARKET |
| Hot Docs | Hot Docs Forum; Deal Maker; Doc Shop |
| Tallinn Black Nights | Industry@Tallinn & Baltic Event (co-production market, Black Nights Stars) |
| Warsaw | Warsaw Next / CentEast Market |
| Sarajevo | CineLink Co-production Market |
| Thessaloniki | Agora (Crossroads, Agora Docs) |
| Rome | MIA Market (Mercato Internazionale Audiovisivo) |
| Sitges | Sitges Pitchbox |
| Málaga | MAFIZ (Málaga Festival Industry Zone) |
| Mar del Plata | Mar del Plata WIP / Industria |
| BAFICI | BAL – Buenos Aires Lab |
| Guadalajara | Industry/Mercado FICG; Guadalajara Co-production Meeting |
| Morelia | Impulso Morelia (WIP) |
| Cartagena | Encuentros Cartagena / FICCI Industria |
| Havana | Nuevas Miradas (EICTV); Havana Industry Days |
| Festival do Rio | RioMarket |
| Gramado | Gramado Film Market |
| Tribeca | Tribeca X; Tribeca Industry / Through Her Lens |
| SXSW | SXSW Conference & Trade Show (film is part of the wider SXSW event) |
| Ventana Sur (Buenos Aires) | A standalone Latin American market (Marché du Film + INCAA), late Nov/early Dec. Market only, no festival. |

### Inferences
- For the app, model the market as a separate `market` object (name, dates, URL) linked to its festival. Markets such as EFM and the Marché du Film have their own accreditation and fees, separate from the festival's.

### Gaps
- Market 2026 dates and accreditation fees were not verified.

---

## Master festival table (Europe + Americas)

**Columns:** short name, official name, city and country, approximate main-venue lat/long [BG], founding year [BG], typical month, 2026 dates (with source), known 2027 dates, FIAPF 2026 status, top prize, key sections [BG], market (see Q3), main venues [BG], official URL [BG].

Status values are A = FIAPF A-Festival, F = FIAPF accredited, — = not accredited, all per the [FIAPF 2026 PDF](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf).

### Tier 1: top ~25 (full records)

1. **Cannes**: Festival de Cannes.
   - Location: Cannes, France; 43.551, 7.017 (Palais des Festivals). Founded 1946 (first planned 1939).
   - Timing: May; 2026 edition 12–23 May [V: FIAPF/Wikipedia]. 2027 dates: not found.
   - Status: A.
   - Top prize: Palme d'Or.
   - Sections: Competition, Un Certain Regard, Out of Competition, Cannes Premiere, Midnight, Cannes Classics, La Cinef. Independent parallel sections: Directors' Fortnight (Quinzaine des Cinéastes), Critics' Week (Semaine de la Critique), ACID.
   - Market: Marché du Film.
   - Venues: Grand Théâtre Lumière, Salle Debussy, Salle Bazin, Palais K.
   - Official site: https://www.festival-cannes.com. Features are submitted via the festival's own online form (not FilmFreeway) [BG].
   - Attendance: roughly 40,000 accredited professionals [BG, unverified].
2. **Berlinale**: Berlin International Film Festival.
   - Location: Berlin, Germany; 52.509, 13.373 (Berlinale Palast, Potsdamer Platz). Founded 1951.
   - Timing: February; 2026 edition 12–22 Feb [V]. 2027 dates: not found.
   - Status: A.
   - Top prize: Golden Bear.
   - Sections: Competition, Perspectives (since 2024), Berlinale Special, Panorama, Forum, Generation, Berlinale Shorts.
   - Market: EFM, Co-Production Market, Talents.
   - Venues: Berlinale Palast, Zoo Palast, Haus der Berliner Festspiele, Uber Eats Music Hall.
   - Official site: https://www.berlinale.de. Submissions via its own online registration [BG].
   - Attendance: about 330,000 tickets sold in typical recent years [BG, unverified].
3. **Venice**: Mostra Internazionale d'Arte Cinematografica (La Biennale di Venezia).
   - Location: Venice Lido, Italy; 45.406, 12.368 (Palazzo del Cinema). Founded 1932, the oldest film festival.
   - Timing: late Aug to early Sep; 2026 edition 2–12 Sep (83rd) [V]. 2027 dates: not found.
   - Status: A.
   - Top prize: Golden Lion.
   - Sections: Venezia (Competition), Out of Competition, Orizzonti, Orizzonti Extra, Venice Classics, Venice Immersive. Independent: Giornate degli Autori, Settimana Internazionale della Critica.
   - Market: Venice Production Bridge.
   - Venues: Sala Grande, PalaBiennale, Sala Darsena, Sala Casinò.
   - Official site: https://www.labiennale.org/en/cinema. Own submission platform [BG].
4. **TIFF**: Toronto International Film Festival.
   - Location: Toronto, Canada; 43.647, -79.390 (TIFF Lightbox). Founded 1976 (as the Festival of Festivals).
   - Timing: September; 2026 edition 10–20 Sep (51st) [V]. 2027 dates: not found.
   - Status: A (new in 2026).
   - Top prize: People's Choice Award (audience). Juried: Platform Prize.
   - Sections: Gala, Special Presentations, Centrepiece, TIFF Docs, Discovery, Platform, Midnight Madness, Wavelengths, Primetime, Short Cuts, Classics.
   - Market: TIFF Industry, plus the new 2026 market [V].
   - Venues: as listed under Q2 [V].
   - Official site: https://tiff.net. Submissions historically via FilmFreeway, with an early-to-late spring window [BG, unverified].
5. **Sundance**: Sundance Film Festival.
   - Location: Park City, Utah, USA, through 2026 (40.646, -111.498, Eccles Theater); Boulder, Colorado from 2027 [V]. Founded 1978 (as the Utah/US Film Festival); Sundance Institute took it over in 1985.
   - Timing: late January; 2026 edition 22 Jan – 1 Feb [V]. 2027 dates (Boulder): not found.
   - Status: —.
   - Top prize: Grand Jury Prize (US Dramatic).
   - Sections: US Dramatic, US Documentary, World Cinema Dramatic, World Cinema Documentary, NEXT, Premieres, Midnight, Shorts.
   - Market: Institute labs.
   - Venues (Utah era): Eccles, The Ray, Library Center, Egyptian, Salt Lake City venues.
   - Official site: https://festival.sundance.org. Submissions via FilmFreeway [BG]; deadlines Aug–Sep, roughly US$65–130 per feature [BG, unverified].
6. **Locarno**: Locarno Film Festival.
   - Location: Locarno, Switzerland; 46.169, 8.795 (Piazza Grande). Founded 1946.
   - Timing: August; 2026 edition 5–15 Aug (79th) [V]. 2027 dates: not found.
   - Status: A.
   - Top prize: Pardo d'oro (Golden Leopard).
   - Sections: Piazza Grande (8,000-seat open air) [BG], Concorso internazionale, Concorso Cineasti del presente, Pardi di domani, Fuori concorso, Histoire(s) du cinéma, Retrospettiva.
   - Market: Locarno Pro.
   - Venues: Piazza Grande, PalaCinema, FEVI, GranRex.
   - Official site: https://www.locarnofestival.ch. Own submission platform [BG].
7. **San Sebastián**: Festival Internacional de Cine de Donostia/San Sebastián (Zinemaldia).
   - Location: San Sebastián, Spain; 43.324, -1.979 (Kursaal). Founded 1953.
   - Timing: September; 2026 edition 18–26 Sep (74th) [V: FIAPF]. 2027 dates: not found.
   - Status: A.
   - Top prize: Golden Shell (Concha de Oro).
   - Sections: Official Section, New Directors, Horizontes Latinos, Zabaltegi-Tabakalera, Perlak, Culinary Zinema, Velódromo.
   - Market: Co-Production Forum, WIP.
   - Venues: Kursaal, Teatro Victoria Eugenia, Principal, Príncipe, Tabakalera, Velódromo Antonio Elorza.
   - Official site: https://www.sansebastianfestival.com. Own platform [BG].
8. **KVIFF**: Karlovy Vary International Film Festival.
   - Location: Karlovy Vary, Czechia; 50.224, 12.883 (Hotel Thermal). Founded 1946.
   - Timing: early July; 2026 edition 3–11 Jul (60th) [V]. **2027 edition 2–10 Jul** [V].
   - Status: A.
   - Top prize: Crystal Globe.
   - Sections: Crystal Globe Competition, Proxima, Special Screenings, Horizons, Imagina.
   - Market: Eastern Promises.
   - Venues: Hotel Thermal (Grand Hall), Lázně III, Pupp, Čas.
   - Official site: https://www.kviff.com [V].
9. **IFFR**: International Film Festival Rotterdam.
   - Location: Rotterdam, Netherlands; 51.920, 4.474 (De Doelen). Founded 1972.
   - Timing: late Jan to early Feb; 2026 edition (55th) dates not verified. 2027 dates: not found.
   - Status: —.
   - Top prize: Tiger Award (€40k) [V].
   - Sections: Tiger Competition, Big Screen Competition, Harbour, Limelight, Bright Future, Short & Mid-length, Art Directions.
   - Market: CineMart, Hubert Bals Fund.
   - Venues: De Doelen, Pathé Schouwburgplein, LantarenVenster, KINO.
   - Official site: https://iffr.com [V].
   - Attendance: around 300,000 visits [BG, unverified].
10. **Annecy**: Festival International du Film d'Animation d'Annecy.
    - Location: Annecy, France; 45.901, 6.127 (Bonlieu). Founded 1960.
    - Timing: June; 2026 edition 21–27 Jun [V: FIAPF]. 2027 dates: not found.
    - Status: A (new in 2026).
    - Top prize: Cristal du long métrage.
    - Sections: Official Feature, Contrechamp, Shorts, Perspectives, Off-Limits, TV & Commissioned, Graduation.
    - Market: MIFA.
    - Venues: Bonlieu, Pathé Annecy, Décavision, open-air Pâquier.
    - Official site: https://www.annecyfestival.com. Submissions via its own online platform [BG].
11. **Clermont-Ferrand**: Festival International du Court Métrage de Clermont-Ferrand.
    - Location: Clermont-Ferrand, France; 45.776, 3.085 (Maison de la Culture). Founded 1979 (international since 1982).
    - Timing: late Jan to early Feb; 2026 edition 30 Jan – 7 Feb [V: FIAPF]. 2027 dates: not found.
    - Status: A (new in 2026).
    - Top prize: Grand Prix, in each of the International, National and Lab competitions.
    - Market: Marché du Film Court.
    - Venues: Maison de la Culture (Jean Cocteau hall), Cinéma Capitole.
    - Official site: https://www.clermont-filmfest.org. Own online platform; free entry [BG].
    - Attendance: about 160,000 admissions [BG, unverified].
12. **Tallinn Black Nights (PÖFF)**: Pimedate Ööde Filmifestival.
    - Location: Tallinn, Estonia; 59.437, 24.753. Founded 1997.
    - Timing: November; 2026 edition 6–22 Nov [V: FIAPF]. 2027 dates: not found.
    - Status: A.
    - Top prize: Grand Prix for Best Film (Official Selection).
    - Sections: Official Selection, First Feature, Critics' Picks, Rebels with a Cause, Just Film (youth), PÖFF Shorts.
    - Market: Industry@Tallinn & Baltic Event.
    - Venues: Coca-Cola Plaza, Solaris Kino.
    - Official site: https://poff.ee.
13. **Warsaw IFF**: Warszawski Międzynarodowy Festiwal Filmowy.
    - Location: Warsaw, Poland; 52.230, 21.003 (Kinoteka, Palace of Culture). Founded 1985.
    - Timing: October; 2026 edition 9–18 Oct [V: FIAPF]. 2027 dates: not found.
    - Status: A.
    - Top prize: Warsaw Grand Prix.
    - Sections: International Competition, Competition 1-2, Free Spirit, Documentary, Shorts.
    - Market: CentEast / Warsaw Next.
    - Official site: https://wff.pl.
14. **Mar del Plata (MDQ)**: Festival Internacional de Cine de Mar del Plata.
    - Location: Mar del Plata, Argentina; -38.001, -57.541 (Teatro Auditorium). Founded 1954; the only A-festival in Latin America.
    - Timing: November; 2026 edition 5–15 Nov (41st) [V]. 2027 dates: not found.
    - Status: A.
    - Top prize: Astor de Oro / Astor Piazzolla award.
    - Sections: International, Latin American and Argentine competitions; Estados Alterados; Autores.
    - Market: MdP Industria / WIP.
    - Venues: Teatro Auditorium, Paseo Aldrey, Cines del Paseo.
    - Official site: https://www.mardelplatafilmfest.com.
15. **Tribeca**: Tribeca Festival.
    - Location: New York, USA; 40.719, -74.010 (Spring Studios / Tribeca). Founded 2002 by Robert De Niro, Jane Rosenthal and Craig Hatkoff.
    - Timing: June; 2026 edition 3–14 Jun (25th) [V: Tribeca press center]. 2027 dates: not found.
    - Status: —.
    - Top prize: Founders Award for Best US Narrative Feature [BG].
    - Sections: US Narrative, International Narrative, Documentary, Viewpoints, Spotlight Narrative and Documentary, Midnight, Escape from Tribeca, Tribeca Immersive, Games, TV.
    - Market: Tribeca X / industry.
    - Official site: https://tribecafilm.com. Submissions via FilmFreeway, with a Sep–Jan window [BG, unverified].
16. **SXSW Film & TV**: SXSW Film & TV Festival.
    - Location: Austin, Texas, USA; 30.265, -97.739 (Paramount Theatre). Founded 1987; film strand since 1994.
    - Timing: March. 2026 and 2027 dates: not verified.
    - Status: —.
    - Top prize: Grand Jury Award (Narrative and Documentary Feature competitions).
    - Sections: Narrative Competition, Documentary Competition, Headliners, Narrative Spotlight, Documentary Spotlight, Visions, Midnighters, 24 Beats per Second, Festival Favorites.
    - Venues: Paramount, Alamo Lamar, Zach Theatre.
    - Official site: https://www.sxsw.com/festivals/film. Submissions via its own system or FilmFreeway [BG, unverified].
17. **Telluride**: Telluride Film Festival.
    - Location: Telluride, Colorado, USA; 37.938, -107.812 (Werner Herzog Theatre). Founded 1974.
    - Timing: Labor Day weekend; 2026 edition 4–7 Sep (53rd) [secondary source: Italy Meets Hollywood; the lineup announced on 3 Sep per Screen Daily]. 2027 dates: not found.
    - Status: —. Non-competitive; lineup unannounced until the day before.
    - Top prize: none (Silver Medallion tributes).
    - Official site: https://telluridefilmfestival.org.
18. **NYFF**: New York Film Festival (Film at Lincoln Center).
    - Location: New York, USA; 40.773, -73.983 (Alice Tully Hall). Founded 1963.
    - Timing: late Sep to Oct. 2026 dates: not verified.
    - Status: —. Non-competitive.
    - Sections: Main Slate, Currents, Spotlight, Revivals.
    - Venues: Alice Tully Hall, Walter Reade Theater, Francesca Beale and Elinor Bunin Munroe theaters.
    - Official site: https://www.filmlinc.org/nyff.
19. **BFI LFF**: BFI London Film Festival.
    - Location: London, UK; 51.507, -0.115 (BFI Southbank). Founded 1957.
    - Timing: October; 2026 edition 7–18 Oct (70th) [V: ICA listing and BFI pages]. 2027 dates: not found.
    - Status: —.
    - Top prize: Best Film (Official Competition).
    - Sections: Galas, Official, First Feature and Documentary Competitions, Love, Debate, Laugh, Dare, Thrill, Cult, Journey, Create, Family, Experimenta, Treasures.
    - Venues: BFI Southbank, Royal Festival Hall, Odeon Luxe Leicester Square, BFI IMAX, ICA, Prince Charles Cinema.
    - Official site: https://www.bfi.org.uk/london-film-festival. Submissions via the BFI's own form [BG].
20. **IDFA**: International Documentary Film Festival Amsterdam.
    - Location: Amsterdam, Netherlands; 52.364, 4.884 (Tuschinski / Eye area). Founded 1988.
    - Timing: November; 2026 edition 12–22 Nov [V: IDFA site]. 2027 dates: not found.
    - Status: —.
    - Top prize: Award for Best Film (International Competition).
    - Sections: International, Envision, Feature-Length Dutch, Short and Mid-length, Youth, DocLab (immersive), Best of Fests, Frontlight.
    - Market: IDFA Forum, Docs for Sale.
    - Venues: Tuschinski, Eye Filmmuseum, De Balie, Rialto, Carré.
    - Official site: https://festival.idfa.nl [V].
21. **CPH:DOX**: Copenhagen International Documentary Film Festival.
    - Location: Copenhagen, Denmark; 55.676, 12.568 (Kulturhuset Islands Brygge / Grand Teatret). Founded 2003.
    - Timing: March. 2026 dates: not verified.
    - Status: —.
    - Top prize: DOX:AWARD.
    - Sections: DOX:AWARD, NEW:VISION, F:ACT, Next:Wave, Nordic:Dox, HUMAN:RIGHTS.
    - Market: CPH:FORUM, CPH:CONFERENCE.
    - Official site: https://cphdox.dk [V].
22. **Hot Docs**: Hot Docs Canadian International Documentary Festival.
    - Location: Toronto, Canada; 43.665, -79.411 (Hot Docs Ted Rogers Cinema). Founded 1993.
    - Timing: late April to early May; 2026 edition 23 Apr – 3 May [V: FIAPF]. 2027 dates: not found.
    - Status: F (new in 2026).
    - Top prize: Best International Feature Documentary.
    - Market: Hot Docs Forum, Deal Maker.
    - Official site: https://hotdocs.ca. Submissions via FilmFreeway [BG, unverified].
23. **Morelia (FICM)**: Festival Internacional de Cine de Morelia.
    - Location: Morelia, Mexico; 19.703, -101.193 (Teatro Morelos / Cinépolis Centro). Founded 2003.
    - Timing: October; 2026 edition was the 24th, ending around 23–25 Oct [V: Chilango]. 2027 dates: not found.
    - Status: —.
    - Top prize: Ojo (Best Mexican Feature).
    - Sections: Mexican Feature, Mexican Documentary, Mexican Short, Michoacán Section, Out of competition.
    - Market: Impulso Morelia.
    - Official site: https://moreliafilmfest.com.
24. **FICG**: Festival Internacional de Cine en Guadalajara.
    - Location: Guadalajara, Mexico; 20.674, -103.344 (Conjunto Santander de Artes Escénicas, UdeG). Founded 1986.
    - Timing: April (it was June in some years); 2026 was the 41st edition, held in April [V: Infobae, 18 Apr 2026 coverage]. Exact 2026 dates not verified; 2027 dates not found.
    - Status: —.
    - Top prize: Premio Mezcal / Premio Maguey; main prize is Best Ibero-American Feature (Premio Guadalajara) [BG].
    - Market: FICG industry / Co-production Meeting.
    - Official site: https://www.ficg.mx.
25. **FICCI**: Festival Internacional de Cine de Cartagena de Indias.
    - Location: Cartagena, Colombia; 10.423, -75.551 (Teatro Adolfo Mejía / Walled City). Founded 1960, the oldest in Latin America.
    - Timing: March or April; 2026 edition 14–19 Apr (65th) [V: Diario del Sur headline]. **2027: 66th edition announced, starting 6 Apr 2027** [Festhome listing; Diario del Sur]. FICCI 66 submission call is open [FICCI bases PDF](https://ficcifestival.com/sites/default/files/2026-08/FICCI66%20_%20Bases_de_Participaci%C3%B3n_ESP.pdf).
    - Status: —.
    - Top prize: India Catalina / Best Film awards.
    - Market: Encuentros Cartagena.
    - Official site: https://ficcifestival.com [V].
    - Attendance: 2026 closed with more than 65,000 attendees [V: La República headline](https://www.larepublica.co/ocio/ficci-cerro-edicion-con-mas-de-65-000-asistentes-4382776).
26. **Havana**: Festival Internacional del Nuevo Cine Latinoamericano.
    - Location: Havana, Cuba; 23.138, -82.382 (Cine Charles Chaplin). Founded 1979.
    - Timing: December; 2026 edition 3–13 Dec (47th) [V: News in America](https://newsinamerica.com/pdcc/boletin/2026/abre-convocatoria-la-edicion-47-del-festival-internacional-del-nuevo-cine-latinoamericano/). 2027 dates: not found.
    - Status: —.
    - Top prize: Gran Premio Coral.
    - Market: Nuevas Miradas.
    - Venues: Charles Chaplin, Yara, Karl Marx, La Rampa.
    - Official site: https://habanafilmfestival.com.
27. **Gramado**: Festival de Cinema de Gramado.
    - Location: Gramado, Brazil; -29.379, -50.875 (Palácio dos Festivais). Founded 1973.
    - Timing: August; 2026 edition was the 54th, with awards around 22–23 Aug [V: O Hoje]. 2027 dates: not found.
    - Status: —.
    - Top prize: Kikito for Best Film.
    - Market: Gramado Film Market.
    - Official site: https://www.festivaldegramado.net.
28. **Festival do Rio**: Rio de Janeiro International Film Festival.
    - Location: Rio de Janeiro, Brazil; -22.97 (Odeon, Cinelândia; area coordinates). Founded 1999, from the merger of Mostra Banco Nacional and Rio Cine.
    - Timing: October. 2026 dates: not verified.
    - Status: —.
    - Top prize: Troféu Redentor.
    - Market: RioMarket.
    - Official site: https://www.festivaldorio.com.br.
29. **BAFICI**: Buenos Aires Festival Internacional de Cine Independiente.
    - Location: Buenos Aires, Argentina; -34.603, -58.384. Founded 1999.
    - Timing: April; 2026 edition (27th) in April, with winners announced around 27 Apr [V: Buenos Aires city government](https://buenosaires.gob.ar/gcaba_historico/noticias/bafici-se-anunciaron-los-ganadores-y-la-gran-premiada-llega-este-jueves-al). 2027 dates: not found.
    - Status: —.
    - Top prize: Best Film (International Competition).
    - Market: BAL.
    - Official site: https://bafici.org [V].

### Tier 2: other significant festivals (core fields)

Format: short name, full name (where needed): city, country; founded [BG]; typical month; 2026 dates where verified; FIAPF status; top prize [BG]; URL [BG].

**Europe**
- **Málaga**: Spain; founded 1998; March; 6–15 Mar 2026 [V]; F; Biznaga de Oro; https://festivaldemalaga.com
- **Sitges**: Sitges, Spain; founded 1968; October; 8–18 Oct 2026 [V]; F; Best Film (Fantàstic); https://sitgesfilmfestival.com
- **Gijón (FICX)**: Gijón, Spain; founded 1963; November; 13–21 Nov 2026 [V]; F; Best Feature (Albar/Grand Prix); https://gijonfilmfestival.com
- **Punto de Vista**: Pamplona, Spain; founded 2005; April (dates may vary); 20–25 Apr 2026 [V]; F (new); Gran Premio Punto de Vista; https://www.puntodevistafestival.com
- **Cinema Jove**: Valencia, Spain; founded 1986; June; 19–27 Jun 2026 [V]; F; Luna de Valencia; https://cinemajove.com
- **Mostra de València**: Valencia, Spain; November; 5–15 Nov 2026 [V]; F; Palmera d'Or; https://mostravalencia.com
- **Zinebi**: Bilbao, Spain; founded 1959; November; 20–27 Nov 2026 [V]; F; Mikeldi de Oro; https://zinebi.eus
- **Seville European Film Festival**: Seville, Spain; November; —; Giraldillo de Oro; https://festivaldesevilla.eu
- **Rome Film Fest**: Rome, Italy; founded 2006; October; 14–25 Oct 2026 [V]; F; Best Film (Progressive Cinema); Auditorium Parco della Musica; https://www.romacinemafest.it
- **Torino**: Turin, Italy; founded 1982; November; 24 Nov – 2 Dec 2026 [V]; F; Best Film; https://www.torinofilmfest.org
- **Noir in Festival**: Milan and Como, Italy; December; TBA [V]; F; Black Panther award; https://www.noirfest.com
- **Viennale**: Vienna, Austria; founded 1960; October; 22 Oct – 3 Nov 2026 [V]; F; mostly non-competitive; Gartenbaukino; https://www.viennale.at
- **Kitzbühel FF**: Austria; August; TBA [V]; F; https://filmfestival-kitzbuehel.com
- **Oberhausen**: Oberhausen, Germany; founded 1954; April–May; 28 Apr – 3 May 2026 [V]; F; Grand Prize of the City of Oberhausen; Lichtburg Filmpalast; https://www.kurzfilmtage.de
- **Hof, DOK Leipzig, Munich FFM, Hamburg**: Germany; all —. DOK Leipzig (founded 1955, October/November, Golden Dove) [BG]; https://www.dok-leipzig.de
- **Tampere**: Tampere, Finland; founded 1969; March; 4–8 Mar 2026 [V]; F; Grand Prix (short); https://tamperefilmfestival.fi
- **Göteborg**: Gothenburg, Sweden; founded 1979; Jan–Feb; —; Dragon Award Best Nordic Film; Nordic Film Market; https://goteborgfilmfestival.se
- **Stockholm IFF**: Sweden; founded 1990; November; — (absent from the 2026 FIAPF list); Bronze Horse; https://www.stockholmfilmfestival.se
- **Sofia IFF**: Sofia, Bulgaria; founded 1997; March; 12–22 Mar 2026 [V]; F; Grand Prix; Sofia Meetings; https://siff.bg
- **Krakow FF**: Kraków, Poland; founded 1961; May–June; 31 May – 7 Jun 2026 [V]; F; Golden Dragon (doc/short/animation); https://www.krakowfilmfestival.pl
- **New Horizons (Nowe Horyzonty)**: Wrocław, Poland; founded 2001; July; —; https://www.nowehoryzonty.pl
- **Gdynia (Polish Film Festival)**: Poland; September; —; Golden Lions
- **TIFF Transilvania**: Cluj-Napoca, Romania; founded 2002; June; 12–21 Jun 2026 [V]; F; Transilvania Trophy; https://tiff.ro
- **Sarajevo FF**: Sarajevo, Bosnia and Herzegovina; founded 1995; August; —; Heart of Sarajevo; CineLink; https://www.sff.ba
- **Herceg Novi FF**: Montenegro; August; 22–28 Aug 2026 [V]; F (new); Golden Mimosa; https://www.hercegfest.co.me
- **Cinedays**: Skopje, North Macedonia; dates TBA [V]; F
- **Motovun FF**: Croatia; July; —
- **Pula FF**: Croatia; July; —; Golden Arena
- **Thessaloniki IFF**: Thessaloniki, Greece; founded 1960; November; — (not in the 2026 PDF); Golden Alexander; Agora market; https://www.filmfestival.gr. Its separate documentary festival runs in March.
- **Molodist**: Kyiv, Ukraine; founded 1970; dates TBA [V]; F; Scythian Deer; https://molodist.com
- **Golden Apricot**: Yerevan, Armenia; founded 2004; July; 12–19 Jul 2026 [V]; F (new); Golden Apricot; https://www.gaiff.am
- **Antalya Golden Orange**: Antalya, Türkiye; founded 1963; October; TBA [V]; F; Golden Orange; https://antalyaff.com
- **Istanbul IFF**: Türkiye; April; —; Golden Tulip; https://film.iksv.org
- **Ji.hlava IDFF**: Jihlava, Czechia; founded 1997; October; —; doc
- **Visions du Réel**: Nyon, Switzerland; founded 1969; April; —; doc; Sesterce d'or; VdR-Industry; https://www.visionsdureel.ch
- **Zurich FF (ZFF)**: Zurich, Switzerland; founded 2005; Sep–Oct; —; Golden Eye; https://zff.com
- **Edinburgh IFF**: Edinburgh, UK; founded 1947; August; —; https://www.edfilmfest.org
- **Sheffield DocFest**: Sheffield, UK; founded 1994; June; —; doc; Grand Jury Award; MeetMarket; https://www.sheffdocfest.com
- **Cork IFF**: Ireland; founded 1956; November; —; https://corkfilmfest.org
- **Galway Film Fleadh**: Ireland; July; —
- **Deauville American Film Festival**: Deauville, France; founded 1975; September; —; Grand Prix; https://festival-deauville.com
- **Cinéma du Réel**: Paris, France; March; —; doc
- **Lyon Lumière Festival**: Lyon, France; founded 2009; October; —; classics, Prix Lumière; Marché International du Film Classique; https://www.festival-lumiere.org
- **Les Arcs**: France; December; —; Coproduction Village
- **Gérardmer**: France; January; —; fantastic genre
- **Series Mania**: Lille, France; March. TV, not film.
- **FEST Belgrade**: Serbia; February–March; —
- **Riga IFF, Vilnius Kino Pavasaris, Reykjavík RIFF, Bergen, Haugesund (Norwegian IFF, with the New Nordic Films market), Odense (short film)**: all —; regional
- **European Film Awards**: not a festival. The ceremony is held in December (Berlin in alternate years) [BG].

**North America**
- **Festival du Nouveau Cinéma (FNC)**: Montréal, Canada; founded 1971; October; 7–18 Oct 2026 [V]; F (new); Louve d'Or; https://nouveaucinema.ca
- **Fantasia**: Montréal, Canada; founded 1996; July–August; —; genre; Frontières market; https://fantasiafestival.com
- **VIFF**: Vancouver, Canada; founded 1982; Sep–Oct; —; https://viff.org
- **Calgary, Whistler, RIDM (Montréal doc), Rendez-vous Québec Cinéma**: all —
- **Fantastic Fest**: Austin, Texas, USA; founded 2005; September; 17–24 Sep 2026 [V]; F; Alamo Drafthouse South Lamar; https://fantasticfest.com
- **AFI Fest**: Los Angeles, USA; founded 1971; October–November; —; TCL Chinese Theatre; https://fest.afi.com
- **Chicago IFF**: Chicago, USA; founded 1964; October; —; Gold Hugo; https://www.chicagofilmfestival.com
- **Seattle IFF (SIFF)**: Seattle, USA; founded 1976; May; —; https://www.siff.net
- **Palm Springs IFF**: Palm Springs, USA; founded 1989; January; —; https://www.psfilmfest.org
- **Mill Valley FF**: Mill Valley, USA; October; —
- **Savannah FF**: Savannah, USA; October–November; —
- **Hamptons IFF**: East Hampton, USA; October; —
- **SFFILM (San Francisco IFF)**: San Francisco, USA; founded 1957; April; —; https://sffilm.org
- **True/False**: Columbia, Missouri, USA; March; —; doc
- **Full Frame**: Durham, North Carolina, USA; April; —; doc
- **DOC NYC**: New York, USA; November; —; doc; https://www.docnyc.net
- **Slamdance**: Park City historically, moved to Los Angeles from 2026 [BG, unverified]; January; —; https://slamdance.com
- **Outfest**: Los Angeles, USA; July; —; LGBTQ+
- **Los Cabos IFF**: Mexico; November–December; —; status irregular in recent years [BG, unverified]
- **FICUNAM**: Mexico City, Mexico; March; —
- **Ambulante**: Mexico, touring; spring; —; doc
- **Guanajuato IFF (GIFF)**: Mexico; July; —
- **Monterrey**: Mexico; August; —
- **Shorts Mexico**: Mexico; —

**Central America and Caribbean**
- **Festival de Cine Global Santo Domingo**: Santo Domingo, Dominican Republic; founded 2006; January–February; 28 Jan – 4 Feb 2026 [V]; F; https://festivaldecineglobal.org
- **Panama IFF (IFF Panamá)**: Panama City, Panama; founded 2012; April; —; status irregular [BG]
- **Icaro (Central American festival)**: Guatemala; November; —
- **Costa Rica IFF (CRFIC)**: San José, Costa Rica; —
- **Puerto Rico, Trinidad & Tobago FF (ttff)**: Port of Spain; September; —
- **Havana**: see Tier 1 #26.

**South America**
- **Festival Internacional de Cine de Valdivia (FICValdivia)**: Valdivia, Chile; founded 1994; October; —; https://ficvaldivia.cl
- **Sanfic (Santiago IFF)**: Santiago, Chile; August; —; Sanfic Industria
- **Lima Film Festival (Festival de Cine de Lima PUCP)**: Lima, Peru; founded 1997; August; —; Trofeo Spondylus
- **FICCI**: see Tier 1 #25.
- **Bogotá (BIFF)**: Bogotá, Colombia; October; —
- **São Paulo International Film Festival (Mostra de São Paulo)**: São Paulo, Brazil; founded 1977; October–November; —; Bandeira Paulista; https://mostra.org
- **É Tudo Verdade / It's All True**: São Paulo and Rio, Brazil; founded 1996; April; —; doc; Oscar-qualifying [BG]
- **Brasília Festival of Brazilian Cinema**: Brasília, Brazil; founded 1965; —; Troféu Candango
- **Mostra de Tiradentes**: Brazil; January; —
- **Punta del Este IFF**: Uruguay; —
- **Cinema Uruguay / FICU (Montevideo)**: Uruguay; April; —
- **Bolivia, Ecuador (EDOC), Venezuela (Mérida)**: regional; —

---

## Notes for the app loader
- Fields marked [BG] (founding year, venues, coordinates, URLs, section names, market names) are stable and well documented, but should go through an automated check (URL check, geocoding) before release.
- Submission fees and deadlines are **not** in these notes as verified data. Sundance, Tribeca, Hot Docs and many US and Canadian festivals use FilmFreeway [BG]. Cannes, Berlin, Venice, Locarno, San Sebastián, Annecy and Clermont-Ferrand use their own portals [BG]. Pull live values from the FilmFreeway pages.
- 2027 dates found so far: KVIFF 2–10 Jul 2027 [V]; FICCI starting 6 Apr 2027 (66th) [V, secondary]; Sundance moving to Boulder, Colorado in 2027 [V, dates not found].
