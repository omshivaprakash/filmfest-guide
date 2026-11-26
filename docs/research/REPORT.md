# Mapping the World's Film Festivals for a Guide

The world's film festival circuit can be mapped, but no single open source covers it. **FIAPF's 2026 reform cut its accreditation down to one list of 49 festivals in 29 countries, and 17 of them now carry a revived "A-Festival" mark.** That list, Wikidata's roughly 16,000 festival items, the Academy/BAFTA/EFA qualifying lists and each festival's own website together make a workable backbone for a worldwide guide ([FIAPF 2026 calendar](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf); [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)). In India, **IFFI Goa is the only A-Festival**. BIFFes, KIFF and IFFK are accredited without the mark. IFFI's 57th edition is under way (20–28 Nov 2026), IFFK's 31st runs 11–18 Dec 2026, and BIFFes' 17th ran 29 Jan–6 Feb 2026 ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2335780&reg=48&lang=2); [Indian Opinion](https://indianopinion.org/iffk-31-delegate-registration-opens-14-films-in-competition); [Deccan Herald](https://www.deccanherald.com/india/karnataka/bengaluru/17th-biffes-to-be-held-from-january-29-and-february-6-over-200-films-to-be-screened-3840527)). Most 2026 top prizes are settled: Cannes went to *Fjord*, Berlin to *Yellow Letters*, Venice to *Woman Unknown* and Busan to *Midday Meal*. Three results are still open as of 26 Nov 2026: IFFI (closes 28 Nov), Marrakech (closes 28 Nov) and IFFK (December). Red Sea's 2026 edition was postponed to Q4 2027, and FESPACO is biennial, so neither has 2026 winners. For engineering, two points matter most. First, accreditation, location and status belong to each *edition*, not to the festival, because FIAPF status, venues (Sundance moves to Boulder in 2027) and cancellations (Red Sea) all change from year to year. Second, every field in the tables below carries a reliability tag, and many stable-looking fields (founding years, venues, coordinates, URLs) are **unverified background knowledge** that has to pass an automated check before launch.

**Reliability legend used in every table.** **[V]** = verified this session (Nov 2026) from the cited page. **[S]** = seen only in a search snippet or headline, so the claim is real but the detail is thin. **[BG]** = background or reference knowledge (training data to about mid-2026) that was **not re-checked**. Treat it as a lead and confirm it on the linked official site before publishing. All latitude/longitude values are approximate (about 3 decimals) and **[BG]**. The verification date for [V] is 26 Nov 2026. Submission fees and deadlines were **not verified** for any festival.

## FIAPF's 2026 reform shrank accreditation to 49 festivals and revived the "A" mark

FIAPF represents 38 national producers' organisations from 31 countries. In 2026 it ran its biggest accreditation reform since 2007: it dropped the old four-category system (competitive feature, competitive specialised, non-competitive, documentary/short) for **one unified accredited list**, and reintroduced the "A" classification about 20 years after it was abandoned ([Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)). The new criteria are measurable. They cover film selection (submissions and the share of non-native entries), industry activity (professional attendees, journalists, press coverage) and audience data (admissions, occupancy, audience-development strategy). Festivals report the figures voluntarily and FIAPF publishes them. Six festivals were newly accredited: Golden Apricot, Herceg Novi, FNC Montréal, Hot Docs, Annecy and Punto de Vista. Four more from under-represented regions were promised "later this year" but not confirmed by November. **Two discrepancies need care when loading.** First, Screen Daily's own table ticks 22 festivals in its "A-List" column while its text names 17; the FIAPF PDF asterisks only 17, so **the PDF is authoritative**. Second, an older FIAPF web page still lists 14 "competitive feature film festivals", which reflects the superseded taxonomy ([FIAPF competitive page](https://fiapf.org/festivals/accredited-festivals/competitive-feature-film-festivals/)).

For the data model this means **the old category field is obsolete**. Store `fiapf_accredited` and `fiapf_a_festival` as booleans **per edition year**. Prestige should also be ranked separately from FIAPF status. Sundance, Rotterdam, Tribeca, SXSW, Telluride, NYFF, BFI London, IDFA, CPH:DOX, Red Sea, Marrakech, Hong Kong, Golden Horse and FESPACO are all absent from the list, yet several are more influential than many accredited festivals. Do not tag Moscow, Thessaloniki, Stockholm or Bratislava as FIAPF festivals for 2026: they are absent from the PDF. Their earlier status is [BG].

### Table 1. FIAPF 2026 accredited festivals (all 49) [V]

Source for every row: [FIAPF 2026 calendar PDF, dated 11 Mar 2026](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf). The PDF gives no cities, so city values are [BG]. "New" = newly accredited in 2026 per Screen Daily.

| # | Festival | City [BG] | Country | 2026 dates (FIAPF) | A-Festival | Region |
|---|---|---|---|---|---|---|
| 1 | Festival de Cine Global Santo Domingo | Santo Domingo | Dominican Rep. | 28 Jan–4 Feb | | Americas |
| 2 | Bengaluru IFF (BIFFes) | Bengaluru | India | 29 Jan–6 Feb | | India |
| 3 | Clermont-Ferrand Int'l Short FF | Clermont-Ferrand | France | 30 Jan–7 Feb | ★ | Europe |
| 4 | Berlinale | Berlin | Germany | 12–22 Feb | ★ | Europe |
| 5 | Tampere FF | Tampere | Finland | 4–8 Mar | | Europe |
| 6 | Málaga FF | Málaga | Spain | 6–15 Mar | | Europe |
| 7 | Sofia IFF | Sofia | Bulgaria | 12–22 Mar | | Europe |
| 8 | Punto de Vista | Pamplona | Spain | 20–25 Apr | (new) | Europe |
| 9 | Hot Docs | Toronto | Canada | 23 Apr–3 May | (new) | Americas |
| 10 | Oberhausen Int'l Short FF | Oberhausen | Germany | 28 Apr–3 May | | Europe |
| 11 | Festival de Cannes | Cannes | France | 12–23 May | ★ | Europe |
| 12 | Kraków FF | Kraków | Poland | 31 May–7 Jun | | Europe |
| 13 | Sydney FF | Sydney | Australia | 3–14 Jun | | Asia-Pacific |
| 14 | Shanghai IFF | Shanghai | China | 12–21 Jun | ★ | Asia-Pacific |
| 15 | Transilvania IFF | Cluj-Napoca | Romania | 12–21 Jun | | Europe |
| 16 | Cinema Jove | Valencia | Spain | 19–27 Jun | | Europe |
| 17 | Annecy Int'l Animation FF | Annecy | France | 21–27 Jun | ★ (new) | Europe |
| 18 | Karlovy Vary IFF | Karlovy Vary | Czechia | 3–11 Jul | ★ | Europe |
| 19 | Golden Apricot Yerevan IFF | Yerevan | Armenia | 12–19 Jul | (new) | Europe/Asia |
| 20 | Cinedays | Skopje | North Macedonia | TBA | | Europe |
| 21 | Locarno FF | Locarno | Switzerland | 5–15 Aug | ★ | Europe |
| 22 | Herceg Novi FF | Herceg Novi | Montenegro | 22–28 Aug | (new) | Europe |
| 23 | Venice IFF (Mostra) | Venice Lido | Italy | 2–12 Sep | ★ | Europe |
| 24 | Toronto IFF (TIFF) | Toronto | Canada | 10–20 Sep | ★ | Americas |
| 25 | Fantastic Fest | Austin | USA | 17–24 Sep | | Americas |
| 26 | San Sebastián IFF | San Sebastián | Spain | 18–26 Sep | ★ | Europe |
| 27 | Eurasia IFF | Almaty/Astana | Kazakhstan | TBA | | Asia |
| 28 | Busan IFF | Busan | South Korea | 6–15 Oct | ★ | Asia-Pacific |
| 29 | Festival du Nouveau Cinéma | Montréal | Canada | 7–18 Oct | (new) | Americas |
| 30 | Sitges Int'l Fantastic FF | Sitges | Spain | 8–18 Oct | | Europe |
| 31 | Warsaw IFF | Warsaw | Poland | 9–18 Oct | ★ | Europe |
| 32 | Rome Film Fest | Rome | Italy | 14–25 Oct | | Europe |
| 33 | Viennale | Vienna | Austria | 22 Oct–3 Nov | | Europe |
| 34 | Tokyo IFF | Tokyo | Japan | 26 Oct–4 Nov (Screen: 28 Oct) | ★ | Asia-Pacific |
| 35 | Molodist Kyiv IFF | Kyiv | Ukraine | TBA | | Europe |
| 36 | Mar del Plata IFF | Mar del Plata | Argentina | 5–15 Nov | ★ | Americas |
| 37 | Mostra de València | Valencia | Spain | 5–15 Nov | | Europe |
| 38 | Kitzbühel FF | Kitzbühel | Austria | TBA | | Europe |
| 39 | Kolkata IFF (KIFF) | Kolkata | India | TBA | | India |
| 40 | Antalya Golden Orange | Antalya | Türkiye | TBA | | Europe/Asia |
| 41 | Tallinn Black Nights (PÖFF) | Tallinn | Estonia | 6–22 Nov | ★ | Europe |
| 42 | Cairo IFF | Cairo | Egypt | 11–20 Nov | ★ | Middle East/Africa |
| 43 | Gijón/Xixón IFF (FICX) | Gijón | Spain | 13–21 Nov | | Europe |
| 44 | IFFI Goa | Panaji | India | 20–28 Nov | ★ | India |
| 45 | Zinebi | Bilbao | Spain | 20–27 Nov | | Europe |
| 46 | Torino FF | Turin | Italy | 24 Nov–2 Dec | | Europe |
| 47 | Fajr IFF | Tehran | Iran | TBA | | Middle East |
| 48 | IFFK Kerala | Thiruvananthapuram | India | TBA | | India |
| 49 | Noir in Festival | Milan/Como | Italy | TBA | | Europe |

## Oscar, BAFTA and EFA lists outrank FIAPF for specialised festivals

For shorts, documentaries and animation, Oscar, BAFTA and European Film Academy qualifying status carry more weight than FIAPF accreditation. The most recent Academy qualifying list that is public and was fetched is the **98th list**: 172 festival or award bodies for shorts, and 31 international festivals for Documentary Feature, with a winning window of 1 Oct 2024 to 30 Sep 2025 ([AMPAS 98th shorts list](https://www.oscars.org/sites/oscars/files/2024-11/98th_qualifying_festival_list_all_shorts.pdf); [AMPAS 98th combined list](https://oscars.org/sites/oscars/files/2024-10/98_Full_Qualifying_Festival_List_Combined.pdf)). The **99th rules** (published 1 May 2026) set an eligibility year of 1 Jan–31 Dec 2026 and short-film deadlines of 13 Aug and 8 Oct 2026, and they announced no changes to the short or documentary categories, so the 98th list is the best proxy. The 99th rules did add one route: a non-English-language feature can now enter International Feature by winning the Berlin Golden Bear, Busan Award, Palme d'Or, Sundance World Cinema Grand Jury Prize, TIFF Platform Award or Venice Golden Lion ([AMPAS 99th rules](https://press.oscars.org/news/awards-rules-and-campaign-promotional-regulations-approved-99th-oscarsr)). The app should label the AMPAS badge "per 98th list, last verified" until the 99th or 100th PDF is checked.

The Academy codes used below are LA (live action), AN (animated), DOC (documentary short), GEN (award listed simply as "short film") and DF (Documentary Feature). The fetched BAFTA British Short Film list is the **2025-awards version**, which is older ([BAFTA list](https://www.bafta.org/wp-content/uploads/2024/09/british_short_film_qualifying_festivals_list_2025-1.pdf)). Newer BAFTA additions are Curtas Vila do Conde ([Curtas](https://festival.curtas.pt/en/detail-news/curtas-vila-do-conde-is-officially-a-bafta-qualifying-festival/)), Drama ([Indie Shorts Mag](https://www.indieshortsmag.com/news/film-festival/2026/07/drama-international-short-film-festival-becomes-bafta-qualifying-for-british-shorts/)) and Animafilm Baku ([Skwigly](https://www.skwigly.co.uk/animafilm-international-animation-festival-becomes-bafta-qualifying-festival/)). The EFA European Short Film (Prix Vimeo) award runs through **31 network festivals** for the 2026/27 (40th) cycle. Each network festival's jury picks one European short of up to 30 minutes between 1 Oct 2025 and 30 Sep 2026 ([EFA network](https://europeanfilmacademy.org/about/european-film-academy-short-film-network); [EFA rules](https://www.europeanfilmawards.eu/regulations/european-short-film/)). Fifteen festivals qualify for all three: Clermont-Ferrand, Oberhausen, Tampere, Kraków, Go Short, Vienna Shorts, Winterthur, Uppsala, Leuven, Odense, Drama, Curtas, ZINEBI, PÖFF Shorts and Cork. That makes a natural "triple-qualifier" badge. Several festivals widely assumed to qualify for the Oscars were **absent from the 98th shorts list**: Outfest, Frameline, BFI Flare, Fantasia, Fantastic Fest, BIFAN, Giffoni, True/False, One World, FIFDH, Créteil, Gérardmer, BIFFF and NIFFF. Treat them as non-qualifying unless confirmed.

### Table 2. Academy Documentary Feature qualifying festivals, 98th list [V]

Source: [AMPAS 98th combined list](https://oscars.org/sites/oscars/files/2024-10/98_Full_Qualifying_Festival_List_Combined.pdf). True/False, DOC NYC, Full Frame and Camden are **not** on this list; US documentaries qualify through theatrical release.

| Festival | Qualifying award |
|---|---|
| Berlinale | Best Documentary Award; TEDDY Best Documentary Feature |
| Cannes | L'Œil d'or |
| FICCI Cartagena | Best Film, Documentary Competition |
| CPH:DOX | DOX:AWARD |
| DMZ Docs | Grand Prize (International and Korean) |
| Doc Edge (NZ) | Best International Feature; Best NZ Feature |
| DocAviv | Best International Film; Best Israeli Documentary |
| DocVille (Belgium) | Jury Award |
| Durban IFF | Best International and Best South African Documentary |
| FESPACO | Golden Stallion, Documentary Feature |
| Göteborg | Dragon Award, Best Nordic Documentary |
| Guadalajara (FICG) | Best Ibero-American Documentary |
| Hong Kong IFF | Firebird Award, Documentary |
| Hot Docs | Best International Feature Documentary |
| IDFA | Award for Best Feature-Length Documentary |
| Sheffield DocFest | Grand Jury Award, International Competition |
| Kerala IDSFFK | Best Long Documentary |
| DOK Leipzig | Golden Dove, International Long Documentary |
| Ji.hlava | Best World Documentary; Best Central & East European Documentary |
| Kraków | Golden Horn for Documentary |
| Millennium Docs Against Gravity | Grand Prix |
| Morelia (FICM) | Best Mexican Documentary Feature |
| Movies That Matter | Grand Jury Documentary |
| Premios Platino | Best Documentary |
| Sarajevo | Heart of Sarajevo, Best Documentary |
| Sydney FF | Documentary Australia Award |
| Taipei Golden Horse | Best Documentary Feature |
| Thessaloniki Doc | Golden Alexander |
| Visions du Réel | International Feature Competition Grand Jury Prize |
| It's All True | Best Documentary, International Competition |
| Yamagata | Robert and Frances Flaherty Prize; Ogawa Shinsuke Prize |


## India's four FIAPF festivals cluster from November to February, and only IFFI carries the "A"

India has four FIAPF-accredited festivals in 2026. **IFFI Goa is the only A-Festival.** BIFFes (Bengaluru), KIFF (Kolkata) and IFFK (Kerala) are accredited without the mark. Mumbai's MAMI and the Chennai festival are not on the list ([FIAPF 2026 calendar](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf)). The PDF gives "TBA" for KIFF and IFFK, but both have since been dated: KIFF runs 16–23 Dec 2026 and IFFK 11–18 Dec 2026. The Indian winter circuit is therefore dense. IFFI closes 28 Nov, IFFK opens 11 Dec, KIFF opens 16 Dec, and BIFFes normally follows in late January. Winning films circulate between them. Fazil Razak's *Moham* won at IFFK 2025 and BIFFes 2026, and Santosh Davakhar's *Gondhal* won at IFFI 2025 and BIFFes 2026 ([Onmanorama](https://www.onmanorama.com/entertainment/entertainment-news/2025/12/19/iffk-2025-two-seasons-two-strangers-best-film-abderrahmane-sissako-lifetime-achievement.html); [biffes.org](https://biffes.org/awardWinner)). The app should cross-link films across these editions.

### IFFI Goa: the 57th edition is under way and its winners are due 28 Nov

The **57th IFFI runs 20–28 Nov 2026 in Goa under the theme "Stories Without Borders"**. It is organised by the Ministry of Information & Broadcasting with the Government of Goa and the Entertainment Society of Goa ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2335780&reg=48&lang=2)). PIB reports **more than 150 international films from 86 countries**, a 76-film Indian Panorama in 18 languages and 14 Gala Premieres. The festival uses **13 screens at four locations with over 4,000 seats**. The submission count is inconsistent within the same release: "over 1,900 from 137 countries" in the body text, against "1,400" in the Festival Director's quote. A secondary blog gives 159 films from about 1,400 submissions ([Elegant IFF](https://elegantiff.com/2026/11/22/iffi-2026-goa-pawlikowskis-fatherland-opens-the-57th-edition-dhurandhar-leads-indian-panorama/)). Store both submission figures with their sources. The 2026 winners are not yet available and should be a placeholder refreshed after 29 Nov.

| Field | IFFI 2026 (57th) | Tag |
|---|---|---|
| Dates | 20–28 Nov 2026 | [V] [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2335780&reg=48&lang=2) |
| Venues | Panaji: 7 screens across INOX, Maquinez, Samrat and Ashoka; INOX Porvorim; Ravindra Bhavan, Margao; Magic Movie, Ponda. Masterclasses: 14 sessions at Kala Academy, 21–27 Nov | [V] PIB |
| Approximate coordinates | INOX Panjim/ESG complex 15.4989, 73.8278; Kala Academy 15.4950, 73.8195; Ravindra Bhavan Margao 15.2833, 73.9667 | [BG] |
| Sections | International Competition (Golden Peacock); Best Debut Feature Competition (7 films); Indian Panorama (feature and non-feature); Gala Premieres; Country of Honour Spain (4 films); Partner Country Russia (4); BRICS focus; Animation (5, new); Films About Films (5, new); Andrzej Wajda centenary (5); Restored Classics (5); Indian centenaries (Shakti Samanta, Raj Khosla, Uttam Kumar, Suryakant Mandhare, Prem Nazir, Raj Kumar, O.P. Nayyar, Ravi); Creative Minds of Tomorrow, 6th ed. (100 participants, 13 crafts) | [V] PIB |
| Opening / mid-fest / closing | *Fatherland* (Paweł Pawlikowski) / *I Matter* (Alina Serban) / *We Are All Strangers* (Anthony Chen, Singapore) | [V] PIB |
| Indian Panorama openers | *Dhurandhar* (feature, Aditya Dhar); *Becoming* (non-feature, Leena Yadav, Ladakhi) | [V] PIB |
| Indian films in competition | Three, including *Kantara: A Legend – Chapter 1* | [V, secondary] [Elegant IFF](https://elegantiff.com/2026/11/22/iffi-2026-goa-pawlikowskis-fatherland-opens-the-57th-edition-dhurandhar-leads-indian-panorama/) |
| People | Festival Director Ashutosh Gowariker; International Jury Chair Aanand L Rai; Indian Panorama Feature Jury Chair Madhur Bhandarkar; Non-Feature Jury Chair Himanshu Shekhar Khatua | [V] PIB |
| Market | WAVES Film Bazaar: Screenwriters' Lab, Co-production Market, Viewing Room, Work-in-Progress Lab, 150 invited guests. Exact 2026 Bazaar dates not stated | [V] PIB; venue (Marriott, Miramar) [BG] |
| Official channels | iffigoa.org; delegate portal my.iffigoa.org; FilmFreeway listing for submissions | [V] [IFFI FAQ](https://www.iffigoa.org/about-faq/en); [FilmFreeway](https://filmfreeway.com/InternationalFilmFestivalofIndiaIFFI-Goa) |
| History | Founded 1952; permanently in Goa since 2004 (35th ed.); run by the Directorate of Film Festivals until its merger into NFDC (2022–23); Golden Peacock worth about Rs 40 lakh | [BG] [Wikipedia](https://en.wikipedia.org/wiki/IFFI_Best_Film_Award) |

The **56th IFFI (2025) closed on 28 Nov 2025** at Dr Shyama Prasad Mukherjee Indoor Stadium. Its Golden Peacock went to **Ash Mayfair's *Skin of Youth* (Vietnam)** ([LatestLY/IANS](https://www.latestly.com/agency-news/iffi-2025-winners-list-skin-of-youth-safe-house-gondhal-bandish-bandits-2-bag-top-honours-check-best-actor-male-and-female-awardees-7222278.html); [The Goan](https://www.thegoan.net/goa-news/%E2%80%98skin-of-youth%E2%80%99-wins-golden-peacock-for-best-film-at-iffi/139702.html); [ANI](https://aninews.in/news/entertainment/bollywood/iffi-2025-vietnamese-film-skin-of-youth-bags-best-feature-santosh-davakahar-wins-best-director-for-marathi-film-gondhal20251129101613/)).

| IFFI 2025 award | Winner | Tag |
|---|---|---|
| Golden Peacock (Best Film) | *Skin of Youth*, Ash Mayfair (Vietnam) | [V] |
| Silver Peacock, Best Director | Santosh Davakhar, *Gondhal* (Marathi) | [V] |
| Best Debut Director | Karan Singh Tyagi, *Kesari 2* | [V] |
| Best Actor (Male) | Ubeimar Rios, *A Poet* | [V] |
| Best Actor (Female) | Jara Sofija Ostan, *Little Trouble Girls* | [V] |
| Special Jury Award | Akinola Davies Jr., *My Father's Shadow* | [V] |
| ICFT-UNESCO Gandhi Medal | *Safe House*, Eirik Svensson | [V] |
| Best Web Series (OTT) | *Bandish Bandits Season 2* | [V] |
| Honour | Rajinikanth, 50 years in cinema | [S] [NewsBytes](https://www.newsbytesapp.com/news/entertainment/iffi-2025-winners-list/story) |

### IFFK Thiruvananthapuram: the 31st edition opens 11 Dec with round-the-clock screenings

The **31st IFFK runs 11–18 Dec 2026**. First shows start at 7 am, screenings run round the clock on six of the eight days, and the edition marks the **centenary of Malayalam cinema**. Delegate registration opened at registration.iffk.in at 10 am on 25 Nov 2026 and took **4,500 registrations in the first four hours** ([Indian Opinion](https://indianopinion.org/iffk-31-delegate-registration-opens-14-films-in-competition); [AltBollywood](https://www.altbollywood.com/post/iffk-2026-delegate-registration-open-31st-edition-thiruvananthapuram)). The International Competition has 14 films, including Adoor Gopalakrishnan's *Padayatra*, Leo Thaddeus's *Chevitorma*, and the Tamil films *Members of the Problematic Family* and *Selvi*. Other sections are World Cinema, Critics Discovery (5 new Malayalam films), Malayalam Cinema Today (12) and Indian Cinema Now (7). Tagore Theatre is confirmed as a venue and the delegate cell. The rest of the venue list, the organiser structure and the competition rules are background knowledge. Kerala State Chalachitra Academy organises the festival for the state Department of Cultural Affairs. It was founded in 1996 in Kozhikode, and its competition is restricted to Asian, African and Latin American cinema ([Wikipedia](https://en.wikipedia.org/wiki/International_Film_Festival_of_Kerala), [BG]).

| IFFK 2025 (30th) award | Winner | Tag |
|---|---|---|
| Suvarna Chakoram (Golden Crow Pheasant, Best Film; Rs 20 lakh) | *Two Seasons, Two Strangers*, Sho Miyake (Japan) | [V] |
| Rajata Chakoram, Best Director | Carina Piazza & Lucia Bracelis, *Before the Body* | [V] |
| Rajata Chakoram, Best Debut Director + KR Mohanan Award | Tanushree Das & Saumyananda Sahi, *Shadowbox* | [V] |
| Special Jury Award + Audience Poll Award | *Thanthapperu*, Unnikrishnan Avala | [V] |
| FIPRESCI Best Film (International Competition) | *Khidki Gaav*, Sanju Surendran | [V] |
| FIPRESCI Best Debut Malayalam Director | Fazil Razak, *Moham* | [V] |
| NETPAC Best Asian Film | *Cinema Jazira* | [V] |
| Special mentions | *Black Rabbit White Rabbit* (technical); Tilottama Shome (acting, *Shadowbox*) | [V] |
| Lifetime Achievement (Rs 10 lakh) | Abderrahmane Sissako | [V] |

Sources for the table: [Onmanorama](https://www.onmanorama.com/entertainment/entertainment-news/2025/12/19/iffk-2025-two-seasons-two-strangers-best-film-abderrahmane-sissako-lifetime-achievement.html), [Kerala Kaumudi](https://keralakaumudi.com/en/kerala/general/iffk-two-seasons-two-strangers-wins-golden-crow-pheasant-%C2%A0thanthapperu-wins-audience-poll-award-1667292) and [Deshabhimani](https://english.deshabhimani.com/deshabhimani-english-/iffk-2025-28348/30th-iffk-rajatha-chakoram-lucia-bracelis-carina-piazza--39280). The awards were presented at Nishagandhi by Chief Minister Pinarayi Vijayan; the closing was reported on 19 Dec 2025, and the start date of the 30th edition was not confirmed. Earlier Suvarna Chakoram winners include *Malu* (Brazil, 2024) and *Utama* (2022) ([Kerala Kaumudi](https://keralakaumudi.com/en/cinema/cine-news/suvarna%20chakoram-for-malu-top-honours-for-feminichi-fathima-grand-finale-for-iffk-2024-check-other-winners-1446830); [DT Next](https://www.dtnext.in/amp/story/entertainment/cinema/spanish-film-utama-honoured-with-suvarna-chakoram-award-at-iffk), [S]).

### BIFFes Bengaluru: the 17th edition ran in January–February 2026 with three competitions

The **17th BIFFes ran 29 Jan–6 Feb 2026 with over 200 films** and tributes to B Saroja Devi, Dharmendra and Shaji N Karun ([Deccan Herald](https://www.deccanherald.com/india/karnataka/bengaluru/17th-biffes-to-be-held-from-january-29-and-february-6-over-200-films-to-be-screened-3840527)). The Karnataka Chalanachitra Academy organises it with the state government. The official awards page lists the winners, contact details (+91 8904645529, biffesblr@gmail.com) and an address at #20/A Circular Road, Nandini FHS Layout, Bengaluru 560096. That address may be the Academy's office rather than a screening venue ([biffes.org](https://biffes.org/awardWinner)). A Deccan Herald headline says the 17th edition moved to a "new venue", but the venue was not named in the fetched text. Earlier editions used PVR Orion Mall, Rajajinagar (about 13.0110, 77.5550) [BG]. No 2027 (18th) dates were found; by pattern the edition would fall in Jan–Mar 2027.

| BIFFes 2026 (17th) competition | Winners | Tag |
|---|---|---|
| Asian Cinema Competition | 1st *Lost Land (Hara Watan)*, Akio Fujimoto (Japan); 2nd *Shape of Momo*, Tribeny Rai (India); 3rd *The Deepest Space In Us*, Yasutomo Chikuma (Japan); Special Mention *Republic of Pipolipinas*, Renei Dimla (Philippines) | [V] |
| Indian Cinema Competition (listed without ranks) | *Sabar Bonda* (Marathi, Rohan Parashuram Kanawade); *Moham* (Malayalam, Fazil Razak); *Kaadu* (Malayalam, Suneesh Vadakumbadan); *Gondhal* (Marathi, Santosh Davakhar); Special Mention *Sarkeet (A Short Trip)* | [V] |
| Kannada Cinema Competition | *Vanya*, Badiger Devendra (Best Kannada Film per [NewsFirst](https://newsfirstlive.com/cinema/17th-international-film-festival-the-film-vanya-wins-the-best-kannada-film-award-11084835), [S]); *Nam Saali*; *Ravana Rajyadalli Navadampathigalu*; *Hakkighagi*; *Mrigatrishna*; *4 by 4* | [V] |
| Lifetime Achievement | Dr Hamsalekha | [V] |

### Delegate registration is cheap, online and approval-based

**IFFI uses a one-time myIFFI profile at my.iffigoa.org.** Applicants register as Delegate or Media, receive an approval email and then pay through a link (net banking, card or an offline HDFC challan). No cash is accepted at venues. Students attend free, passes are non-transferable and non-refundable, a lost badge costs Rs 100, and screening tickets are booked online ([IFFI FAQ](https://www.iffigoa.org/about-faq/en)). The 2025 fee for professionals and cine-enthusiasts was **Rs 1,180 including GST**, and the opening and closing ceremonies are invitation-only ([AltBollywood](https://www.altbollywood.com/post/iffi-2026-goa-dates-delegate-pass-57th-edition)). IFFK's 2024 fees were the same Rs 1,180 general, with Rs 590 for students. Both figures are Rs 1,000 plus 18% GST. The 2026 IFFK and BIFFes fees were not found. BIFFes historically charged about Rs 800 general and Rs 400 concession [BG]. IFFK historically has about 13,000–15,000 delegates [BG].

| Festival | Portal | Fee (latest found) | Tag |
|---|---|---|---|
| IFFI | my.iffigoa.org | Rs 1,180 incl. GST (2025); students free | [V] |
| IFFK | registration.iffk.in (opened 25 Nov 2026) | Rs 1,180 general / Rs 590 students (2024) | [V] |
| BIFFes | filmfestival.biffes.org | about Rs 800 / Rs 400 (historical) | [BG] |
| MIFF | via miff.in | not found; registration opened before 15–21 Jun 2026 | [S] [News on AIR](https://www.newsonair.gov.in/delegate-registrations-open-for-19th-miff-ahead-of-june-15-21-event/) |
| Jaipur IFF | FilmFreeway tickets | VIP/industry delegate passes | [S] [FilmFreeway](https://www.filmfreeway.com/JaipurInternationalFilmFestival/tickets) |

### Table 3. Other Indian festivals

| Festival | City | 2025 / 2026 editions | Organiser / notes | Tag and source |
|---|---|---|---|---|
| Kolkata IFF (KIFF) | Kolkata | 30th: 4–12 Dec 2024; 31st: 6–13 Nov 2025 (215 films, Poland focus); **32nd: 16–23 Dec 2026**, inauguration at Victoria Memorial, Ireland focus | West Bengal Information & Cultural Affairs Dept; FIAPF accredited. Founded 1995; venues Nandan, Rabindra Sadan, Sisir Mancha; top award Golden Royal Bengal Tiger [BG] | [V] [ThePrint](https://theprint.in/feature/kolkata-international-film-festival-to-be-held-between-december-4-12/2189800); [IndiaBlooms](https://www.indiablooms.com/showbiz/rajinikanth-prabhas-akshay-kumar-kangana-ranaut-star-studded-kiff-2026-inauguration-to-shift-to-victoria-memorial/details); [S] [Instytut Polski](https://instytutpolski.pl/newdelhi/2025/11/03/poland-as-country-of-focus-at-the-31st-kolkata-international-film-festival/) |
| Jio MAMI Mumbai FF | Mumbai | 2025 edition cancelled for a revamp; return planned for 2026 with a South Asian focus; no 2026 dates confirmed | Not FIAPF | [V] [Screen Daily](https://www.screendaily.com/news/mumbai-film-festival-cancels-2025-edition/5207162.article); [S] [Yahoo](https://ca.news.yahoo.com/jio-mami-mumbai-film-festival-073000146.html) |
| MIFF (documentary, short fiction, animation) | Mumbai | 19th: 15–21 Jun 2026 at NFDC Complex, Pedder Road; 346 films | MIB/NFDC. Biennial since 1990; top award Golden Conch [BG] | [S] [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2250700&reg=3&lang=2); [IndianTelevision](https://indiantelevision.com/movies/mumbai-international-film-festival-2026-returns-for-19th-edition-with-346-films-and-a-global-slate/); [brochure](https://miff.in/storage/documents/2026/brochure/doc_69b1059ed9d83.pdf) |
| Pune IFF (PIFF) | Pune | 24th: 15–22 Jan 2026 | Pune Film Foundation with Govt of Maharashtra; director Jabbar Patel [BG] | [S] [Modern Shrines](https://modernshrines.in/2025/12/21/24th-piff-film-festival-15-22-january-2026/) |
| Delhi international festival | Delhi | 2026 edition with 125 films | Details thin | [S] [Outlook Traveller](https://www.outlooktraveller.com/amp/story/destinations/india/News/delhi-to-host-international-film-festival-2026-featuring-125-films) |
| Bengaluru Int'l Short FF (BISFF) | Bengaluru | 2026 winners page live; separate from BIFFes; Academy short-qualifying (GEN, AN) on the 98th list | | [V] [bisff.in](https://bisff.in/winners); [AMPAS98](https://www.oscars.org/sites/oscars/files/2024-11/98th_qualifying_festival_list_all_shorts.pdf) |
| IDSFFK | Thiruvananthapuram | Usually Jul–Aug [BG] | Kerala State Chalachitra Academy; Academy Documentary Feature qualifier (Best Long Documentary) and DOC-short qualifier | [V] [AMPAS98-DF](https://oscars.org/sites/oscars/files/2024-10/98_Full_Qualifying_Festival_List_Combined.pdf) |
| Kashish Mumbai Int'l Queer FF | Mumbai | May–Jun [BG] | Founded 2010 [BG] | [BG] |
| Not researched (all [BG], months only) | | Chennai IFF (Dec), Dharamshala IFF (Oct/Nov), Jaipur IFF (Jan), Habitat FF Delhi (May), Ajanta-Ellora IFF (Jan), Guwahati, Shimla, Third Eye Asian (Mumbai), Hyderabad; diaspora festivals IFFLA, IFFM Melbourne (Aug), LIFF London (Jun), Stuttgart (Jul) | | [BG] |

India's national and state film awards (the National Film Awards from MIB/NFDC, the Kerala State Film Awards from the Chalachitra Academy and the Karnataka State Film Awards) are award bodies, not festivals. No 2025 or 2026 winners for them were researched.

## Most 2026 top prizes are settled, with three still pending and two editions missing

By 26 Nov 2026 the season's headline prizes are known. Cristian Mungiu's *Fjord* won the Palme d'Or (his second), İlker Çatak's *Yellow Letters* won the Golden Bear, May el-Toukhy's *Woman Unknown* the Golden Lion, Majid Majidi's *Midday Meal* the Busan Award, and Milcho Manchevski's *Sister Brother Manhole Cover* the Tokyo Grand Prix. Three results are pending: IFFI and Marrakech both close on 28 Nov, and IFFK runs in December. Two festivals have no 2026 winners at all. **Red Sea postponed its 6th edition (planned 3–12 Dec 2026) to Q4 2027**, and **FESPACO is biennial**, with the next edition in 2027 ([Screen Daily](https://www.screendaily.com/news/red-sea-international-film-festival-postponed-until-2027/5220602.article); [fespaco.bf](https://fespaco.bf/en/)). Red Sea's foundation gave "a comprehensive review" of timing and logistics as its reason; Africanews framed the decision "amid Houthi attacks on Saudi Arabia", which is the outlet's framing and not the stated cause ([Africanews](https://www.africanews.com/2026/09/21/red-sea-film-festival-postponed-amid-houthi-attacks-on-saudi-arabia/)). The Red Sea Fund and Labs continue.

The year has a strong pattern of crossover winners, which the app should expose as film-level links. ***La bola negra* (Javier Calvo & Javier Ambrossi) shared Cannes Best Director, won the TIFF People's Choice and took the San Sebastián Audience Award**, putting it on an Oscar path ([AP via Local10](https://www.local10.com/entertainment/2026/09/20/la-bola-negra-wins-tiffs-people-choice-award-putting-it-on-oscar-path/)). Romanian directors won both Cannes and Locarno. Simon Stone's *Elsinore* won the TIFF International People's Choice, and its lead Andrew Scott won Best Actor at Mar del Plata. *The Violinist* won at Annecy, APSA and Golden Horse. Sompot Chidgasornpongse's *9 Temples to Heaven* took Best Director at both Shanghai (Asian New Talent) and APSA. Akio Fujimoto's *Lost Land* won the 2025 Golden Yusr at Red Sea and first prize at BIFFes 2026.

### Table 4. Top prizes, 2026 editions (and latest edition where 2026 is absent)

| Festival | Edition, dates | Top prize | Winner (director) | Tag and source |
|---|---|---|---|---|
| Cannes | 79th, 12–23 May 2026; jury president Park Chan-wook | Palme d'Or | *Fjord* (Cristian Mungiu) | [V] [Euronews](https://euronews.com/culture/2026/05/23/cannes-2026-cristian-mungius-political-drama-fjord-wins-the-palme-dor); [Wikipedia](https://en.wikipedia.org/wiki/2026_Cannes_Film_Festival) |
| Berlinale | 76th, 12–22 Feb 2026; jury president Wim Wenders | Golden Bear | *Yellow Letters* (İlker Çatak) | [V] [Outlook India](https://www.outlookindia.com/art-entertainment/berlinale-2026-full-winners-list-out) |
| Venice | 83rd, 2–12 Sep 2026; jury president Maggie Gyllenhaal | Golden Lion | *Woman Unknown* (May el-Toukhy) | [V] [Euronews](https://www.euronews.com/culture/2026/09/12/venice-film-festival-2026-woman-unknown-of-may-el-toukhy-wins-the-golden-lion) |
| TIFF | 51st, 10–20 Sep 2026 | People's Choice Award | *La bola negra* (Javier Calvo & Javier Ambrossi) | [V] [TheWrap](https://thewrap.com/industry-news/awards/la-bola-negra-wins-tiff-peoples-choice-award) |
| Sundance | 22 Jan–1 Feb 2026, last Utah edition | Grand Jury Prize, US Dramatic | *Josephine* (Beth de Araújo) | [V] [Sundance](https://www.sundance.org/blogs/the-complete-list-of-2026-sundance-film-festival-award-winners/) |
| Locarno | 79th, 5–15 Aug 2026 | Pardo d'oro | *You Don't Belong Here* (Florin Șerban) | [V] [Romania Insider](https://www.romania-insider.com/florin-serban-top-prize-locarno-film-festival-2026) |
| San Sebastián | 74th, 18–26 Sep 2026; jury president Ira Sachs | Golden Shell | *Tender Loving Care* (Mike Leigh) | [V] [Ara](https://en.ara.cat/culture/indisputable-golden-shell-to-mike-leigh-for-the-extraordinary-tender-loving-care_1_5862038.html) |
| Karlovy Vary | 60th, 3–11 Jul 2026 | Crystal Globe | *Fruit Gathering* (Aung Phyoe) | [V] [KVIFF](https://www.kviff.com/en/news/6023-the-crystal-globe-goes-to-fruit-gathering-lover-not-a-fighter-wins-the-proxima-competition) |
| IFFR Rotterdam | 55th, Jan–Feb 2026 (dates not verified) | Tiger Award (€40,000) | *Variations on a Theme* (Jason Jacobs & Devon Delmar) | [V] [IFFR](https://iffr.com/en/blog-iffr-2026-tiger-big-screen-award-winners) |
| Annecy | 21–27 Jun 2026 (50th edition per Unifrance) | Cristal for a Feature | *The Violinist* (Ervin Han & Raúl García) | [V] [Cartoon Brew](https://www.cartoonbrew.com/festivals/annecy-winners-2026-violinist-iron-boy-paper-trail-263799.html) |
| Mar del Plata | 41st, 5–15 Nov 2026 | Top international prize (source: "Premio Astor Piazzolla") | *The Night Arezou Disappeared* (Arian Vazirdaftari) | [V] [Otros Cines](https://www.otroscines.com/post/festival-de-mar-del-plata-2026-todos-los-premios) |
| Morelia | 24th, Oct 2026 | Best Mexican Feature | *6 meses en el edificio rosa con azul* (Bruno Santamaría Razo) | [V] [Chilango](https://www.chilango.com/cine-y-tv/peliculas/ficm-2026-lista-completa-de-ganadores/) |
| Gramado | 54th, Aug 2026 | Kikito, Best Brazilian Feature | *Nosso Segredo* | [V, headline] [Jornal do Comércio](https://www.jornaldocomercio.com/cultura/2026/08/1260657-nosso-segredo-recebe-o-kikito-de-melhor-filme-no-54-festival-de-cinema-de-gramado.html) |
| BAFICI | 27th, Apr 2026 | International Competition | Film by Ezequiel Salinas & Ramiro Sonzini (title not retrieved) | [S] [Unidiversidad](https://www.unidiversidad.com.ar/los-argentinos-ezequiel-salinas-y-ramiro-sonzini-ganadores-del-bafici-internacional) |
| CPH:DOX | 2026 | Top award not confirmed | *Whispers in May* (Dongnan Chen) "wins big" | [S] [Screen Daily](https://www.screendaily.com/news/dongnan-chens-coming-of-age-story-whispers-in-may-wins-big-at-cphdox-2026/5215063.article) |
| Busan | 31st, 6–15 Oct 2026 | Busan Award, Best Film (KRW 50m) | *Midday Meal* (Majid Majidi) | [V] [Korea Times](https://www.koreatimes.co.kr/entertainment/films/20261015/iranian-film-midday-meal-wins-top-honor-at-31st-biff) |
| Tokyo | 39th, 26 or 28 Oct–4 Nov 2026 (sources conflict) | Tokyo Grand Prix | *Sister Brother Manhole Cover* (Milcho Manchevski) | [V] [Screen Daily](https://www.screendaily.com/news/tokyo-film-festival-unveils-2026-winners/5222049.article) |
| Shanghai | 28th, 12–21 Jun 2026 | Golden Goblet, Best Feature | *Atlantic Rhapsody* (Zhong Kaifeng) | [V] [Screen Daily](https://www.screendaily.com/news/atlantic-rhapsody-wins-top-golden-goblet-award-at-shanghai-film-festival/5217856.article) |
| Cairo | 47th, 11–20 Nov 2026 | Golden Pyramid | *Four Minus Three* (Adrian Goiginger) | [V] [The Film Verdict](https://thefilmverdict.com/cairo-2026-the-awards/) |
| Golden Horse | 63rd, ceremony 22 Nov 2026, Taipei Music Center | Best Narrative Feature | *We Are Born Good* (Yeung Leung-chuen) | [V] [Focus Taiwan](https://focustaiwan.tw/culture/202611220016) |
| APSA | 2026, about 1–2 Nov, Gold Coast [BG] | Best Film | *Guria* (Levan Koguashvili) | [V] [Screen Daily](https://www.screendaily.com/news/guria-wins-best-film-at-asia-pacific-screen-awards-2026/5221948.article) |
| Hong Kong Film Awards | 44th, 2026 | Best Film | *Ciao UFO* (won five) | [V, headline] [Screen Daily](https://www.screendaily.com/news/ciao-ufo-wins-five-including-best-film-at-hong-kong-film-awards-2026/5215823.article) |
| Asian Film Awards | 19th, 16 Mar 2026, Xiqu Centre | Honorary awards only found (Zhang Ziyi, Terrance Lau, Liu Haoran); "stripped-down" edition | — | [V] [AFA](https://www.afa-academy.com/?p=75916); [AllAfrica](https://allafrica.com/stories/202603180499.html) |
| Marrakech | 23rd, 20–28 Nov 2026; jury president Marion Cotillard | Étoile d'Or | **Pending (closes 28 Nov)**; 2025: *Promised Sky* (Erige Sehiri) | [V] [Le360](https://fr.le360.ma/culture/fifm-2026-76-films-trois-hommages-et-dix-rencontres-au-programme-de-la-23eme-edition_YKR2YKZHTND4HKBBIR2VO7ZQQY/); [IONCinema](https://www.ioncinema.com/news/film-festivals/2025-marrakech-intl-film-fest-promised-sky-wins-letoile-dor-all-the-winners) |
| IFFI Goa | 57th, 20–28 Nov 2026 | Golden Peacock | **Pending (closes 28 Nov)**; 2025: *Skin of Youth* (Ash Mayfair) | [V] see India section |
| IFFK | 31st, 11–18 Dec 2026 | Suvarna Chakoram | **Pending**; 2025: *Two Seasons, Two Strangers* (Sho Miyake) | [V] see India section |
| BIFFes | 17th, 29 Jan–6 Feb 2026 | Asian Competition 1st prize | *Lost Land (Hara Watan)* (Akio Fujimoto) | [V] [biffes.org](https://biffes.org/awardWinner) |
| Red Sea | 5th, Dec 2025; **no 2026 edition** | Golden Yusr (US$100k) | 2025: *Lost Land* (Akio Fujimoto), first Rohingya-language feature | [V] [RSIFF](https://redseafilmfest.com/en/the-yusr-awards-2025/) |
| FESPACO | 29th, 2025; **biennial, next 2027** | Étalon d'or de Yennenga | 2025: *Katanga, la danse des scorpions* (Dani Kouyaté), first Burkinabè winner in 28 years | [V] [FESPACO](https://fespaco.bf/en/dani-kouyate-honored-with-golden-stallion-of-yennenga-at-29th-fespaco/) |

### Table 5. Secondary awards for loading (2026 unless stated)

Each row inherits the source cited for its festival in Table 4 unless another source is given.

| Festival | Award | Winner | Tag |
|---|---|---|---|
| Cannes | Grand Prix | *Minotaur* (Andrey Zvyagintsev) | [V] |
| Cannes | Jury Prize | *The Dreamed Adventure* (Valeska Grisebach) | [V] |
| Cannes | Best Director (shared) | Javier Ambrossi & Javier Calvo (*La Bola Negra*); Paweł Pawlikowski (*Fatherland*) | [V] Euronews |
| Cannes | Best Actress (shared) | Virginie Efira and Tao Okamoto (*All of a Sudden*) | [V] |
| Cannes | Best Actor (shared) | Emmanuel Macchia and Valentin Campagne (*Coward*) | [V] |
| Cannes | Screenplay | Emmanuel Marre (*A Man of His Time*) | [V] |
| Cannes | Un Certain Regard Prize | *Everytime* (Sandra Wollner) | [V] |
| Cannes | Short Film Palme d'Or | *For the Opponents* (Federico Luis) | [V] |
| Cannes | Caméra d'Or | Unconfirmed: Wikipedia lists *A Girl Unknown* (Zou Jing) without a label | gap |
| Berlinale | Silver Bear Grand Jury Prize | *Salvation* (Emin Alper) | [V] |
| Berlinale | Silver Bear Jury Prize | *Queen at Sea* (Lance Hammer) | [V] |
| Berlinale | Best Director | Grant Gee (*Everybody Digs Bill Evans*) | [V] |
| Berlinale | Best Lead Performance | Sandra Hüller (*Rose*) | [V] |
| Berlinale | Best Supporting Performance | Anna Calder-Marshall & Tom Courtenay (*Queen at Sea*) | [V] |
| Berlinale | Screenplay | Geneviève Dulude-De Celles (*Nina Roza*) | [V] |
| Berlinale | Outstanding Artistic Contribution | Anna Fitch & Banker White (*Yo (Love Is a Rebellious Bird)*) | [V] |
| Venice | Silver Lion Grand Jury Prize | *Possible Love* (Lee Chang-dong) | [V] |
| Venice | Silver Lion Best Director | Ilya Khrzhanovsky (*Dau*; source spells "Krzhanovsky") | [V] |
| Venice | Special Jury Prize | *NAZA* (Yuval Abraham & Rachel Szor) | [V] |
| Venice | Volpi Cup Best Actor | John Malkovich (*Wild Horse Nine*) | [V] |
| Venice | Volpi Cup Best Actress | Mathilde Arcel (*Woman Unknown*) | [V] |
| Venice | Screenplay | Stéphane Brizé (*A Good Little Soldier*) | [V] |
| Venice | Marcello Mastroianni Award | Malou Khebizi (*15/18 (A Place to Heal)*) | [V] [AV Club](https://www.avclub.com/venice-film-festival-winners-2026) |
| TIFF | International People's Choice | *Elsinore* (Simon Stone) | [V] [Wikipedia](https://en.wikipedia.org/wiki/2026_Toronto_International_Film_Festival) |
| TIFF | Documentary People's Choice | *Darlene Love: I Know Where I've Been* (Barry Avrich) | [V] |
| TIFF | Midnight Madness People's Choice | *Ladies and Gentlemen, Brian Mulroney* (Matthew Rankin) | [V] |
| TIFF | Platform Prize | *Angh* (Theja Rio) | [V] |
| TIFF | Best Canadian Feature | *Sunburn* (Serville Poblete) | [V] |
| TIFF | FIPRESCI / NETPAC | *Ancestors* (David Turpin) / *Thirteen in Gaza* (Hosam Abu Dan) | [V] |
| Sundance | US Documentary Grand Jury | *Nuisance Bear* (Gabriela Osio Vanden & Jack Weisman) | [V] |
| Sundance | World Dramatic Grand Jury | *Shame and Money* (Visar Morina) | [V] |
| Sundance | World Documentary Grand Jury | *To Hold a Mountain* (Biljana Tutorov & Petar Glomazić) | [V] |
| Sundance | Short Film Grand Jury | *The Baddest Speechwriter of All* (Ben Proudfoot & Stephen Curry) | [V] |
| Sundance | Audience Awards | US Dramatic *Josephine*; US Doc *American Pachuco: The Legend of Luis Valdez*; World Dramatic *Hold Onto Me*; World Doc *One in a Million* | [V] |
| Sundance | Alfred P. Sloan Prize | *In the Blink of an Eye* (Andrew Stanton) | [V] |
| Locarno | Special Jury Prize | *The Riverbank* (Matheus Farias & Enock Carvalho) | [V] [Wikipedia](https://en.wikipedia.org/wiki/79th_Locarno_Film_Festival) |
| Locarno | Best Direction | Hong Sang-soo (*Nowhere to Lay My Eyes*) | [V] |
| Locarno | Cineasti del presente Golden Leopard | *The Illusion of an Everlasting Summer* (Alessandra Sanguinetti) | [V] |
| Locarno | Honours | Leopard of Honour Darren Aronofsky; Pardo alla Carriera James Gray | [V] |
| Locarno | Best Actress | Monica Bellucci, per one outlet; Wikipedia's list garbled; verify | conflict [Sorrisi](https://www.sorrisi.com/cinema/attori-attrici/monica-bellucci-miglior-attrice-a-locarno-79/) |
| San Sebastián | Special Jury Prize / Best Director | *Border* (China) / Amanda Kernell (*Brace Your Heart*) | [V] |
| San Sebastián | Lead Performance (shared) | Kate O'Flynn (*Tender Loving Care*) and the lead of *Growth of the Soil* | [V] |
| San Sebastián | Cinematography / Supporting / Audience | *Growth of the Soil* (Hans Petter Moland) / Javier Cámara (*5 minutos más*) / *La bola negra* | [V] |
| Karlovy Vary | Special Jury Prize + Best Director | *The Guest* (Mads Mengel) | [V] |
| Karlovy Vary | Best Actor / Actress | Ghassan Saad (*Pipes*) / Anna Schinz (*A Happy Family*) | [V] |
| Karlovy Vary | Proxima Grand Prix / Audience | *Lover, Not a Fighter* (Martina Buchelová) / *Bára – Diary of a Rockstar* (Helena Třeštíková) | [V] |
| IFFR | Big Screen Award | *Master* (Rezwan Shahriar Sumit) | [V] |
| IFFR | Tiger Special Jury Awards | *La belle année* (Angelica Ruffier); *Supporting Role* (Ana Urushadze, also FIPRESCI) | [V] |
| Annecy | Contrechamp Grand Prix / Cristal for a Short | *Blaise* (Dimitri Planchon & Jean-Paul Guigue) / *Paper Trail* (Don Hertzfeldt) | [V] |
| Mar del Plata | Best Actor / Argentine / Latin American Feature | Andrew Scott (*Elsinore*) / *Cebar, frenar, llorar* (Gerardo Tassan) / *El pez que fuma* (Luis Fernández) | [V] |
| Morelia | Best Mexican Documentary | *Forensita* (Pablo Vaca) | [V] |
| Gramado | Most Kikitos | *Feito Pipa* (four) | [V, headline] [O Hoje](https://ohoje.com/2026/08/24/nosso-segredo-vence-festival-de-gramado-e-feito-pipa-leva-quatro-kikitos/) |
| Busan | Best Director / Special Jury | Lee Yun Chan (*To Be Ordinary*) / Eddie Cahyono (*My Mother*); 13 films in competition; attendance 200,043 | [V] |
| Busan | Vision awards / Actor of the Year | *Zogsool* (four prizes) / Kang Seung-ho | [S] [Screen](https://www.screendaily.com/news/mongolian-satire-zogsool-leads-busan-vision-awards-with-four-prizes/5221459.article); [Sports Khan](https://sports.khan.co.kr/en/article/202610161026007) |
| Busan 2025 | Best Film / Best Director (first competitive edition) | *Gloaming in Luomu* (Zhang Lu) / Shu Qi (*Girl*) | [S] [Screen](https://www.screendaily.com/news/zhang-lus-gloaming-in-luomu-wins-busan-award-for-best-film-shu-qi-takes-best-director-for-girl/5209353.article) |
| Tokyo | Special Jury / Director / Actress / Actor | *Magic Atlas* (Sun Xun) / Lisandro Alonso (*Double Freedom*) / Hu Ling (*The Night That Binds Us*) / Ryo Narita (*Two Cigarettes, Three Nights*) | [V] |
| Tokyo | Artistic Contribution / Audience | *Until the Day Ends* (Jelena Maksimović) / *Heysel 85* (Teodora Ana Mihai) | [V] |
| Tokyo | Asian Future / Nippon Cinema Now / Ethical Film | *Serife Tavsan* (Tareq Daoud) / *silver express* (Miki Tanaka) / *I Rarely Wake Up Dreaming* (Isabelle Stever) | [V] |
| Tokyo | Kurosawa Akira Award | Mipo O and Mohammad Rasoulof | [V] |
| Tokyo 2025 / 2024 | Grand Prix | *Palestine 36* (Annemarie Jacir) / *Teki Cometh* | [S] [Screen](https://www.screendaily.com/news/annemarie-jacirs-palestine-36-leads-winners-at-tokyo-film-festival/5210635.article); [Deadline](https://deadline.com/2024/11/teki-cometh-tokyo-film-fest-grand-prix-best-director-actor-1236168919) |
| Shanghai | Jury Grand Prix / Director / Actress | *Iluminada* (Nicolás Rincón Gille) / Yassine El Idrissi (*Halima*) / Khadija Amari (*Halima*) | [V] |
| Shanghai | Actor / Screenplay / Cinematography / Artistic | Zhang Songwen (*Secret in the Box*) / Reis Çelik (*Night of Blindness*) / Hao Jiayue (*Atlantic Rhapsody*) / *The Miserable Mother* (Susanne Heinrich) | [V] |
| Shanghai | Asian New Talent Film / Director | *Her First Taste* (Gong Yiwen) / Sompot Chidgasornpongse (*9 Temples to Heaven*) | [V] |
| Shanghai | Documentary / Animation | *Notes Unheard* (Gu Jun) / *Lucy Lost* (Olivier Clert) | [V] |
| Cairo | Silver / Bronze Pyramid | *Words of Love* (Rudi Rosenberg) / *Al Baraneya* (Ashgan El-Hamus) | [V] |
| Cairo | Horizons of Arab Cinema (Saad Eldin Wahba) | *The Day of Wrath: Tales from Tripoli* (Rania Rafei) | [V] |
| Cairo 2025 | Golden Pyramid | *The New Year That Never Came* (Romania; director Bogdan Mureșanu [BG]) | [S] [AOL/Variety](https://www.aol.com/entertainment/never-came-black-comedy-repressive-094215863.html) |
| Golden Horse | Best Director / Leading Actor | Joseph Hsu (*Double Happiness*) / Liu Kuan-ting (*Double Happiness*) | [V] |
| Golden Horse | Leading Actress / New Director | Angela Yuen (*Afterpiece*) / Shu Qi (*Girl*) | [V] |
| Golden Horse | Animated Feature + Adapted Screenplay / Original Score | *The Violinist* / Kin Leonn & Thomas Foguenne (*We Are All Strangers*) | [V] [Bakchormeeboy](https://bakchormeeboy.com/2026/11/24/film-singapore-films-score-big-at-63rd-golden-horse-awards-with-four-wins-across-nominees-the-violinist-ah-girl-and-we-are-all-strangers/) |
| Golden Horse 2025 | Best Film / Best Actor | *A Foggy Tale* / Chang Chen | [S] [Focus Taiwan](https://focustaiwan.tw/culture/202511230004) |
| APSA | Director / Jury Grand Prize / Performance / New Performer / Animated | Sompot Chidgasornpongse / *No Good Men* (Shahrbanoo Sadat) / Pushpa Thing Lama / Sim Su-bin / *The Violinist* | [V] [Martin Cid](https://www.martincid.com/movies/guria-asia-pacific-screen-awards-best-film/) |
| Red Sea 2025 | Silver Yusr Feature ($30k) / Jury Prize ($10k) | *All That's Left of You* (Cherien Dabis) / *Hijra* (Shahad Ameen) | [V] RSIFF |
| Red Sea 2025 | Golden / Silver Yusr Short | *Coyotes* (Said Zagha, $25k) / *Empty Lands* (Karim Eldin Elalfy, $12.5k) | [V] |
| Red Sea 2025 | Director / Screenplay / Actor / Actress | Ameer Fakher Eldin (*Yunan*) / Cyril Aris & Bane Fakih / Georges Khabbaz / Seo Su-bin | [V] |
| Red Sea 2025 | Cinematic Achievement / Audience ($50k each) / Asharq Doc | *Nighttime Sounds* (Zhang Zhongchen) / *Hijra*; *My Father's Scent* (Mohamed Siam) / *In-I-In Motion* (Juliette Binoche) | [V] |

**Not retrieved, and therefore left blank for the loader:** Venice Orizzonti, the Clermont-Ferrand 2026 Grand Prix, Hot Docs 2026 Best International Feature, Tribeca 2026 (the [press release](https://tribecafilm.com/press-center/festival/press-releases/2026-tribeca-festival-announces-winners) exists but was not read), SXSW 2026, IDFA 2026 (12–22 Nov), Shanghai 2025, the Busan 2026 acting awards and the AFA 2026 competitive categories.

## Per-festival master tables pair verified 2026 dates with unverified basics

The tables in this section are designed to load directly into the app. Across all of them, **2026 dates, FIAPF status and 2026 winners carry [V] where a source was read**. Founding years, coordinates, sections, venues, market names and URLs are mostly **[BG]**: stable and widely documented, but not re-checked in this research. Submission platforms, fees and deadlines are unverified everywhere and should be pulled live from each festival's FilmFreeway or official page. FIAPF codes are **A** (A-Festival), **F** (accredited) and **—** (not accredited), per the [FIAPF 2026 PDF](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf). Only four 2027 dates were found: Karlovy Vary 2–10 Jul 2027 ([KVIFF](https://www.kviff.com/en/news/6023-the-crystal-globe-goes-to-fruit-gathering-lover-not-a-fighter-wins-the-proxima-competition)), Cartagena's 66th edition from 6 Apr 2027 ([FICCI bases](https://ficcifestival.com/sites/default/files/2026-08/FICCI66%20_%20Bases_de_Participaci%C3%B3n_ESP.pdf)), Sundance in Boulder 21–31 Jan 2027 ([Variety AU](https://au.variety.com/2026/film/global/sundance-film-festival-2027-dates-boulder-colorado-33520/)) and Red Sea "Q4 2027".

### Table 6. Europe and the Americas, tier 1 (full records)

Fields marked [V] are verified and their sources appear in Tables 1 and 4. All other cells are [BG].

| # | Festival | City, country | Lat, long [BG] | Founded [BG] | 2026 dates | FIAPF | Top prize | Key sections [BG] | Market / forum [BG] | Main venues [BG] | URL [BG] |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Festival de Cannes | Cannes, France | 43.551, 7.017 | 1946 (planned 1939) | 12–23 May [V] | A | Palme d'Or | Competition, Un Certain Regard, Out of Competition, Cannes Premiere, Midnight, Cannes Classics, La Cinef; parallel Directors' Fortnight, Critics' Week, ACID | Marché du Film; La Fabrique Cinéma | Grand Théâtre Lumière, Salle Debussy, Salle Bazin, Palais K | festival-cannes.com |
| 2 | Berlinale | Berlin, Germany | 52.509, 13.373 | 1951 | 12–22 Feb [V] | A | Golden Bear | Competition, Perspectives (since 2024), Berlinale Special, Panorama, Forum, Generation, Shorts | EFM; Co-Production Market; Talents; World Cinema Fund | Berlinale Palast, Zoo Palast, Haus der Berliner Festspiele | berlinale.de |
| 3 | Venice (Mostra) | Venice Lido, Italy | 45.406, 12.368 | 1932 (oldest) | 2–12 Sep [V] | A | Golden Lion | Venezia, Out of Competition, Orizzonti, Orizzonti Extra, Classics, Immersive; Giornate degli Autori, Settimana della Critica | Venice Production Bridge; Biennale College Cinema; Final Cut in Venice | Sala Grande, PalaBiennale, Sala Darsena, Sala Casinò | labiennale.org/en/cinema |
| 4 | TIFF | Toronto, Canada | 43.647, -79.390 | 1976 | 10–20 Sep [V] | A (new) | People's Choice Award; juried Platform Prize | Gala, Special Presentations, Centrepiece, Docs, Discovery, Platform, Midnight Madness, Wavelengths, Primetime, Short Cuts, Classics | TIFF Industry; **new 2026 film market at Metro Toronto Convention Centre** [V] | Princess of Wales, Roy Thomson Hall, Royal Alexandra, Lightbox, Scotiabank, John Bassett Theatre [V] | tiff.net |
| 5 | Sundance | Park City, Utah, USA (to 2026); Boulder, Colorado (2027) [V] | 40.646, -111.498 | 1978; Institute since 1985 | 22 Jan–1 Feb [V]; 2027: 21–31 Jan, Boulder [V] | — | Grand Jury Prize, US Dramatic | US/World Dramatic and Documentary, NEXT, Premieres, Midnight, Shorts | Institute labs | Eccles, The Ray, Egyptian; Boulder 2027: Boulder Theater, Macky Auditorium, Chautauqua, Cinemark Century [V] | festival.sundance.org |
| 6 | Locarno | Locarno, Switzerland | 46.169, 8.795 | 1946 | 5–15 Aug [V] | A | Pardo d'oro | Piazza Grande (8,000 seats), Concorso internazionale, Cineasti del presente, Pardi di domani, Fuori concorso, Retrospettiva | Locarno Pro; Open Doors; BaseCamp | Piazza Grande, PalaCinema, FEVI, GranRex | locarnofestival.ch |
| 7 | San Sebastián | San Sebastián, Spain | 43.324, -1.979 | 1953 | 18–26 Sep [V] | A | Golden Shell | Official, New Directors, Horizontes Latinos, Zabaltegi-Tabakalera, Perlak, Culinary Zinema | Europe-Latin America Co-Production Forum; WIP Latam/Europa; Ikusmira Berriak | Kursaal, Victoria Eugenia, Príncipe, Tabakalera, Velódromo | sansebastianfestival.com |
| 8 | Karlovy Vary | Karlovy Vary, Czechia | 50.224, 12.883 | 1946 | 3–11 Jul [V]; **2027: 2–10 Jul [V]** | A | Crystal Globe | Crystal Globe Competition, Proxima, Special Screenings, Horizons, Imagina | Eastern Promises Industry Days | Hotel Thermal, Lázně III, Pupp | kviff.com [V] |
| 9 | IFFR Rotterdam | Rotterdam, Netherlands | 51.920, 4.474 | 1972 | Jan–Feb (not verified) | — | Tiger Award (€40k) [V] | Tiger, Big Screen, Harbour, Limelight, Bright Future, Short & Mid-length, Art Directions | CineMart; Rotterdam Lab; Hubert Bals Fund | De Doelen, Pathé Schouwburgplein, LantarenVenster, KINO | iffr.com [V] |
| 10 | Annecy | Annecy, France | 45.901, 6.127 | 1960 | 21–27 Jun [V] | A (new) | Cristal du long métrage | Official Feature, Contrechamp, Shorts, Perspectives, Off-Limits, TV & Commissioned, Graduation | MIFA | Bonlieu, Pathé, Décavision, Pâquier open-air | annecyfestival.com |
| 11 | Clermont-Ferrand | Clermont-Ferrand, France | 45.776, 3.085 | 1979 (int'l 1982) | 30 Jan–7 Feb [V] | A | Grand Prix (International, National, Lab) | Three competitions | Marché du Film Court | Maison de la Culture, Cinéma Capitole | clermont-filmfest.org |
| 12 | Tallinn Black Nights (PÖFF) | Tallinn, Estonia | 59.437, 24.753 | 1997 | 6–22 Nov [V] | A | Grand Prix, Official Selection | Official, First Feature, Critics' Picks, Rebels with a Cause, Just Film, PÖFF Shorts | Industry@Tallinn & Baltic Event | Coca-Cola Plaza, Solaris Kino | poff.ee |
| 13 | Warsaw IFF | Warsaw, Poland | 52.230, 21.003 | 1985 | 9–18 Oct [V] | A | Warsaw Grand Prix | International, Competition 1-2, Free Spirit, Documentary, Shorts | CentEast / Warsaw Next | Kinoteka (Palace of Culture) | wff.pl |
| 14 | Mar del Plata | Mar del Plata, Argentina | -38.001, -57.541 | 1954 | 5–15 Nov [V] | A (only Latin American A) | Astor de Oro / Astor Piazzolla award | International, Latin American, Argentine competitions; Estados Alterados; Autores | MdP Industria / WIP | Teatro Auditorium, Paseo Aldrey | mardelplatafilmfest.com |
| 15 | Tribeca | New York, USA | 40.719, -74.010 | 2002 | 3–14 Jun (25th) [V] | — | Founders Award, Best US Narrative | US/International Narrative, Documentary, Viewpoints, Spotlight, Midnight, Immersive, Games, TV | Tribeca X; Through Her Lens | Spring Studios | tribecafilm.com |
| 16 | SXSW Film & TV | Austin, USA | 30.265, -97.739 | 1987 (film 1994) | March (not verified) | — | Grand Jury Award | Narrative and Documentary Competitions, Headliners, Spotlights, Visions, Midnighters | SXSW Conference & Trade Show | Paramount, Alamo Lamar, Zach Theatre | sxsw.com/festivals/film |
| 17 | Telluride | Telluride, USA | 37.938, -107.812 | 1974 | 4–7 Sep (secondary source) | — | None (Silver Medallion tributes); non-competitive | Lineup secret until eve | — | Werner Herzog Theatre | telluridefilmfestival.org |
| 18 | NYFF | New York, USA | 40.773, -73.983 | 1963 | Sep–Oct (not verified) | — | Non-competitive | Main Slate, Currents, Spotlight, Revivals | — | Alice Tully Hall, Walter Reade | filmlinc.org/nyff |
| 19 | BFI London FF | London, UK | 51.507, -0.115 | 1957 | 7–18 Oct (70th) [V] | — | Best Film, Official Competition | Galas, Official/First Feature/Documentary Competitions, strands (Love, Debate, Laugh, Dare, Thrill, Cult, Journey, Create, Family), Experimenta, Treasures | — | BFI Southbank, Royal Festival Hall, Odeon Luxe Leicester Square, BFI IMAX | bfi.org.uk/london-film-festival |
| 20 | IDFA | Amsterdam, Netherlands | 52.364, 4.884 | 1988 | 12–22 Nov [V] | — | Best Film, International Competition | International, Envision, Dutch, Short & Mid-length, Youth, DocLab, Best of Fests, Frontlight | IDFA Forum [V]; Docs for Sale; Bertha Fund | Tuschinski, Eye, De Balie, Carré | festival.idfa.nl [V] |
| 21 | CPH:DOX | Copenhagen, Denmark | 55.676, 12.568 | 2003 | March (not verified) | — | DOX:AWARD | DOX:AWARD, NEW:VISION, F:ACT, Next:Wave, Nordic:Dox, HUMAN:RIGHTS | CPH:FORUM; CONFERENCE; MARKET | Kulturhuset Islands Brygge, Grand Teatret | cphdox.dk [V] |
| 22 | Hot Docs | Toronto, Canada | 43.665, -79.411 | 1993 | 23 Apr–3 May [V] | F (new) | Best International Feature Doc | — | Hot Docs Forum; Deal Maker; Doc Shop | Hot Docs Ted Rogers Cinema | hotdocs.ca |
| 23 | Morelia (FICM) | Morelia, Mexico | 19.703, -101.193 | 2003 | Oct (24th) [V] | — | Ojo, Best Mexican Feature | Mexican Feature, Documentary, Short; Michoacán | Impulso Morelia | Teatro Morelos, Cinépolis Centro | moreliafilmfest.com |
| 24 | Guadalajara (FICG) | Guadalajara, Mexico | 20.674, -103.344 | 1986 | April (41st) [V]; exact dates not verified | — | Premio Mezcal / Maguey; Best Ibero-American Feature | — | Co-production Meeting | Conjunto Santander (UdeG) | ficg.mx |
| 25 | Cartagena (FICCI) | Cartagena, Colombia | 10.423, -75.551 | 1960 (oldest in Latin America) | 14–19 Apr (65th) [V]; **2027 from 6 Apr** [V]; 65,000+ attendees [V] | — | India Catalina / Best Film | — | Encuentros Cartagena | Teatro Adolfo Mejía | ficcifestival.com [V] |
| 26 | Havana | Havana, Cuba | 23.138, -82.382 | 1979 | 3–13 Dec (47th) [V] | — | Gran Premio Coral | — | Nuevas Miradas | Charles Chaplin, Yara, Karl Marx | habanafilmfestival.com |
| 27 | Gramado | Gramado, Brazil | -29.379, -50.875 | 1973 | Aug (54th) [V] | — | Kikito, Best Film | — | Gramado Film Market | Palácio dos Festivais | festivaldegramado.net |
| 28 | Festival do Rio | Rio de Janeiro, Brazil | about -22.97 (area) | 1999 | Oct (not verified) | — | Troféu Redentor | — | RioMarket | Odeon, Cinelândia | festivaldorio.com.br |
| 29 | BAFICI | Buenos Aires, Argentina | -34.603, -58.384 | 1999 | April (27th) [V] | — | Best Film, International Competition | — | BAL (Buenos Aires Lab) | — | bafici.org [V] |

Sources for the [V] cells not already cited in Tables 1 and 4: [Tribeca press center](https://tribecafilm.com/press-center/festival/press-releases/2026-tribeca-festival-announces-winners), [IDFA](https://festival.idfa.nl/en/idfa-2026-2/), [IDFA Professionals](https://professionals.idfa.nl/markets/co-producing-co-financing/attend-idfa-forum/), [La República](https://www.larepublica.co/ocio/ficci-cerro-edicion-con-mas-de-65-000-asistentes-4382776), [News in America (Havana)](https://newsinamerica.com/pdcc/boletin/2026/abre-convocatoria-la-edicion-47-del-festival-internacional-del-nuevo-cine-latinoamericano/), [Buenos Aires city (BAFICI)](https://buenosaires.gob.ar/gcaba_historico/noticias/bafici-se-anunciaron-los-ganadores-y-la-gran-premiada-llega-este-jueves-al) and [Boulder city FAQ](https://bouldercolorado.gov/sundance-film-festival-frequently-asked-questions). The BFI London dates were verified from ICA and BFI listings, and the Guadalajara edition from Infobae coverage of 18 Apr 2026; those URLs were not captured in the notes. Submissions run through each festival's own portal for Cannes, Berlin, Venice, Locarno, San Sebastián, Annecy and Clermont-Ferrand (via Short Film Depot), and through FilmFreeway for Sundance, TIFF, Tribeca and Hot Docs. All of these platforms are [BG].

### Table 7. Europe and the Americas, tier 2 (core fields)

2026 dates and FIAPF status are [V] from the FIAPF PDF where given. Founding year, month, top prize and URL are [BG].

| Festival | City, country | Founded | Month | 2026 dates | FIAPF | Top prize / notes | URL |
|---|---|---|---|---|---|---|---|
| Málaga | Málaga, Spain | 1998 | Mar | 6–15 Mar | F | Biznaga de Oro; MAFIZ market | festivaldemalaga.com |
| Sitges | Sitges, Spain | 1968 | Oct | 8–18 Oct | F | Best Film; Sitges Pitchbox | sitgesfilmfestival.com |
| Gijón (FICX) | Gijón, Spain | 1963 | Nov | 13–21 Nov | F | Best Feature | gijonfilmfestival.com |
| Punto de Vista | Pamplona, Spain | 2005 | Apr | 20–25 Apr | F (new) | Gran Premio (documentary) | puntodevistafestival.com |
| Cinema Jove | Valencia, Spain | 1986 | Jun | 19–27 Jun | F | Luna de Valencia (youth) | cinemajove.com |
| Mostra de València | Valencia, Spain | — | Nov | 5–15 Nov | F | Palmera d'Or | mostravalencia.com |
| Zinebi | Bilbao, Spain | 1959 | Nov | 20–27 Nov | F | Mikeldi de Oro (doc and short) | zinebi.eus |
| Seville European FF | Seville, Spain | — | Nov | — | — | Giraldillo de Oro | festivaldesevilla.eu |
| Rome Film Fest | Rome, Italy | 2006 | Oct | 14–25 Oct | F | Best Film (Progressive Cinema); MIA market | romacinemafest.it |
| Torino | Turin, Italy | 1982 | Nov | 24 Nov–2 Dec | F | Best Film; TorinoFilmLab | torinofilmfest.org |
| Noir in Festival | Milan/Como, Italy | 1991 | Dec | TBA | F | Black Panther / Raymond Chandler Award | noirfest.com |
| Viennale | Vienna, Austria | 1960 | Oct | 22 Oct–3 Nov | F | Mostly non-competitive | viennale.at |
| Kitzbühel FF | Kitzbühel, Austria | — | Aug | TBA | F | — | filmfestival-kitzbuehel.com |
| Oberhausen | Oberhausen, Germany | 1954 | Apr–May | 28 Apr–3 May | F | Grand Prize of the City of Oberhausen | kurzfilmtage.de |
| DOK Leipzig | Leipzig, Germany | 1955 | Oct–Nov | — | — | Golden Dove | dok-leipzig.de |
| Tampere | Tampere, Finland | 1969 | Mar | 4–8 Mar | F | Grand Prix (short) | tamperefilmfestival.fi |
| Göteborg | Gothenburg, Sweden | 1979 | Jan–Feb | — | — | Dragon Award Best Nordic Film; Nordic Film Market | goteborgfilmfestival.se |
| Stockholm IFF | Stockholm, Sweden | 1990 | Nov | — | — (absent from 2026 PDF) | Bronze Horse | stockholmfilmfestival.se |
| Sofia IFF | Sofia, Bulgaria | 1997 | Mar | 12–22 Mar | F | Grand Prix; Sofia Meetings | siff.bg |
| Kraków FF | Kraków, Poland | 1961 | May–Jun | 31 May–7 Jun | F | Golden Dragon | krakowfilmfestival.pl |
| New Horizons | Wrocław, Poland | 2001 | Jul | — | — | — | nowehoryzonty.pl |
| Gdynia (Polish FF) | Gdynia, Poland | — | Sep | — | — | Golden Lions | — |
| Transilvania IFF | Cluj-Napoca, Romania | 2002 | Jun | 12–21 Jun | F | Transilvania Trophy | tiff.ro |
| Sarajevo FF | Sarajevo, Bosnia and Herzegovina | 1995 | Aug | — | — | Heart of Sarajevo; CineLink | sff.ba |
| Herceg Novi FF | Herceg Novi, Montenegro | — | Aug | 22–28 Aug | F (new) | Golden Mimosa | hercegfest.co.me |
| Cinedays | Skopje, North Macedonia | — | — | TBA | F | — | — |
| Motovun / Pula | Croatia | — | Jul | — | — | Pula: Golden Arena | — |
| Thessaloniki IFF | Thessaloniki, Greece | 1960 | Nov (doc festival Mar) | — | — (absent from 2026 PDF) | Golden Alexander; Agora | filmfestival.gr |
| Molodist | Kyiv, Ukraine | 1970 | Oct | TBA | F | Scythian Deer | molodist.com |
| Istanbul IFF | Istanbul, Türkiye | 1982 | Apr | — | — | Golden Tulip; Meetings on the Bridge | film.iksv.org |
| Ji.hlava IDFF | Jihlava, Czechia | 1997 | Oct | — | — | Documentary | ji-hlava.com |
| Visions du Réel | Nyon, Switzerland | 1969 | Apr | — | — | Sesterce d'or; VdR-Industry | visionsdureel.ch |
| Zurich FF | Zurich, Switzerland | 2005 | Sep–Oct | — | — | Golden Eye | zff.com |
| Edinburgh IFF | Edinburgh, UK | 1947 | Aug | — | — | — | edfilmfest.org |
| Sheffield DocFest | Sheffield, UK | 1994 | Jun | — | — | Grand Jury Award; MeetMarket | sheffdocfest.com |
| Cork IFF | Cork, Ireland | 1956 | Nov | — | — | — | corkfilmfest.org |
| Galway Film Fleadh | Galway, Ireland | — | Jul | — | — | — | — |
| Deauville American FF | Deauville, France | 1975 | Sep | — | — | Grand Prix | festival-deauville.com |
| Cinéma du Réel | Paris, France | 1978 | Mar | — | — | Documentary | cinemadureel.org |
| Lumière Festival | Lyon, France | 2009 | Oct | — | — | Prix Lumière; classics market | festival-lumiere.org |
| Les Arcs | Les Arcs, France | — | Dec | — | — | Coproduction Village | — |
| Gérardmer | Gérardmer, France | 1994 | Jan | — | — | Fantastic genre | festival-gerardmer.com |
| FEST | Belgrade, Serbia | — | Feb–Mar | — | — | — | — |
| Riga, Vilnius Kino Pavasaris, Reykjavík RIFF, Bergen, Haugesund (New Nordic Films), Odense | various | — | various | — | — | Regional | — |
| Festival du Nouveau Cinéma | Montréal, Canada | 1971 | Oct | 7–18 Oct | F (new) | Louve d'Or | nouveaucinema.ca |
| Fantasia | Montréal, Canada | 1996 | Jul–Aug | — | — | Cheval Noir; Frontières market | fantasiafestival.com |
| VIFF | Vancouver, Canada | 1982 | Sep–Oct | — | — | — | viff.org |
| Fantastic Fest | Austin, USA | 2005 | Sep | 17–24 Sep | F | Alamo Drafthouse South Lamar | fantasticfest.com |
| AFI Fest | Los Angeles, USA | 1971 | Oct–Nov | — | — | TCL Chinese Theatre | fest.afi.com |
| Chicago IFF | Chicago, USA | 1964 | Oct | — | — | Gold Hugo | chicagofilmfestival.com |
| SIFF Seattle | Seattle, USA | 1976 | May | — | — | — | siff.net |
| Palm Springs IFF | Palm Springs, USA | 1989 | Jan | — | — | ShortFest in June | psfilmfest.org |
| SFFILM | San Francisco, USA | 1957 | Apr | — | — | — | sffilm.org |
| Mill Valley, Savannah, Hamptons | USA | — | Oct–Nov | — | — | Awards-season stops | — |
| True/False; Full Frame; DOC NYC | Columbia MO; Durham NC; New York | — | Mar; Apr; Nov | — | — | Documentary | truefalse.org; fullframefest.org; docnyc.net |
| Slamdance | Los Angeles from 2026 (unverified) | — | Jan | — | — | — | slamdance.com |
| Outfest | Los Angeles, USA | 1982 | Jul | — | — | LGBTQ+ | outfest.org |
| Santo Domingo Global | Santo Domingo, Dominican Rep. | 2006 | Jan–Feb | 28 Jan–4 Feb | F | — | festivaldecineglobal.org |
| Los Cabos, FICUNAM, Ambulante, Guanajuato (GIFF), Monterrey, Shorts Mexico | Mexico | — | various | — | — | Los Cabos status irregular | — |
| Panama IFF, Icaro (Guatemala), CRFIC (Costa Rica), ttff (Trinidad & Tobago) | Central America and Caribbean | — | various | — | — | Panama status irregular | — |
| FICValdivia | Valdivia, Chile | 1994 | Oct | — | — | — | ficvaldivia.cl |
| Sanfic | Santiago, Chile | — | Aug | — | — | Sanfic Industria | — |
| Lima Film Festival (PUCP) | Lima, Peru | 1997 | Aug | — | — | Trofeo Spondylus | — |
| Mostra de São Paulo | São Paulo, Brazil | 1977 | Oct–Nov | — | — | Bandeira Paulista | mostra.org |
| É Tudo Verdade / It's All True | São Paulo & Rio, Brazil | 1996 | Apr | — | — | Documentary; Academy Documentary Feature qualifier [V] | etudoverdade.com.br |
| Brasília, Tiradentes, Bogotá (BIFF), Punta del Este, FICU Montevideo, EDOC (Ecuador), Mérida (Venezuela) | South America | — | various | — | — | Regional | — |

### Table 8. Asia-Pacific (excluding India), Middle East and Africa, tier 1

[V] cells are cited in Tables 1 and 4. All other cells are [BG] and should be checked against the URL shown.

| # | Festival | City, country | Lat, long [BG] | Founded [BG] | 2026 dates | FIAPF | Top prize | Key sections [BG] | Market [BG] | Main venues [BG] | URL [BG] |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Busan IFF (BIFF) | Busan, South Korea | 35.171, 129.128 | 1996 | 6–15 Oct [V]; attendance 200,043 [V] | A (new) | Busan Award, Best Film (KRW 50m) [V]; competition since 2025 | Competition, Gala, Icons, Jiseok, Window on Asian Cinema, Korean Cinema Today, World Cinema, Wide Angle, Open Cinema, On Screen, Midnight Passion | ACFM / Asian Project Market; Asian Cinema Fund | Busan Cinema Center, CGV Centum City | biff.kr |
| 2 | Tokyo IFF | Tokyo, Japan | 35.674, 139.760 | 1985 | 26 Oct (FIAPF) or 28 Oct (Screen)–4 Nov [V] | A | Tokyo Grand Prix [V] | Competition, Asian Future, Gala, Nippon Cinema Now, World Focus, Youth, Japanese Animation, Classics | TIFFCOM; Tokyo Gap-Financing Market | Tokyo Midtown Hibiya, TOHO Hibiya, Yurakucho Asahi Hall | 2026.tiff-jp.net |
| 3 | Shanghai IFF | Shanghai, China | 31.205, 121.436 | 1993 | 12–21 Jun (28th) [V]; 4,000+ entries [S] | A ("China's only A-festival") | Golden Goblet, Best Feature [V] | Main Competition, Asian New Talent, Documentary, Animation, Short [V]; Panorama, Belt & Road | SIFF Market and Project | Shanghai Grand Theatre, Film Art Centre | siff.com |
| 4 | Cairo IFF | Cairo, Egypt | 30.042, 31.224 | 1976 | 11–20 Nov (47th) [V]; 145 films [V] | A | Golden Pyramid [V] | International Competition, Horizons of Arab Cinema, Critics' Week, Shorts, Special Presentations, Classics | Cairo Industry Days / Cairo Film Connection | Cairo Opera House | ciff.org.eg |
| 5 | Red Sea IFF | Jeddah, Saudi Arabia | 21.485, 39.187 | 2019 (first ed. Dec 2021) | **2026 cancelled; 6th ed. Q4 2027** [V] | — | Golden Yusr (US$100k) [V] | Red Sea Competition, Spotlight, International and Arab Spectacular, Treasures, New Saudi/New Arab, Shorts, Family | Red Sea Souk; Fund; Labs (continue) [V] | Culture Square, Al-Balad | redseafilmfest.com |
| 6 | Marrakech IFF | Marrakech, Morocco | 31.626, -8.016 | 2001 | 20–28 Nov (23rd) [V]; 76 films, 39 countries [V] | — | Étoile d'Or [V] | Official Competition (14 first/second features) [V], Gala, Special Screenings, 11th Continent, Moroccan Panorama, Young Audience | Atlas Workshops (12 supported films in 2026) [V] | Palais des Congrès; Jemaa el-Fna | marrakech-festival.com |
| 7 | Golden Horse FF and Awards | Taipei, Taiwan | 25.052, 121.597 | Awards 1962; festival 1980 | Festival 6–22 Nov; awards 22 Nov [V] | — | Best Narrative Feature [V] | Awards for Chinese-language films; Gala, Window on Asia, Cinema Today | Golden Horse FPP; Film Academy | Taipei Music Center [V]; Ximending cinemas | goldenhorse.org.tw |
| 8 | Hong Kong IFF | Hong Kong SAR | 22.294, 114.170 | 1977 | Late Mar–Apr (not verified) | — | Firebird Awards | Gala, Firebird competitions, Filmmaker in Focus, Restored Classics | HAF (with FILMART) | HK Cultural Centre, City Hall, Xiqu Centre, M+ | hkiff.org.hk |
| 9 | FESPACO | Ouagadougou, Burkina Faso | 12.371, -1.520 | 1969 | **No 2026 edition**; biennial, odd years; 30th in 2027 | — | Étalon d'or de Yennenga [V] | Feature, Documentary, Short, Series, Animation, Diaspora | MICA | Ciné Burkina, Ciné Neerwaya | fespaco.bf |
| 10 | Carthage (JCC) | Tunis, Tunisia | 36.800, 10.180 | 1966 (annual since 2015) | Oct–Dec (not verified) | — | Tanit d'Or | Features, Docs, Shorts, Première Œuvre | Carthage Pro (Chabaka, Takmil) | Cité de la Culture | jcctunisie.org |
| 11 | El Gouna FF | El Gouna, Egypt | 27.395, 33.678 | 2017 | October (not verified) | — | El Gouna Golden Star | Feature Narrative, Documentary and Short competitions | CineGouna Platform | Conference and Culture Center | elgounafilmfestival.com |
| 12 | Doha FF / Ajyal (DFI) | Doha, Qatar | 25.360, 51.528 | Ajyal 2013; Doha FF Nov 2025 (check) | Nov–Dec (not verified) | — | Ajyal youth-jury awards; DFF prizes | — | Qumra; DFI grants | Katara Cultural Village | dohafilminstitute.com |
| 13 | Sydney FF | Sydney, Australia | -33.871, 151.207 | 1954 | 3–14 Jun [V] | F | Sydney Film Prize (A$60k) | Official Competition, Documentary Australia Award, Dendy Awards, First Nations Award | — | State Theatre | sff.org.au |
| 14 | Melbourne IFF | Melbourne, Australia | -37.816, 144.969 | 1952 | August | — | Bright Horizons (A$140k) | Bright Horizons, Australian Showcase, Night Shift, Accelerator Lab | 37°South; MIFF Premiere Fund | The Forum, ACMI | miff.com.au |
| 15 | Beijing IFF | Beijing, China | 40.002, 116.388 | 2011 | April | — | Tiantan Award | Tiantan competition, Beijing Film Panorama, Project Pitch, Market | Market | Huairou; Yanqi Lake | bjiff.com |
| 16 | FIRST Xining | Xining, China | 36.617, 101.778 | 2006 | Late July | — | Best Feature | Debut and second features, Short, Documentary | FIRST Venture Capital Initiative; FIRST Lab | Xining Grand Theatre | firstfilm.org.cn |
| 17 | Singapore IFF | Singapore | 1.294, 103.854 | 1987 | Nov–Dec | — | Silver Screen Awards, Asian Feature | Asian Feature Competition, SE Asian Shorts, Singapore Panorama | SAFF; Southeast Asian Film Lab | Capitol Theatre, The Projector | sgiff.com |
| 18 | Jeonju IFF | Jeonju, South Korea | 35.818, 127.144 | 2000 | Late Apr–May | — | International Competition Grand Prize | International, Korean, Short Competitions; Frontline; JCP premieres | Jeonju Project Market; JCP | Jeonju Cinema Town | jeonjufest.kr |
| 19 | BIFAN | Bucheon, South Korea | 37.504, 126.766 | 1997 | July | — | Bucheon Choice, Best Film | Bucheon Choice, Korean and World Fantastic, Forbidden Zone, BIFAN+ AI Film | NAFF; B.I.G. | Bucheon City Hall | bifan.kr |
| 20 | Durban IFF | Durban, South Africa | -29.866, 31.026 | 1979 | July | — | Best Feature Film | Feature, Documentary, South African, Short competitions | Durban FilmMart; Talents Durban | Suncoast Cinecentre | durbanfilmfest.co.za |
| 21 | Fajr IFF | Tehran, Iran | 35.758, 51.410 | 1983 | TBA [V] (national Feb; international Apr–May) | F | Crystal Simorgh | International Competition, Eastern Vista, Festival of Festivals | Fajr Film Market | Charsou Cineplex, Pardis Mellat | fajriff.com |
| 22 | Asia Pacific Screen Awards | Gold Coast, Australia | -28.000, 153.430 | 2007 | about 1–2 Nov | Awards body | APSA Best Film [V] | About 10 categories; MPA APSA Academy Film Fund (US$25k) | — | — | asiapacificscreenawards.com |
| 23 | Asian Film Awards | Hong Kong SAR | 22.302, 114.168 | 2007 | 16 Mar (19th) [V] | Awards body | Best Film | Run by AFA Academy (HKIFFS, Busan, Tokyo) | — | Xiqu Centre [V] | afa-academy.com |

Golden Apricot Yerevan (F, new; 12–19 Jul 2026), Eurasia (F; TBA) and Antalya Golden Orange (F; TBA) sit between Europe and Asia. They appear in Table 1 and in Table 9 below; the app should assign each to one region only. Busan, Tokyo, Cairo and Golden Horse accept entries free of charge, and Sydney and Singapore use FilmFreeway, but all of these submission details are [BG].

### Table 9. Asia-Pacific, Middle East and Africa, tier 2 (all [BG] unless marked)

| # | Festival (acronym) | City, country | Founded | Typical month | Top award | Market / notes | Website |
|---|---|---|---|---|---|---|---|
| 24 | Tokyo FILMeX | Tokyo, Japan | 2000 | Nov–Dec | Grand Prize | Talents Tokyo | https://filmex.jp |
| 25 | Yamagata International Documentary FF (YIDFF) | Yamagata, Japan | 1989 | Oct, odd years (2025, 2027) | Robert and Frances Flaherty Prize | New Asian Currents | https://www.yidff.jp |
| 26 | New Zealand IFF / Whānau Mārama | Auckland/Wellington + 11 cities, NZ | 1969 (Wellington), 1972 (Auckland) | Jul–Aug | NZIFF Best NZ Short / Aotearoa awards | Civic Theatre, Auckland | https://www.nziff.co.nz |
| 27 | Jogja-NETPAC Asian FF (JAFF) | Yogyakarta, Indonesia | 2006 | Late Nov–early Dec | Golden Hanoman | JAFF Market (since 2023) | https://jaff-filmfest.org |
| 28 | Eurasia IFF | Almaty/Astana, Kazakhstan | 1998 | Autumn (TBA 2026) [V: FIAPF accredited] | Grand Prix | | https://eurasiaiff.kz |
| 29 | Almaty Film Festival | Almaty, Kazakhstan | 2018 | Sept | Best Film | Central Asian cinema | https://almatyfilmfestival.com |
| 30 | Golden Apricot Yerevan IFF (GAIFF) | Yerevan, Armenia | 2004 | July; 2026: 12–19 Jul [V] | Golden Apricot | Regional Co-production Platform; FIAPF accredited [V] | https://gaiff.am |
| 31 | Antalya Golden Orange FF | Antalya, Türkiye | 1963 | Oct (TBA 2026) [V: FIAPF accredited] | Golden Orange | Antalya Film Forum | https://antalyaff.com |
| 32 | Istanbul Film Festival (IKSV) | Istanbul, Türkiye | 1982 | April | Golden Tulip | Meetings on the Bridge | https://film.iksv.org |
| 33 | Taipei Film Festival | Taipei, Taiwan | 1998 | Jun–Jul | Taipei Film Awards Grand Prize | Zhongshan Hall | https://www.taipeiff.taipei |
| 34 | Taiwan Int'l Documentary Festival (TIDF) | Taipei, Taiwan | 1998 | May | Grand Prize (Asian Vision) | TIDF Pitch | https://www.tidf.org.tw |
| 35 | Kaohsiung Film Festival | Kaohsiung, Taiwan | 2001 | Oct | Kaohsiung Awards (shorts, XR) | VR/XR focus | https://www.kff.tw |
| 36 | Hainan Island IFF (HIIFF) | Sanya, China | 2019 | Dec | Golden Coconut | | https://www.hiiff.com |
| 37 | Pingyao Int'l FF (PYIFF) | Pingyao, China | 2017 | Oct (not held some years) | Roberto Rossellini awards | Founded by Jia Zhangke | https://pyiffestival.com |
| 38 | Macao IFF & Awards (IFFAM) | Macau SAR | 2016 | Dec | Best Film | | https://www.iffam.com |
| 39 | Hong Kong Asian FF (HKAFF) | Hong Kong SAR | 2004 | Oct–Nov | New Talent Award | | https://www.hkaff.hk |
| 40 | Jecheon Int'l Music & FF (JIMFF) | Jecheon, South Korea | 2005 | Aug | Grand Prize | Music films | https://www.jimff.org |
| 41 | DMZ Int'l Documentary FF | Goyang/Paju, South Korea | 2009 | Sept | Grand Prize | DMZ Docs Industry | https://www.dmzdocs.com |
| 42 | QCinema IFF | Manila (Quezon City), Philippines | 2013 | Nov | Asian NextWave Best Film | QCinema Project Market | https://qcinema.ph |
| 43 | Cinemalaya Philippine Independent FF | Manila, Philippines | 2005 | Aug | Best Film (Balanghai) | | https://cinemalaya.org |
| 44 | Hanoi IFF (HANIFF) | Hanoi, Vietnam | 2010 | Nov, every 2 years | Best Film | | https://haniff.vn |
| 45 | Ho Chi Minh City IFF (HIFF) | Ho Chi Minh City, Vietnam | 2024 | Apr | Best Film | | https://hiff.vn |
| 46 | Luang Prabang FF | Luang Prabang, Laos | 2010 | Dec | Non-competitive | Southeast Asian focus | https://lpfilmfest.org |
| 47 | Bangkok Asian FF / World FF of Bangkok | Bangkok, Thailand | 2003 (WFFBKK) | Nov | Lotus awards | | https://worldfilmbkk.com |
| 48 | Malaysia IFF (MIFFest) | Kuala Lumpur, Malaysia | 2017 | Jul | Golden Global Awards | | https://miffest.com |
| 49 | Dhaka IFF (DIFF) | Dhaka, Bangladesh | 1992 | Jan | Best Film (Asian Competition) | Rainbow Film Society; West Meets East pitch | https://dhakafilmfestival.org |
| 50 | Kathmandu Int'l Mountain FF (KIMFF) | Kathmandu, Nepal | 2000 | Dec | Best Film | Himalayan Film Lab | https://kimff.org |
| 51 | Colombo IFF | Colombo, Sri Lanka | 2016? [unclear] | Varies | Best Film | Irregular; low confidence | (not found) |
| 52 | Pakistan IFF (PIFF) | Karachi, Pakistan | 2023? [low confidence] | Varies | | Also: Lahore Int'l Children's FF (2005, Nov) | (not found) |
| 53 | Tbilisi IFF | Tbilisi, Georgia | 2000 | Dec | Golden Prometheus | Caucasus | https://tbilisiff.ge |
| 54 | Adelaide Film Festival | Adelaide, Australia | 2003 | Oct | Feature Fiction Award | AFF Investment Fund | https://adelaidefilmfestival.org |
| 55 | Brisbane Int'l FF (BIFF) | Brisbane, Australia | 1992 | Oct–Nov | | | https://biff.com.au |
| 56 | Doc Edge | Auckland/Wellington, NZ | 2005 | May–Jun | Best Feature Documentary | Oscar-qualifying [BK] | https://docedge.nz |
| 57 | Saudi Film Festival | Dhahran, Saudi Arabia | 2008 | Apr–May | Golden Palm | At Ithra | https://saudifilmfestival.org |
| 58 | Amman Int'l FF (Awal Film) | Amman, Jordan | 2020 | Jul | Black Iris Award | Amman Film Industry Days | https://ammanfilmfestival.com |
| 59 | Jerusalem FF | Jerusalem, Israel | 1984 | Jul | Haggiag Award | Pitch Point | https://jff.org.il |
| 60 | Haifa IFF | Haifa, Israel | 1983 | Sep–Oct | Golden Anchor (Mediterranean) | | https://haifaff.co.il |
| 61 | Docaviv | Tel Aviv, Israel | 1998 | May | Best Israeli Documentary | | https://docaviv.co.il |
| 62 | Cinéma Vérité IDF | Tehran, Iran | 2007 | Dec | Best Documentary | | https://cinemaverite.ir |
| 63 | Duhok IFF | Duhok, Iraq (Kurdistan) | 2012 | Oct | Best Kurdish Film | | https://duhokiff.com |
| 64 | Luxor African FF | Luxor, Egypt | 2012 | Mar | Golden Mask of Tutankhamun | | https://luxorafricanfilmfestival.com |
| 65 | Aswan Int'l Women FF | Aswan, Egypt | 2017 | Feb–Mar | Best Feature | | https://aswanwomenff.com |
| 66 | Ismailia Int'l FF for Documentary & Shorts | Ismailia, Egypt | 1991 | Feb–Mar | Best Documentary | | (official site not confirmed) |
| 67 | Alexandria Mediterranean FF | Alexandria, Egypt | 1979 | Sep–Oct | Golden Nefertiti | | (not confirmed) |
| 68 | Khouribga African FF | Khouribga, Morocco | 1977 | Jun | Grand Prix Ousmane Sembène | | (not confirmed) |
| 69 | Africa Int'l FF (AFRIFF) | Lagos, Nigeria | 2010 | Nov | Globe Awards | | https://afriff.com |
| 70 | Encounters South African Int'l Documentary FF | Cape Town/Johannesburg, South Africa | 1999 | Jun | Best Documentary | | https://encounters.co.za |
| 71 | Joburg Film Festival | Johannesburg, South Africa | 2016 | Oct–Nov | Best Feature | Joburg Film Market | https://joburgfilmfestival.co.za |
| 72 | Zanzibar IFF (ZIFF) | Stone Town, Tanzania | 1997 | Jun–Jul | Golden Dhow | At the Old Fort | https://ziff.or.tz |
| 73 | Mashariki African FF | Kigali, Rwanda | 2015 | Mar | Golden Impala | | https://mashariki.rw |
| 74 | Kalasha Int'l Film & TV Market/Awards | Nairobi, Kenya | 2009 | Nov–Dec | Kalasha Award | Kenya Film Commission | https://kalasha.org |
| 75 | Hong Kong Film Awards (HKFA) | Hong Kong SAR | 1982 | Apr (ceremony) | Best Film (2026: *Ciao UFO* [V]) | Awards, not a festival | https://www.hkfaa.com |

Rows 51 (Colombo) and 52 (Pakistan) are low-confidence, and Pingyao's 2025–26 status is unclear. Verify them before loading.

### Specialised festival tables (documentary, short, animation, genre, identity, youth, human rights, environment)

These tables come from the specialised-festival research. In them, **† marks unverified background fields** (founding year, month, top-award name, website), equivalent to [BG] elsewhere. A **bold** 2026 date was verified. Qualifying columns use the 98th Academy list ([AMPAS98](https://www.oscars.org/sites/oscars/files/2024-11/98th_qualifying_festival_list_all_shorts.pdf), [AMPAS98-DF](https://oscars.org/sites/oscars/files/2024-10/98_Full_Qualifying_Festival_List_Combined.pdf)) with codes LA, AN, DOC, GEN and DF. They also use the 2025-awards BAFTA British Short Film list ([BAFTA25](https://www.bafta.org/wp-content/uploads/2024/09/british_short_film_qualifying_festivals_list_2025-1.pdf)), the 40th-cycle EFA Short Film Network ([EFA40](https://europeanfilmacademy.org/about/european-film-academy-short-film-network)) and the [FIAPF 2026 calendar](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf) ("A" or "Acc"). A "—" means the festival was not found on that list.

#### Documentary
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| IDFA | Amsterdam, NL | 1988 | Nov | **12–22 Nov** ([IDFA](https://festival.idfa.nl/en/idfa-2026-2/)) | IDFA Award Best Feature-Length Doc [AMPAS98-DF] | DF, DOC | Y | — | — | idfa.nl |
| CPH:DOX | Copenhagen, DK | 2003 | Mar | — | DOX:AWARD [AMPAS98-DF] | DF | Y | — | — | cphdox.dk |
| Hot Docs | Toronto, CA | 1993 | Apr–May | **23 Apr–3 May** [FIAPF26] | Best Int'l Feature Doc [AMPAS98-DF] | DF, DOC | Y | — | Acc | hotdocs.ca |
| Sheffield DocFest | Sheffield, UK | 1994 | Jun | — | Grand Jury Award [AMPAS98-DF] | DF, GEN | Y | — | — | sheffdocfest.com |
| Visions du Réel | Nyon, CH | 1969 | Apr | — | Int'l Feature Comp. Grand Jury Prize [AMPAS98-DF] | DF, GEN | Y | — | — | visionsdureel.ch |
| DOK Leipzig | Leipzig, DE | 1955 | Oct | — | Golden Dove [AMPAS98-DF] | DF, AN, DOC | Y | — | — | dok-leipzig.de |
| Yamagata IDFF | Yamagata, JP | 1989 | Oct, odd years | No 2026 edition (biennial†) | Robert & Frances Flaherty Prize [AMPAS98-DF] | DF | — | — | — | yidff.jp |
| True/False | Columbia, MO, US | 2004 | Late Feb–Mar | — | Non-competitive (True Vision Award†) | — | — | — | — | truefalse.org |
| It's All True | São Paulo & Rio, BR | 1996 | Apr | — | Best Doc, Int'l Comp. [AMPAS98-DF] | DF, DOC | — | — | — | etudoverdade.com.br |
| DMZ Docs | Goyang/Paju, KR | 2009 | Sep | — | Grand Prize [AMPAS98-DF] | DF | — | — | — | dmzdocs.com |
| DOC NYC | New York, US | 2010 | Nov | — | Grand Jury Prize† | GEN | Y | — | — | docnyc.net |
| Ji.hlava IDFF | Jihlava, CZ | 1997 | Oct | — | Best World Doc [AMPAS98-DF] | DF | — | — | — | ji-hlava.com |
| Thessaloniki Doc FF | Thessaloniki, GR | 1999 | Mar | — | Golden Alexander [AMPAS98-DF] | DF | — | — | — | filmfestival.gr |
| Doclisboa | Lisbon, PT | 2002 | Oct | — | Grand Prize† | GEN | — | — | — | doclisboa.org |
| Millennium Docs Against Gravity | Warsaw + cities, PL | 2004 | May | — | Grand Prix [AMPAS98-DF] | DF | — | — | — | mdag.pl |
| DocAviv | Tel Aviv, IL | 1998 | May | — | Best Int'l Film [AMPAS98-DF] | DF, GEN | — | — | — | docaviv.co.il |
| Doc Edge | Auckland/Wellington, NZ | 2005 | Jun | — | Best Int'l Feature [AMPAS98-DF] | DF, GEN | — | — | — | docedge.nz |
| DocVille | Leuven, BE | 2005 | May | — | Jury Award [AMPAS98-DF] | DF | — | — | — | docville.be |
| Punto de Vista | Pamplona, ES | 2005 | Apr | **20–25 Apr** [FIAPF26] | Grand Prize† | — | — | — | Acc | puntodevistafestival.com |
| ZINEBI | Bilbao, ES | 1959 | Nov | **20–27 Nov** [FIAPF26] | Grand Prix† | GEN, DOC | Y | Y | Acc | zinebi.eus |
| Full Frame | Durham, NC, US | 1998 | Apr | — | Grand Jury Award† | GEN | — | — | — | fullframefest.org |
| Camden IFF | Camden/Rockport, ME, US | 2005 | Sep | — | Harrell Award† | GEN | Y | — | — | pointsnorthinstitute.org |
| Big Sky Doc FF | Missoula, MT, US | 2003 | Feb | — | Best Feature/Short† | GEN, DOC | — | — | — | bigskyfilmfest.org |
| Hot Springs Doc FF | Hot Springs, AR, US | 1992 | Oct | — | — | DOC | — | — | — | hsdfi.org |
| DokuFest | Prizren, XK | 2002 | Aug | — | — | — | Y | Y | — | dokufest.com |
| Open City Documentary | London, UK | 2011 | Sep | — | — | — | Y | — | — | opencitylondon.com |
| Cinéma du Réel | Paris, FR | 1978 | Mar | — | Grand Prix† | — | — | — | — | cinemadureel.org |
| FIPADOC | Biarritz, FR | 2019 (successor to FIPA) | Jan | — | Grand Prix† | — | — | — | — | fipadoc.com |

#### Short film
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Clermont-Ferrand ISFF | Clermont-Ferrand, FR | 1979 (int'l comp. from 1988) | Late Jan–Feb | **30 Jan–7 Feb** [FIAPF26] | Grand Prix | GEN | Y | Y | **A** | clermont-filmfest.org |
| Oberhausen | Oberhausen, DE | 1954 | Late Apr–May | **28 Apr–3 May** [FIAPF26] | Grand Prize of the City of Oberhausen | GEN | Y | Y | Acc | kurzfilmtage.de |
| Tampere FF | Tampere, FI | 1970 | Mar | **4–8 Mar** [FIAPF26] | Grand Prix | GEN, LA, DOC | Y | Y | Acc | tamperefilmfestival.fi |
| Palm Springs ShortFest | Palm Springs, CA, US | 1995 | Jun | — | Best of the Festival | GEN, AN, DOC, LA | Y | — | — | psfilmfest.org |
| Interfilm | Berlin, DE | 1982 | Nov | — | Int'l Competition Awards | AN, LA | — | — | — | interfilm.de |
| REGARD | Saguenay, QC, CA | 1996 | Mar | — | Grand Prix | GEN | — | — | — | festivalregard.com |
| Kraków FF | Kraków, PL | 1961 | Late May–Jun | **31 May–7 Jun** [FIAPF26] | Golden Dragon / Golden Horn | GEN, AN, DOC, LA, DF | Y | Y | Acc | krakowfilmfestival.pl |
| Aspen ShortsFest | Aspen, CO, US | 1991 | Apr | — | Best Short | AN, GEN, DOC, LA | Y | — | — | aspenfilm.org |
| HollyShorts | Los Angeles, US | 2005 | Aug | — | Grand Prize | GEN, AN, LA, DOC | Y | — | — | hollyshorts.com |
| Go Short | Nijmegen, NL | 2009 | Apr | — | Grand Prix | AN, DOC, LA, GEN | Y | Y | — | goshort.nl |
| Vienna Shorts | Vienna, AT | 2004 | May–Jun | — | — | GEN | Y | Y | — | viennashorts.com |
| Kurzfilmtage Winterthur | Winterthur, CH | 1997 | Nov | — | Grand Prize | GEN | Y | Y | — | kurzfilmtage.ch |
| Uppsala Short FF | Uppsala, SE | 1982 | Oct | — | Uppsala Grand Prix | GEN | Y | Y | — | shortfilmfestival.com |
| Kurzfilm Festival Hamburg | Hamburg, DE | 1985 | Jun | — | — | — | Y | Y | — | festival.shortfilm.com |
| Curtas Vila do Conde | Vila do Conde, PT | 1993 | Jul | — | Grand Prize | GEN | Y (new) | Y | — | festival.curtas.pt |
| Drama ISFF | Drama, GR | 1978 | Sep | — | Golden Dionysus | GEN | Y (new) | Y | — | dramafilmfestival.gr |
| Leuven ISFF | Leuven, BE | 1995 | Nov–Dec | — | — | GEN | Y | Y | — | kortfilmfestival.be |
| Brest European Short FF | Brest, FR | 1986 | Nov | — | Grand Prix | — | Y | — | — | filmcourt.fr |
| Encounters | Bristol, UK | 1995 | Sep | — | Grand Prix | — | Y | Y | — | encounters.film |
| Busan ISFF | Busan, KR | 1980 | Apr–May | — | Grand Prix | GEN | Y | — | — | bisff.org |
| Flickerfest | Sydney, AU | 1991 | Jan | — | Best Int'l Short | GEN, AN, DOC | Y | — | — | flickerfest.com.au |
| Show Me Shorts | Auckland, NZ | 2006 | Oct–Nov | — | Best Film | GEN | Y | — | — | showmeshorts.co.nz |
| Curta Cinema | Rio de Janeiro, BR | 1991 | Nov | — | — | GEN | Y | — | — | curtacinema.com.br |
| Vilnius Short FF | Vilnius, LT | 2007 | Jan | — | — | GEN | — | Y | — | vilniusshorts.lt |
| PÖFF Shorts | Tallinn, EE | 2013 | Nov | — | — | LA, AN, GEN | Y | Y | (A, parent) | poff.ee |
| Glasgow Short FF | Glasgow, UK | 2007 | Mar | — | Bill Douglas Award | — | Y | — | — | glasgowshort.org |
| London Short FF | London, UK | 2004 | Jan | — | — | — | Y | — | — | shortfilms.org.uk |

#### Animation
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Annecy | Annecy, FR | 1960 | Jun | **21–27 Jun** (moved to avoid the G7 summit; [AWN](https://www.awn.com/news/annecy-shifts-2026-festival-dates)) [FIAPF26] | Cristal | GEN | — | — | **A** | annecyfestival.com |
| Ottawa IAF | Ottawa, CA | 1976 | Sep | — | Grand Prize | AN | — | — | — | animationfestival.ca |
| Animafest Zagreb | Zagreb, HR | 1972 | Jun | — | Grand Prix | GEN | — | — | — | animafest.hr |
| Hiroshima Animation Season (successor to Hiroshima Int'l Animation Festival, 1985–2020†) | Hiroshima, JP | 2022 (biennial; 2026 = 3rd ed.) | Aug | **19–23 Aug** ([Skwigly](https://www.skwigly.co.uk/hiroshima-animation-season-2026-official-selection-international-jury-and-trailer-revealed/)) | Grand Prix (Short Comp.) | GEN | — | — | — | animation.hiroshimafest.org |
| Stuttgart ITFS | Stuttgart, DE | 1982 | Apr–May | — | Grand Prix | GEN | — | — | — | itfs.de |
| Fantoche | Baden, CH | 1995 | Sep | — | Best Film | GEN | — | — | — | fantoche.ch |
| ANIMA Brussels | Brussels, BE | 1982 | Feb–Mar | — | Grand Prix | GEN | — | — | — | animafestival.be |
| Anifilm | Liberec, CZ | 2010 | May | — | — | GEN | — | — | — | anifilm.cz |
| Animator | Poznań, PL | 2008 | Jul | — | Golden Pegasus | GEN | — | — | — | animator-festival.com |
| Animest | Bucharest, RO | 2006 | Oct | — | — | GEN | — | — | — | animest.ro |
| CINANIMA | Espinho, PT | 1977 | Nov | — | Grand Prize | GEN | — | — | — | cinanima.pt |
| Fest Anča | Žilina, SK | 2008 | Jul | — | — | AN | — | — | — | festanca.sk |
| BIAF (Bucheon Int'l Animation Festival) | Bucheon, KR | 1999 | Oct | — | Grand Prix | GEN | — | — | — | biaf.or.kr |
| Animayo | Gran Canaria, ES | 2006 | May | — | — | GEN | — | — | — | animayo.com |
| ChileMonos | Santiago, CL | 2012 | May | — | — | AN | — | — | — | chilemonos.cl |
| Manchester Animation Festival | Manchester, UK | 2015 | Nov | — | — | GEN | — | — | — | manchesteranimationfestival.co.uk |
| KaBoom | Utrecht/Amsterdam, NL | 2014 | Mar | — | — | GEN | — | — | — | kaboomfestival.nl |
| Animation Dingle | Dingle, IE | 2008 | Mar | — | — | GEN | — | — | — | animationdingle.com |
| Spark Animation | Vancouver, CA | 2010 | Oct | — | — | GEN | — | — | — | sparkcg.org |
| SIGGRAPH Computer Animation Festival | US/Canada (rotating) | 1974 (conference) | Jul–Aug | — | Best in Show | GEN | — | — | — | siggraph.org |
| Imaginaria | Conversano, IT | 2003 | Aug | — | — | AN | — | — | — | imaginariafilmfestival.org |
| Animafilm | Baku, AZ | 2019 | Dec | — | — | — | Y (new, for animation; [Skwigly](https://www.skwigly.co.uk/animafilm-international-animation-festival-becomes-bafta-qualifying-festival/)) | — | — | — |

#### Fantastic / genre
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Sitges | Sitges, ES | 1968 | Oct | **8–18 Oct** [FIAPF26] | Best Feature Film | GEN, AN | — | — | Acc | sitgesfilmfestival.com |
| Fantasia | Montreal, CA | 1996 | Jul–Aug | — | Cheval Noir | — | — | — | — | fantasiafestival.com |
| Fantastic Fest | Austin, TX, US | 2005 | Sep | **17–24 Sep** [FIAPF26] | Best Picture (per section) | — | — | — | Acc | fantasticfest.com |
| BIFAN | Bucheon, KR | 1997 | Jul | — | Best of Bucheon | — | — | — | — | bifan.kr |
| BIFFF | Brussels, BE | 1983 | Apr | — | Golden Raven | — | — | — | — | bifff.net |
| NIFFF | Neuchâtel, CH | 2000 | Jul | — | H.R. Giger "Narcisse" Award | — | — | — | — | nifff.ch |
| Gérardmer | Gérardmer, FR | 1994 (successor to Avoriaz 1973–93) | Late Jan–Feb | — | Grand Prix | — | — | — | — | festival-gerardmer.com |
| Fantasporto | Porto, PT | 1981 | Feb–Mar | — | Best Film | — | — | — | — | fantasporto.com |
| Strasbourg European Fantastic FF | Strasbourg, FR | 2008 | Sep | — | Octopus d'or | — | — | — | — | strasbourgfestival.com |
| FrightFest | London, UK | 2000 | Aug | — | — (non-competitive) | — | — | — | — | frightfest.co.uk |
| Screamfest | Los Angeles, US | 2001 | Oct | — | Best Feature | — | — | — | — | screamfestla.com |
| Noir in Festival | Milan/Como, IT | 1991 | Dec | TBA [FIAPF26] | Raymond Chandler Award | — | — | — | Acc | noirfest.com |

#### LGBTQ+
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| BFI Flare | London, UK | 1986 | Mar | — | — (shorts prizes) | — | Y | — | — | bfi.org.uk/flare |
| Frameline | San Francisco, US | 1977 | Jun | — | Audience Awards | — | Y | — | — | frameline.org |
| Outfest LA | Los Angeles, US | 1982 | Jul | — | Grand Jury Prizes | — (not on 98th list) | Y | — | — | outfest.org |
| Kashish Mumbai Int'l Queer FF | Mumbai, IN | 2010 | May–Jun | — | Best Narrative/Doc | — | — | — | — | mumbaiqueerfest.com |
| Mardi Gras Film Festival | Sydney, AU | 1993 | Feb | — | — | — | — | — | — | queerscreen.org.au |
| Iris Prize | Cardiff, UK | 2007 | Oct | — | Iris Prize (cash prize for shorts) | — | Y | — | — | irisprize.org |
| Out On Film | Atlanta, US | 1987 | Sep–Oct | — | — | LA | Y | — | — | outonfilm.org |
| SQIFF | Glasgow, UK | 2015 | Sep–Oct | — | — | — | Y | — | — | sqiff.org |
| TEDDY Award (Berlinale section award) | Berlin, DE | 1987 | Feb | — | TEDDY | DF (Best Doc) [AMPAS98-DF] | — | — | (Berlinale A) | teddyaward.tv |
| Inside Out | Toronto, CA | 1991 | May–Jun | — | — | — | — | — | — | insideout.ca |

#### Children and youth
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Giffoni | Giffoni Valle Piana, IT | 1971 | Jul | — | Gryphon Awards | — | — | — | — | giffonifilmfestival.it |
| SCHLINGEL | Chemnitz, DE | 1996 | Sep–Oct | — | — | — | — | — | — | ff-schlingel.de |
| Zlín Film Festival | Zlín, CZ | 1961 | May–Jun | — | Golden Slipper | — | — | — | — | zlinfest.cz |
| LUCAS | Frankfurt, DE | 1974 | Sep–Oct | — | — | — | — | — | — | lucas-filmfestival.de |
| Chicago Int'l Children's FF | Chicago, US | 1983 | Oct–Nov | — | — | AN, LA | — | — | — | cicff.org |
| NY Int'l Children's FF | New York, US | 1997 | Feb–Mar | — | Grand Prize | AN, LA | — | — | — | nyicff.org |
| Cinekid | Amsterdam, NL | 1987 | Oct | — | — | — | — | — | — | cinekid.nl |
| BUFF Malmö | Malmö, SE | 1984 | Mar | — | — | — | — | — | — | buff.se |
| Cinema Jove | Valencia, ES | 1986 | Jun | **19–27 Jun** [FIAPF26] | Luna de Valencia | — | — | — | Acc | cinemajove.com |
| Olympia Int'l FF for Children & Young People | Pyrgos, GR | 1997 | Dec | — | — | — | — | — | — | olympiafestival.gr |
| Berlinale Generation (section) | Berlin, DE | 1978 | Feb | — | Crystal Bears | — | — | — | (Berlinale A) | berlinale.de |

#### Student, film school and cinematography
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| EnergaCamerimage | Toruń, PL | 1993 | Nov | — | Golden Frog | DOC | — | — | — | camerimage.pl |
| FAMUFEST (FAMU student festival) | Prague, CZ | 1983 | Spring | — | — | — | — | — | — | famufest.cz |
| Kraków FF (see Short film) | Kraków, PL | 1961 | May–Jun | **31 May–7 Jun** | Golden Dragon | multi | Y | Y | Acc | — |
| FILMSCHOOLFEST Munich | Munich, DE | 1981 | Nov | — | VFF Young Talent Award | — | — | — | — | filmschoolfest-munich.de |
| Sehsüchte | Potsdam, DE | 1972 | Apr–May | — | — | — | — | — | — | sehsuechte.de |
| Poitiers Film Festival | Poitiers, FR | 1977 | Dec | — | Grand Prix | — | — | — | — | poitiersfilmfestival.com |
| Molodist (originally a student festival) | Kyiv, UA | 1970 | Oct (TBA 2026) | TBA [FIAPF26] | Scythian Deer | — | Y | — | Acc | molodist.com |
| BAFTA Student Awards (award, not festival) | London/LA | — | — | — | — | — | Y [BAFTA25] | — | — | bafta.org |

#### Experimental
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Ann Arbor Film Festival | Ann Arbor, MI, US | 1963 | Mar | — | Best of Festival | GEN, AN, LA | — | — | — | aafilmfest.org |
| EMAF | Osnabrück, DE | 1981 | Apr | — | — | — | — | — | — | emaf.de |
| Images Festival | Toronto, CA | 1987 | Apr | — | — | — | — | — | — | imagesfestival.com |
| Media City FF | Windsor, CA | 1994 | May | — | — | — | — | — | — | mediacityfilmfestival.com |
| Courtisane | Ghent, BE | 2002 | Mar–Apr | — | — | — | — | — | — | courtisane.be |

#### Human rights
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| One World | Prague, CZ | 1999 | Mar | — | Best Film | — | — | — | — | oneworld.cz |
| FIFDH | Geneva, CH | 2003 | Mar | — | Grand Prix | — | — | — | — | fifdh.org |
| Movies That Matter | The Hague, NL | 2006 | Mar | — | Grand Jury Documentary [AMPAS98-DF] | DF | — | — | — | moviesthatmatter.nl |
| Human Rights Watch FF | London / New York, UK/US | 1988 | Mar / Jun | — | non-competitive | — | — | — | — | ff.hrw.org |
| FiSahara | Sahrawi refugee camps (Tindouf), DZ | 2003 | Oct | — | White Camel | — | — | — | — | fisahara.org |

#### Environmental, nature and outdoor
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Wildscreen | Bristol, UK | 1982 | Oct, biennial | — | Panda Awards | — | — | — | — | wildscreen.org |
| Jackson Wild Summit | Jackson Hole, WY, US | 1991 | Sep | — | Grand Teton Award | — | — | — | — | jacksonwild.org |
| CinemAmbiente | Turin, IT | 1998 | Jun | — | — | — | — | — | — | cinemambiente.it |
| DC Environmental FF | Washington DC, US | 1993 | Mar | — | — | — | — | — | — | dceff.org |
| Mountainfilm | Telluride, CO, US | 1979 | May | — | Charlie Fowler Award | GEN | — | — | — | mountainfilm.org |
| Banff Mountain FF | Banff, CA | 1976 | Oct–Nov | — | Grand Prize | — | — | — | — | banffcentre.ca |

#### Women's film
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Festival International de Films de Femmes de Créteil | Créteil, FR | 1979 | Mar–Apr | — | Grand Prix | — | — | — | — | filmsdefemmes.com |
| Seoul Int'l Women's FF | Seoul, KR | 1997 | Aug–Sep | — | — | — | — | — | — | siwff.or.kr |
| IFFF Dortmund+Köln | Dortmund/Cologne, DE | 1984 (merged 2006) | Apr | — | Int'l Feature Award | — | — | — | — | frauenfilmfestival.eu |
| Reel Sisters of the Diaspora | Brooklyn, NY, US | 1997 | Oct | — | — | LA | — | — | — | reelsisters.org |
| Athena Film Festival | New York, US | 2011 | Feb–Mar | — | — | — | — | — | — | athenafilmfestival.com |

#### Black and African diaspora
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| Pan African Film & Arts Festival | Los Angeles, US | 1992 | Feb | — | — | LA, DOC, AN | — | — | — | paff.org |
| FESPACO | Ouagadougou, BF | 1969 | Feb–Mar, odd years | No 2026 edition (biennial†) | Étalon d'or de Yennenga | DF, DOC | — | — | — | fespaco.bf |
| American Black FF | Miami, US | 1997 | Jun | — | — | GEN | Y | — | — | abff.com |
| BlackStar | Philadelphia, US | 2012 | Aug | — | — | DOC, LA | Y | — | — | blackstarfest.org |
| Martha's Vineyard African American FF | Oak Bluffs, MA, US | 2002 | Aug | — | — | GEN | — | — | — | mvaaff.com |
| Urbanworld | New York, US | 1997 | Sep–Oct | — | — | LA | — | — | — | urbanworld.org |
| BronzeLens | Atlanta, US | 2009 | Aug | — | — | GEN | — | — | — | bronzelens.com |
| BUFF (British Urban FF) | London, UK | 2005 | Sep | — | — | — | Y | — | — | britishurbanfilmfestival.com |
| Durban IFF | Durban, ZA | 1979 | Jul | — | Best Feature | GEN, DF | — | — | — | diff.ukzn.ac.za |

#### Indigenous
| Festival | City, Country | Est.† | Month† | 2026 dates | Top award† | AMPAS | BAFTA | EFA | FIAPF | Website† |
|---|---|---|---|---|---|---|---|---|---|---|
| imagineNATIVE | Toronto, CA | 2000 | Oct | — | — | LA | — | — | — | imaginenative.org |
| Skábmagovat | Inari, FI | 1999 | Jan | — | — | — | — | — | — | skabmagovat.fi |
| Maoriland FF | Ōtaki, NZ | 2014 | Mar | — | — | — | — | — | — | maorilandfilm.co.nz |
| Wairoa Māori FF | Wairoa, NZ | 2005 | Jun | — | — | — | — | — | — | — |
| Red Nation FF | Los Angeles, US | 1995 | Nov | — | — | — | — | — | — | rednationff.com |
| LA Skins Fest | Los Angeles, US | 2007 | Nov | — | — | — | — | — | — | laskinsfest.com |
| Dreamspeakers | Edmonton, CA | 1995 | Sep | — | — | — | — | — | — | dreamspeakers.org |

Submission platforms for specialised festivals are also †. Clermont-Ferrand uses Short Film Depot. Oberhausen, Annecy, IDFA, Sheffield, Visions du Réel, CPH:DOX and Hot Docs run their own entry systems. Most North American festivals use FilmFreeway, and many European short festivals use Festhome, Short Film Depot or Reelport. Final deadlines usually fall three to five months before the festival, and biennial festivals open calls about a year ahead. FilmFreeway's curated [Academy Award qualifying festivals](https://filmfreeway.com/festivals/curated/academy-award-qualifying-festivals) listing is a useful cross-check. One verified 2026 data point: **Hiroshima Animation Season ran 19–23 Aug 2026 (3rd edition) with 3,181 submissions from 110 countries**, and its Short Film Competition Grand Prix confers Academy eligibility ([Skwigly](https://www.skwigly.co.uk/hiroshima-animation-season-2026-official-selection-international-jury-and-trailer-revealed/)). Annecy moved its 2026 dates to avoid the G7 summit ([AWN](https://www.awn.com/news/annecy-shifts-2026-festival-dates)).

## Markets drew record crowds in 2026 while deals and studios thinned

Festivals with markets attached are where films are sold, and both of Europe's big markets reported growth in 2026. **The Marché du Film at Cannes had about 16,000 participants from more than 140 countries** (up from 15,000+ in 2025), with 1,700 buyers, 600 exhibiting companies, 1,500 screenings and 250 industry events. The festival itself accredited about 40,000 professionals ([Marché du Film](https://www.marchedufilm.com/news/the-marche-du-film-maintains-record-levels-of-participation-and-confirms-its-global-leadership/); [Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film)). **EFM in Berlin had more than 12,500 professionals (up 5%), 1,794 buyers and 606 films with an 83.17% market-premiere rate** ([Berlinale](https://www.berlinale.de/en/2026/news-press-releases/277528.html)). A trade commentary summed EFM up as "attendance up, deals down" ([Filmtake](https://www.filmtake.com/?p=43470)). The mood at Cannes matched: fewer and more deliberate meetings, private equity filling gaps left by weaker pre-sales, and, for the first time since 2017, no major-studio tentpole. Japan, the Country of Honour, saw about 50% higher attendance and launched a Japan IP Market ([Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film)). TIFF added a formal film market at the Metro Toronto Convention Centre in 2026 ([Wikipedia](https://en.wikipedia.org/wiki/2026_Toronto_International_Film_Festival)).

Model each market, forum, lab or fund as its own entity linked to a parent festival or organisation. Markets such as EFM and the Marché du Film have their own accreditation and fees, and several (Ventana Sur, FILMART, AFM) are standalone. Arab-world funding shifts in 2026 because Red Sea is paused. Its Fund and Labs continue, but the late-year calendar now leans on Cairo Film Connection, Marrakech's Atlas Workshops and Carthage Pro ([Screen Daily](https://www.screendaily.com/news/red-sea-international-film-festival-postponed-until-2027/5220602.article)). No 2026 project counts or grant totals were verified for any market or fund. The founding years and timings in both tables below are [BG].

### Table 10. Markets, forums, labs and funds: Europe and the Americas [BG]

| Parent festival / body | Market, forum, lab or fund | Timing [BG] |
|---|---|---|
| Cannes | Marché du Film (incl. Cannes Docs, Cannes Next, Producers Network); La Fabrique Cinéma | May |
| Berlinale | European Film Market (EFM); Berlinale Co-Production Market; Berlinale Talents; World Cinema Fund | February |
| Venice | Venice Production Bridge (Gap-Financing Market, Book Adaptation Rights Market); Biennale College Cinema; Final Cut in Venice | Aug–Sep |
| TIFF | TIFF Industry Conference; new film market (2026, [V]) | September |
| Sundance | Sundance Institute labs and grants (year-round); informal sales market | Year-round / January |
| Locarno | Locarno Pro (Match Me!, Heritage Online, First Look); Open Doors; BaseCamp | August |
| San Sebastián | Europe-Latin America Co-Production Forum; WIP Latam; WIP Europa; Ikusmira Berriak; Elías Querejeta Zine Eskola | September |
| Karlovy Vary | Eastern Promises Industry Days (Works in Progress, First Cut+) | July |
| IFFR | CineMart; Rotterdam Lab; Hubert Bals Fund; Rotterdam Pro | Jan–Feb |
| Annecy | MIFA (animation market) | June |
| Clermont-Ferrand | Marché du Film Court | Jan–Feb |
| IDFA | IDFA Forum ([V](https://professionals.idfa.nl/markets/co-producing-co-financing/attend-idfa-forum/)); Docs for Sale; IDFA Bertha Fund | November |
| CPH:DOX | CPH:FORUM; CPH:CONFERENCE; CPH:MARKET | March |
| Hot Docs | Hot Docs Forum; Deal Maker; Doc Shop | Apr–May |
| Tallinn Black Nights | Industry@Tallinn & Baltic Event | November |
| Warsaw | Warsaw Next / CentEast Market | October |
| Sarajevo | CineLink Co-production Market | August |
| Thessaloniki | Agora (Crossroads, Agora Docs) | November |
| Rome | MIA (Mercato Internazionale Audiovisivo) | October |
| Torino | TorinoFilmLab | November |
| Sitges | Sitges Pitchbox | October |
| Málaga | MAFIZ | March |
| Göteborg | Nordic Film Market | Jan–Feb |
| Haugesund | New Nordic Films | August |
| Fantasia | Frontières | Jul–Aug |
| Sheffield DocFest | MeetMarket | June |
| Mar del Plata | MdP WIP / Industria | November |
| BAFICI | BAL (Buenos Aires Lab) | April |
| Guadalajara | Industry / Co-production Meeting | April |
| Morelia | Impulso Morelia (WIP) | October |
| Cartagena | Encuentros Cartagena | April |
| Havana | Nuevas Miradas (EICTV); Havana Industry Days | December |
| Festival do Rio / Gramado | RioMarket / Gramado Film Market | October / August |
| Tribeca | Tribeca X; Through Her Lens | June |
| SXSW | SXSW Conference & Trade Show | March |
| Standalone | Ventana Sur, Buenos Aires (Marché du Film + INCAA); AFM (Santa Monica until 2024, then Las Vegas); NFDC/WAVES Film Bazaar, Goa (with IFFI) | Late Nov–Dec; November; November |

### Table 11. Markets, forums, labs and funds: Asia-Pacific, Middle East and Africa [BG except where marked]

| Market / fund | Parent | Founded | Timing | Notes | URL |
|---|---|---|---|---|---|
| Asian Contents & Film Market (ACFM), incl. Asian Project Market (APM, ex-PPP 1998) | Busan IFF | ACFM 2006 (as Asian Film Market) | Oct, during BIFF | Asia's largest festival market; APM is a pitching co-pro market | https://www.acfm.kr |
| Asian Cinema Fund (ACF) | Busan IFF | 2007 | Annual call | Script development, post-production and documentary funds (AND fund) | https://www.biff.kr |
| Hong Kong-Asia Film Financing Forum (HAF) | HKIFFS / FILMART | 2000 | March | Pitches, WIP lab, HAF Goes to Cannes | https://www.haf.org.hk |
| FILMART | HKTDC | 1997 | March | Major Asian rights market | https://www.hktdc.com/event/hkfilmart |
| TIFFCOM; Tokyo Gap-Financing Market | Tokyo IFF / UNIJAPAN | TIFFCOM 2004 | Late Oct–Nov | Rights and IP market | https://tiffcom.jp |
| Golden Horse Film Project Promotion (FPP) | Golden Horse FF | 2007 | Nov | Chinese-language projects | https://www.goldenhorse.org.tw |
| TCCF (Taipei Creative Content Fest) | TAICCA | 2020 | Nov | Pitching and market | https://tccf.taicca.tw |
| SIFF Project / Co-Financing Forum | Shanghai IFF | ~2007 | June | | https://www.siff.com |
| FIRST Venture Capital Initiative / FIRST Lab | FIRST Xining | ~2013 | July | | https://www.firstfilm.org.cn |
| Jeonju Cinema Project (JCP) / Jeonju Project Market | Jeonju IFF | 2014 (JCP) | April–May | Finances features that premiere at Jeonju | https://www.jeonjufest.kr |
| NAFF (Network of Asian Fantastic Films) | BIFAN Bucheon | 2008 | July | Genre projects | https://www.bifan.kr |
| Southeast Asian Film Financing (SAFF) Project Market | Singapore IFF | ~2014 | Nov–Dec | Plus Southeast Asian Film Lab | https://sgiff.com |
| Talents Tokyo | Tokyo FILMeX | 2010 | Nov | Berlinale Talents partner | https://filmex.jp |
| Purin Pictures | Private, Thailand | 2017 | Biannual | SE Asian grants | https://purinpictures.org |
| SEAFIC (Southeast Asia Fiction Film Lab) | Independent, Thailand | 2018 | Annual | Script lab | https://seafic.org |
| 37°South Market / MIFF Premiere Fund | Melbourne IFF | 2004 / 2007 | Aug | Australia's main co-finance market | https://miff.com.au |
| Adelaide Film Festival Investment Fund | AFF | 2003 | | | https://adelaidefilmfestival.org |
| Red Sea Fund; Red Sea Souk (Project Market, WIP, Souk Awards); Red Sea Labs | Red Sea Film Foundation | Fund 2021 | Souk in Dec (none 2026) | Arab, African and Asian filmmakers | https://redseafilmfest.com |
| Doha Film Institute Grants; Qumra | DFI, Qatar | Grants 2010; Qumra 2015 | Spring and fall grant cycles; Qumra in March | MENA and world-cinema grants | https://www.dohafilminstitute.com |
| CineGouna Platform (SpringBoard, Bridge) | El Gouna FF | 2017 | Oct | Arab projects | https://elgounafilmfestival.com |
| Cairo Film Connection / Cairo Industry Days | Cairo IFF | 2018 (CFC) | Nov | Arab projects | https://ciff.org.eg |
| Chabaka; Takmil (WIP) | Carthage JCC | 2014 / 2015 | Nov–Dec | Arab and African projects | https://jcctunisie.org |
| Atlas Workshops (Ateliers de l'Atlas) | Marrakech IFF | 2018 | Nov–Dec | Africa and Arab world | https://marrakech-festival.com |
| AFAC Cinema Program | Arab Fund for Arts and Culture, Beirut | 2007 | Annual | | https://www.arabculturefund.org |
| Durban FilmMart (DFM) | Durban FilmMart Institute | 2010 | July | Africa's leading co-pro market | https://durbanfilmmart.co.za |
| MICA (Marché International du Cinéma et de l'Audiovisuel Africain); Ouaga Film Lab | FESPACO | MICA 1983 | Feb–Mar, odd years | | https://fespaco.bf |
| Realness African Screenwriters' Residency | Realness Institute, South Africa | 2016 | | | https://realness.institute |
| Saudi Film Commission / Daw Film Competition | Saudi Ministry of Culture | 2020 | | National funding | https://film.moc.gov.sa |

## Between 3,000 and 16,000 festivals exist, depending on what counts

No single count of the world's festivals holds up, because the numbers depend on definitions. **Stephen Follows's 2013 census found 9,706 festivals that had run at least once in 15 years, of which only 2,954 were active**, meaning they had run within the previous two years. He combined 12 directories and estimated 90–95% accuracy. The same data showed a young, fragile and North American circuit. About 75% of festivals had been founded in the previous decade, about 39% ran only once, fewer than a quarter were more than six years old, and about 70% were in North America. 77% screened shorts, half had a competition, half ran under seven days, and October had about five times as many festivals as December ([Stephen Follows](https://stephenfollows.com/many-film-festivals-are-in-the-world/)). The University of St Andrews puts the number at "more than 10,000… and still rising" and dates the first festival to Venice in 1932 ([St Andrews](https://www.st-andrews.ac.uk/film-studies/research/impact/film-festivals/)). Wikidata holds **16,177 film-festival items**, but only about half have a country and 653 have coordinates, which suggests many thin bulk-imported entries (live query, 26 Nov 2026). The defensible public statement for the app is "about 3,000 active festivals, 10,000+ ever held", with both dates shown. No post-2020 census and no verified FilmFreeway count were found.

Big-festival economics rest on public money and on commissioned impact studies. **The Berlinale's budget is about €33M, and federal funding was cut from €12.9M (2025) to €11.9M for 2026.** The festival earns 60% of its budget itself, and director Tricia Tuttle has warned of cuts in 2027–28 ([Screen Daily](https://www.screendaily.com/news/berlinale-facing-funding-shortfall-in-2027-and-2028-warns-festival-director/5213254.article); [Bundestag hib 34/2026](https://www.bundestag.de/presse/hib/kurzmeldungen-1136674)). Impact figures come from the festivals' own reports and use differing methods (gross versus net new spending), so the app should label them "festival-reported" and never rank festivals by them.

### Table 12. Festival-reported scale and economic statistics

| Festival / market | Year | Metric | Value | Source |
|---|---|---|---|---|
| Berlinale | 2026 | Budget; federal (BKM) funding; Berlin Senate funding | about €33M; €11.9M (cut from €12.9M); €1M | [Screen Daily](https://www.screendaily.com/news/berlinale-facing-funding-shortfall-in-2027-and-2028-warns-festival-director/5213254.article); [Bundestag](https://www.bundestag.de/presse/hib/kurzmeldungen-1136674) |
| Berlinale | 2026 | Films shown; self-generated share of budget; 2025 sponsorship growth | 218 (55 German); 60%; +27% | [Bundestag](https://www.bundestag.de/presse/hib/kurzmeldungen-1136674) |
| EFM | 2026 | Professionals; buyers; films; market premieres; speakers | 12,500+ (+5%); 1,794; 606; 83.17%; 369 | [Berlinale](https://www.berlinale.de/en/2026/news-press-releases/277528.html) |
| Cannes / Marché du Film | 2026 | Accredited professionals; Marché participants; buyers; exhibitors; screenings | about 40,000; about 16,000 from 140+ countries; 1,700; 600; 1,500 | [Marché du Film](https://www.marchedufilm.com/news/the-marche-du-film-maintains-record-levels-of-participation-and-confirms-its-global-leadership/) |
| Sundance | 2025 | Attendance; economic impact (Utah); jobs | 85,000+ (+17% on 2024, about −40% on 2020); nearly $200M; 2,600+ | [KPCW](https://www.kpcw.org/park-city/2025-09-02/report-sundance-attendance-jumps-17-at-2025-festival); [Sundance report](https://www.sundance.org/wp-content/uploads/2025/07/2025-Sundance-Film-Festival-Attendance-Recap-and-Economic-Impact-Report.pdf) |
| TIFF | 2024 | Economic activity; tax revenue; visitors; films | $240M; $36M a year; 700,000+ over 11 days; 291 | [The Varsity](https://thevarsity.ca/2025/09/14/how-tiff-powers-torontos-economy/) |
| Busan | 2026 | Attendance | 200,043 (first time above 200k since 2015) | [Korea Times](https://www.koreatimes.co.kr/entertainment/films/20261015/iranian-film-midday-meal-wins-top-honor-at-31st-biff) |
| Cartagena (FICCI) | 2026 | Attendance | 65,000+ | [La República](https://www.larepublica.co/ocio/ficci-cerro-edicion-con-mas-de-65-000-asistentes-4382776) |
| Shanghai | 2026 | Entries | 4,000+ (record) | [Shanghai gov](https://english.shanghai.gov.cn/en-Latest-WhatsNew/20260520/b3fd5cdc4f3c4be7a6e4309240707489.html) |
| IFFI | 2026 | International films; submissions | 150+ (159) from 86 countries; 1,900+ or 1,400 (conflict) | [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2335780&reg=48&lang=2) |
| Hiroshima Animation Season | 2026 | Submissions | 3,181 from 110 countries | [Skwigly](https://www.skwigly.co.uk/hiroshima-animation-season-2026-official-selection-international-jury-and-trailer-revealed/) |

Not verified: the Cannes festival budget, the Venice/Biennale budget, Berlinale admissions (historically about 330,000 tickets [BG]), IFFR visits (about 300,000 [BG]), Clermont-Ferrand admissions (about 160,000 [BG]), Sundance 2026 attendance and TIFF 2025–26 economics. TIFF's 2026 ticket-price rises prompted "people's festival no more" complaints ([CP24](https://www.cp24.com/local/toronto/2026/08/31/peoples-festival-no-more-tiff-fans-grapple-with-ticket-price-hikes/)).

### Women still direct under a quarter of top competition films

**Cannes 2026 had 5 of 22 competition films directed by women (about 23%), down from 7 of 22 in 2025.** Organisers said women directed 34% of all features in the official programme, or 38% including shorts. Only three women have won the Palme d'Or, most recently Justine Triet in 2023. Thierry Frémaux rejected quotas, and Collectif 50/50 accused the festival of "feminism washing" ([CP24/AFP](https://www.cp24.com/news/entertainment/2026/05/11/cannes-film-festival-defends-male-dominated-competition/)). Venice 2026 jury president Maggie Gyllenhaal called the two female-directed competition films "a systemic problem" ([TheWrap](https://www.thewrap.com/creative-content/movies/maggie-gyllenhaal-female-directors-venice/)). A July report quoted a Venice chief citing a single female director in competition ([World of Reel](https://www.worldofreel.com/blog/2026/7/23/venice-film-festival-chief-on-one-female-director-in-competition-shes-the-only-one-we-found-of-adequate-quality)), so the count is unresolved between one and two. The data lesson is that shares must be computed **per section**, because competition and full-programme figures diverge sharply. Jury-gender, race and ethnicity series were not compiled.

### 2025–26 trends that change the data model

Five trends from 2025–26 affect how the data is modelled. **Sundance held its final Park City edition in January 2026 and moves to Boulder for 21–31 Jan 2027**, across 11 venues ([Variety AU](https://au.variety.com/2026/film/global/sundance-film-festival-2027-dates-boulder-colorado-33520/); [Axios Denver](https://www.axios.com/local/denver/2025/03/27/boulder-sundance-film-festival-2027)). Location therefore belongs to the edition. Red Sea's postponement and MAMI's cancelled 2025 edition show that the edition `status` field must take cancelled and postponed values ([Screen Daily](https://www.screendaily.com/news/mumbai-film-festival-cancels-2025-edition/5207162.article)). FIAPF's reform makes accreditation an edition-level fact. Generative-AI rules are appearing: Cinema St. Louis will bar generative-AI films from its festival from 2027 ([St. Louis Public Radio](https://www.stlpr.org/text/arts/2026-09-08/cinema-st-louis-limits-ai-use-festival-films)). A claimed Cannes 2026 AI ban comes only from a low-quality blog and is unverified ([aifilms.ai](https://studio.aifilms.ai/blog/cannes-2026-ai-ban-official-selection)). Finally, public funding is tightening (the Berlinale cut) and studios are pulling back from Cannes and Venice ([Screen Daily](https://www.screendaily.com/features/six-talking-points-from-the-venice-2026-lineup-studios-and-female-directors-go-missing/5218857.article)). An `ai_policy` text field on the edition record is worth adding.

Research on festivals is well organised and can supply editorial context. The Film Festival Research Network bibliography by Marijke de Valck and Skadi Loist is one starting point ([UvA DARE](https://dare.uva.nl/id/afc9e635-cee1-405e-9c68-8cd7d4397903)). Others are their overview "Film Festival Studies: An Overview of a Burgeoning Field" ([PDF](https://is.muni.cz/el/phil/podzim2012/FAVz032/37474845/De_Valck__Marijke__and_Skadi_Loist_Film_Festival_Studies_An_Overview_of_a_Burgeoning_Field.pdf?lang=en)), the edited volume *Film Festivals: History, Theory, Method, Practice* ([Routledge](https://www.routledge.com/Film-Festivals-History-Theory-Method-Practice/de-Valck-Kredell-Loist/p/book/9780415712477)) and Dina Iordanova's St Andrews programme and *Film Festival Yearbook* series ([St Andrews](https://www.st-andrews.ac.uk/film-studies/research/impact/film-festivals/)). The journal *Film Festival Studies* (since 2023) and filmfestivalresearch.org are [BG].

## Accreditation, location and status belong to the edition, not the festival

The central modelling decision is to split the stable **Festival** from the yearly **Edition**. Every fact that changed in 2025–26 is edition-level: FIAPF accreditation and A status, location (Sundance), status (Red Sea, MAMI), mode (in-person, hybrid or online), dates, jury and winners. Premiere status belongs on the **Selection** (a film in a section of an edition), not on the Film. EFM's 83% market-premiere rate shows that premiere status is a metric even for markets. schema.org's `ScreeningEvent` (with `workPresented` pointing to a `Movie`, plus `superEvent`/`subEvent`, `eventStatus`, `eventAttendanceMode` and `previousStartDate`) covers publishing screenings, but it has no Festival-edition, Award or Jury types, so the internal model has to be richer ([schema.org](https://schema.org/ScreeningEvent)).

### Table 13. Proposed entities and key fields

| Entity | Key fields | Notes |
|---|---|---|
| Festival | id, wikidata_qid, name, short_name, original_name, founded_year (+ source_tag), organiser, website, region, categories[] (general, documentary, short, animation, genre, LGBTQ+, children, human rights, environment, women, Black/diaspora, Indigenous, experimental, student), parallel_sections_owner | QID is the dedup key; region assigned once (e.g. Yerevan, Antalya) |
| Edition | festival_id, number, year, start_date, end_date, city, venue_ids[], status (scheduled / cancelled / postponed / rescheduled), mode (in-person / hybrid / online), fiapf_accredited, fiapf_a_festival, theme, director, budget, public_funding (+ level), admissions, accredited_professionals, films_screened, submissions, economic_impact_reported (+ study_author), ai_policy, source_url, verified_at | Matches schema.org `eventStatus` / `eventAttendanceMode`; store conflicting values (IFFI submissions, Tokyo start date) with sources |
| Section | edition_id, name, competitive (bool), type (main competition, sidebar, shorts, parallel/independent, market) | Parallel sections (Directors' Fortnight, Critics' Week, Giornate) flagged as independent |
| Film | title, original_title, year, countries (ISO 3166), languages (ISO 639), runtime, wikidata_qid, imdb_id, tmdb_id | |
| Selection | film_id, section_id, premiere_status (world / international / continental / national / regional / local / none) | Premiere status lives here |
| Screening | selection_id, venue_id, datetime, format, subtitle_language (BCP 47), ticket_url | Maps to `ScreeningEvent` |
| Venue | name, address, lat, long, capacity, screens, osm_id, wikidata_qid, coord_source | Coordinates tagged geocoded vs approximate |
| Person | name, gender (nullable, self-identified), nationality, wikidata_qid, imdb_id | Enables per-section gender statistics |
| Credit | person_id, film_id, role | Director, producer, cast |
| Jury / JuryMember | edition_id, section_id; person_id, role (president / member) | |
| Award / Prize | edition_id, name, category, prize_money (+ currency); film_id and/or person_id, won (bool), ex_aequo (bool) | Shared prizes (Cannes Best Director 2026) need ex_aequo |
| Qualification | festival_id, body (AMPAS / BAFTA / EFA / FIAPF), list_version (e.g. "98th"), codes (LA, AN, DOC, GEN, DF), valid_from, valid_to | Shows "last verified list" in the UI |
| Market / Fund | name, parent_festival_id or organisation, type (market, co-pro forum, lab, fund, WIP), edition dates, url, accreditation_fee | Standalone markets have no parent |
| Registration | edition_id, portal_url, category (professional, student, media), fee, currency, tax_included | IFFI/IFFK Rs 1,180 incl. GST |
| SourceTag (on every field group) | value_source_url, tag (V / S / BG), checked_at | Drives the "unverified" badge |

Publish each Edition as JSON-LD (`Festival`, a subtype of `Event`) and each screening as a `ScreeningEvent`, with `sameAs` pointing to the Wikidata item. Store Wikidata QIDs for deduplication and joins. Google's Event rich results require `name`, `startDate` and `location` with a PostalAddress, and recommend `eventStatus`, `endDate`, `image`, `offers`, `organizer` and `previousStartDate`. Google warns: "When the event status changes, DON'T remove the startDate" ([Google Search Central](https://developers.google.com/structured-data/events/), updated 2026-09-08). For calendar export, generate a per-festival and an all-festivals `.ics` from the same records, using all-day dates with an exclusive DTEND and a stable UID such as `<QID>-<year>@domain`. The ICS details come from general knowledge, not a fetched RFC.

## Wikidata, FIAPF and OSM can feed the guide; commercial film APIs need licences

**No open, licensed, machine-readable worldwide festival directory exists.** The best workable stack has four layers. Wikidata is the CC0 backbone for festivals, editions, awards and IDs. FIAPF's yearly PDF and each festival's site supply current dates and accreditation. The Academy, BAFTA and EFA PDFs supply qualifying status. OpenStreetMap supplies venues under ODbL. The large submission directories (FilmFreeway, Festhome, Short Film Depot) offer no public directory API. FilmFreeway's API is a Submissions API that festivals switch on for their own entries ([FilmFreeway help](https://filmfreeway.com/help/article/16110/add-an-api-key); [API ToS, updated 2026-08-13](https://filmfreeway.com/page/api-terms-of-service)). Third-party scrapers exist, but they show demand rather than permission, so treat these platforms as link-out targets ([Apify actor](https://apify.com/versusmedia/festival-api-actor)).

Wikidata was tested live on 26 Nov 2026. A festival query returned **16,177 distinct festivals in 7.5 s**. Of those, 8,221 had a country (P17), 653 coordinates (P625), 14,263 a website (P856) and 2,292 an inception date (P571). An editions query returned **4,139 editions of class Q27787439 in 1.8 s**, but only 917 had a start time (P580). A subclass path is required: Cannes (Q42369) is not a direct instance of film festival (Q220505), and `P31/P279*` adds about 190 items. Awards need a UNION pattern, because the Palme d'Or (Q179808) has no "conferred by" (P1027) statement. With the UNION, Cannes returned 22 awards and 753 wins, Berlin 22 and 617, and Venice 11 and 319, against only 84 rows for Cannes with P1027 alone. Nominations are almost absent: only 28 P1411 statements point to the Palme d'Or. Two back-to-back heavy queries triggered **HTTP 429**, and a label-search query hit the **60 s timeout** (HTTP 504). Run queries one at a time with gaps, send a descriptive User-Agent and gzip encoding, honour Retry-After, and use dumps for bulk pulls ([Wikidata:Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)). Licensing is CC0, and crediting Wikidata is requested but not required.

### Table 14. Data sources, licences and access

| Source | Provides | Licence / terms | Access and limits | Tested? |
|---|---|---|---|---|
| Wikidata (WDQS SPARQL) | Festivals, editions, awards, coordinates, websites, cross-IDs (IMDb P345, TMDB P4947/P4985 [BG]) | CC0 | 60 s timeout; 429 on bursts; User-Agent required ([Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)) | Yes, live |
| FIAPF calendar PDF | 49 accredited festivals, A marks, dates | Publicly posted PDF | Annual manual parse ([PDF](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf)); fiapf.org pages failed to fetch | Read |
| AMPAS qualifying lists | Shorts and Documentary Feature qualifiers | Public PDFs; "may change without notice" | 98th list latest found; queries to qualifyingfestivals@oscars.org ([AMPAS98-DF](https://oscars.org/sites/oscars/files/2024-10/98_Full_Qualifying_Festival_List_Combined.pdf)) | Read |
| BAFTA / EFA lists | British Short Film qualifiers; EFA Short Film Network | Public PDF / web page | 2025 BAFTA list and 40th EFA cycle read; 2027 BAFTA lists not fetched | Read |
| TMDB API | Film and person metadata, images | Free non-commercial with attribution ("This product uses the TMDB API but is not endorsed or certified by TMDB"); commercial needs a licence ([TMDB FAQ](https://developer.themoviedb.org/docs/faq)) | Rate limits not verified | Blocked by proxy |
| IMDb non-commercial datasets | Daily TSV: title.basics, akas, crew, principals, ratings, name.basics | Personal and non-commercial use only ([IMDb](https://data.imdb.com/non-commercial-datasets)) | **No festival or award data**; event pages governed by [conditions of use](https://m.imdb.com/conditions) | Blocked by proxy |
| Letterboxd API | Ratings, lists | By application ([api-beta](https://letterboxd.com/api-beta/)) | Terms not confirmed | No |
| JustWatch API | Streaming availability | Partner contract and token; branded links required ([docs](https://apis.justwatch.com/docs/api)) | — | No |
| OMDb | Film metadata | Not verified (about 1,000 requests/day free, CC BY-NC [BG]) | — | No |
| OSM Overpass | Cinemas (`amenity=cinema`) | ODbL: attribution and share-alike for distributed databases [BG] | overpass-api.de: under 10,000 queries and 1 GB per day, divided by 100 for regular use; wait 30 s after 429; commercial use should go to self-hosted or paid servers ([OSM wiki](https://wiki.openstreetmap.org/wiki/Overpass_API)). Servers "barely usable for over a year", with IP bans ([OSM Community](https://community.openstreetmap.org/t/overpass-api-performance-issues/140598?page=10)) | Blocked by proxy |
| Geofabrik extracts + osmium | Same cinema data, offline | ODbL | Avoids public-server quotas | No |
| Nominatim | Geocoding | Attribution required | Maximum 1 request/s, identifying User-Agent, cache results, no bulk geocoding, no autocomplete ([policy](https://operations.osmfoundation.org/policies/nominatim/)) | No |
| OpenFreeMap | Vector map tiles | Free, no key, commercial use allowed; attribution "© OpenMapTiles, Data from OpenStreetMap"; no SLA ([openfreemap.org](https://openfreemap.org)) | Unlimited on the public instance | No |
| OSM raster tiles | Map tiles | Visible attribution; valid Referer; no bulk or offline use; no SLA ([tile policy](https://operations.osmfoundation.org/policies/tiles/)) | Low-traffic only | No |
| CARTO basemaps | Map tiles | API key now required; 5M (non-commercial) or 1M (commercial) tile requests/month ([terms](https://www.carto.com/legal/basemap-terms/)) | Old keyless URLs to be avoided | No |
| Protomaps PMTiles | Self-hosted tiles | Single file served by HTTP range requests ([docs](https://docs.protomaps.com/deploy/)) | Planet file about 100 GB+; regional extracts on R2 or similar | No |
| Kaggle / Great Tables / Zenodo | Oscar datasets; 1,851 Cannes competition films 1946–present ([great_tables](https://posit-dev.github.io/great-tables/reference/data.films.html)) | Varies; licences not checked | Bulk download | No |
| Wikipedia tables | Records and winners lists | CC BY-SA (share-alike) | Parse tables; prefer Wikidata | No |
| Festhome / Short Film Depot / Cinando / Festival Scope / Eventival | Directories and industry databases | No public API found; Cinando is paywalled | Link out | No |

### Working SPARQL

All three queries ran on 26 Nov 2026. For full coverage, also include the edition classes Q27968043 and Q27968055 and the point-in-time property P585. Run the award query one festival at a time, because without the VALUES filter it may time out.

```sparql
# Q1 festivals (16,177 in 7.5 s)
SELECT ?fest ?festLabel ?countryLabel ?coord ?website ?inception WHERE {
  ?fest wdt:P31/wdt:P279* wd:Q220505 .
  OPTIONAL { ?fest wdt:P17 ?country . }
  OPTIONAL { ?fest wdt:P625 ?coord . }
  OPTIONAL { ?fest wdt:P856 ?website . }
  OPTIONAL { ?fest wdt:P571 ?inception . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul,fr,de,es". }
}

# Q2 editions (4,139 in 1.8 s)
SELECT ?edition ?editionLabel ?festLabel ?start ?end WHERE {
  ?edition wdt:P31 wd:Q27787439 .
  OPTIONAL { ?edition wdt:P179|wdt:P361 ?fest . }
  OPTIONAL { ?edition wdt:P580 ?start . }
  OPTIONAL { ?edition wdt:P582 ?end . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul". }
}

# Q3 award winners (Cannes, Berlinale, Venice)
SELECT ?festLabel ?award ?awardLabel ?winner ?winnerLabel ?year WHERE {
  VALUES ?fest { wd:Q42369 wd:Q130871 wd:Q49024 }
  { ?award wdt:P1027 ?fest }
  UNION { ?award wdt:P31 ?cls . ?cls wdt:P1027|wdt:P361 ?fest }
  UNION { ?award wdt:P361 ?fest . ?award wdt:P31/wdt:P279* wd:Q618779 }
  ?winner p:P166 ?st . ?st ps:P166 ?award .
  OPTIONAL { ?st pq:P585 ?year . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul". }
} ORDER BY ?festLabel ?awardLabel DESC(?year)
```

The Overpass query below is untested, because the proxy blocked it. It finds cinemas within 5 km of a festival coordinate; the useful tags are `name`, `website`, `wikidata`, `addr:*`, `screen` and `operator`.

```
[out:json][timeout:60];
nwr["amenity"="cinema"](around:5000,43.5513,7.0128);
out center tags;
```

### A refresh cadence that stays inside every usage policy

A scheduled GitHub Actions job can maintain the data without breaking any provider's policy. Run Wikidata festivals, editions and awards weekly (three to five serial queries with 5–10 s gaps). Rebuild the OSM cinema layer monthly from Geofabrik extracts filtered with osmium, and keep it as a separate ODbL file. Look up TMDB on demand, only for new QIDs, and cache by ID. Do a manual pass on the FIAPF, AMPAS, BAFTA and EFA PDFs each year. Commit the outputs as diffable JSON or CSV, and fail the job if festival counts drop by more than about 10%, which catches upstream breakage. GitHub disables scheduled workflows after 60 days without repository activity, so add a keepalive ([gh-action-keepalive](https://github.com/efrecon/gh-action-keepalive); [HackerNoon](https://hackernoon.com/your-github-actions-cron-job-can-disappear-without-failing)). The OSM wiki specifically asks users not to run Overpass from AI-generated app hosts such as lovable.app or netlify.app ([OSM wiki](https://wiki.openstreetmap.org/wiki/Overpass_API)). For maps, the recommended keyless setup is MapLibre GL JS with an OpenFreeMap style and a festival GeoJSON overlay. The style URL pattern (for example `tiles.openfreemap.org/styles/liberty`) is [BG].

### Open items the loader must fill before launch

The highest-value gaps are listed here so they can become tickets. Results due imminently: IFFI 2026 and Marrakech 2026 (both 28 Nov), IFFK 2026 (18 Dec) and IDFA 2026. Missing official lists: the 99th or 100th Academy qualifying-festival PDFs, the 2027 BAFTA lists (including the separate animation list) and EFA feature and documentary selection festivals. Unconfirmed 2026 dates: IFFR, SXSW, NYFF, CPH:DOX, HKIFF, Carthage, El Gouna, Doha, Fajr, Eurasia, Antalya and every specialised festival not marked in bold. Uncaptured details: market and fund 2026 figures, fees and deadlines for every festival, BIFFes 2026 venue and fees, and IFFK 2026 fees. Two FIAPF questions remain open: whether the four promised additional accreditations happened, and the reform's exact announcement date (the PDF is dated 11 Mar 2026). Every coordinate needs geocoding, and every [BG] or † field needs an automated URL and site check.

## Conclusion

The most useful finding for a builder is that the authoritative layer of the festival world is small, public and annual, while the long tail is large, unlicensed and stale. Forty-nine FIAPF festivals, about 200 Academy-qualifying bodies, 31 EFA network festivals and a few dozen BAFTA qualifiers can be loaded with high confidence from a handful of PDFs. The remaining 3,000-plus active festivals have to come from Wikidata's thin records and festival websites. The app should therefore show its confidence openly: verification tags, "last verified list" badges and source links are core product features, not footnotes. That matters most in India, where IFFI's A status, IFFK's December slot and BIFFes' January slot form a coherent circuit that no global directory describes well.

The 2025–26 disruptions are a design test rather than noise. Sundance moving, Red Sea pausing, MAMI cancelling, FIAPF re-tiering and Busan becoming a competition would each break a schema that treats a festival as one fixed row. A model keyed on editions, with status, location, accreditation and prize data stored per year and sourced field by field, absorbs these changes. The same structure also yields the crossover insights (*La bola negra*, *Lost Land*, *The Violinist*, *Moham*) that make a guide more useful than a list.
