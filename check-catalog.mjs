import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

const { festivals, films, honors, worldFestivals: hand = [] } = JSON.parse(readFileSync(new URL('./catalog.json', import.meta.url)));
// Extractor shards listed in data/shards.json are merged the same way app.js merges them.
const shardList = existsSync(new URL('./data/shards.json', import.meta.url)) ? JSON.parse(readFileSync(new URL('./data/shards.json', import.meta.url))) : [];
for (const path of shardList) {
  const shard = JSON.parse(readFileSync(new URL(`./${path}`, import.meta.url)));
  for (const record of shard.festivals || []) {  // same merge as app.js mergeFestivals: a known id only adds missing editions
    const known = festivals.find(festival => festival.id === record.id);
    if (!known) festivals.push(record);
    else known.editions.push(...record.editions.filter(edition => !known.editions.some(old => old.year === edition.year)));
  }
  films.push(...(shard.films || []));
  honors.push(...(shard.honors || []));
}
// Announced dates and results (data/announced), merged the way app.js merges them.
const { festivalWhen, mergeAnnounced } = createRequire(import.meta.url)('./calendar.js');
const announced = JSON.parse(readFileSync(new URL('./data/announced/announced.json', import.meta.url)));
const announcedIds = new Set([...festivals, ...hand].map(festival => festival.id));
for (const [id, list] of Object.entries(announced.editions)) for (const edition of list) {
  assert.ok(announcedIds.has(id) && Number.isInteger(edition.year) && new URL(edition.source).protocol === 'https:', `announced ${id}`);
  if (edition.jury) assert.ok(edition.jury.every(([name]) => name) && new URL(edition.jurySource).protocol === 'https:', `announced ${id} ${edition.year} jury needs names and a source`);
  assert.ok(edition.off || festivalWhen({ editions: [edition] }, new Date(edition.year, 0, 1)), `announced ${id} ${edition.year} dates must parse`);
}
mergeAnnounced([...festivals, ...hand], announced.editions);
films.push(...announced.films);
const imported = new Set(festivals.flatMap(festival => [festival.id, festival.wikidata]).filter(Boolean));
const worldFestivals = hand.filter(festival => !imported.has(festival.id));
assert.equal(new Set(films.map(film => film.id)).size, films.length);
for (const record of [...films, ...honors]) {
  assert.ok(festivals.some(festival => festival.id === record.festival && festival.editions.some(edition => edition.year === record.year)));
  for (const url of [...(record.sources || []), ...(record.awards || [record.award]).map(award => award[1])]) {
    assert.equal(new URL(url).protocol, 'https:');
  }
}
for (const format of ['Feature', 'Short film', 'Documentary']) assert.ok(films.some(film => film.format === format));
const ids = [...festivals, ...worldFestivals].map(festival => festival.id);
assert.equal(new Set(ids).size, ids.length, 'festival ids must be unique');
for (const festival of [...festivals, ...worldFestivals]) {
  assert.ok(Math.abs(festival.lat) <= 90 && Math.abs(festival.lon) <= 180, `${festival.id} needs coordinates`);
  if (festival.url) assert.equal(new URL(festival.url).protocol, 'https:');
}
for (const festival of worldFestivals) assert.ok(festival.name && festival.city && festival.country && festival.region && festival.month && festival.status === 'wip', festival.id);
const world = JSON.parse(readFileSync(new URL('./data/world-festivals/world-festivals.json', import.meta.url))).festivals;
assert.equal(new Set(world.map(record => record.id)).size, world.length, 'world festival ids must be unique');
for (const record of world) {
  assert.ok(/^Q\d+$/.test(record.id) && record.name && record.country && record.region, record.id);
  assert.ok(Math.abs(record.ll[1]) <= 90 && Math.abs(record.ll[0]) <= 180, `${record.id} needs coordinates`);
  if (record.logo) assert.ok(existsSync(new URL(`./${record.logo.file}`, import.meta.url)) && record.logo.license && record.logo.source, `${record.id} logo needs a file and licence`);
}
const { films: links } = JSON.parse(readFileSync(new URL('./data/youtube-links/youtube.json', import.meta.url)));
for (const [id, link] of Object.entries(links)) assert.ok(films.some(film => film.id === id) && /^Q\d+$/.test(link.wikidata) && link.youtube.length, `youtube link ${id}`);
// enrich shard: films it names must exist, and every poster must be a local file with its licence.
const enrichFilms = new URL('./data/enrich/films.json', import.meta.url);
if (existsSync(enrichFilms)) {
  const filmIds = new Set(films.map(film => film.id));
  for (const [id, extra] of Object.entries(JSON.parse(readFileSync(enrichFilms)).films)) {
    if (!filmIds.has(id)) continue;  // a film a later shard run dropped: the app ignores it, and enrich's next run removes it
    assert.ok(/^Q\d+$/.test(extra.wikidata), `enrich film ${id}`);
    if (extra.poster) assert.ok(existsSync(new URL(`./${extra.poster.file}`, import.meta.url)) && extra.poster.license && new URL(extra.poster.source).protocol === 'https:', `${id} poster needs a file and licence`);
  }
}
// Data freshness: every source needs an id and label; a date, if given here or in its shard's stamp, must parse.
const { sources } = JSON.parse(readFileSync(new URL('./sync.json', import.meta.url)));
assert.equal(new Set(sources.map(entry => entry.id)).size, sources.length, 'sync.json ids must be unique');
for (const entry of sources) {
  assert.ok(entry.id && entry.label, 'sync.json entries need an id and label');
  const stampFile = new URL(`./data/${entry.id}/sync.json`, import.meta.url);
  const updated = entry.updated || (existsSync(stampFile) && JSON.parse(readFileSync(stampFile)).updated);
  if (updated) assert.ok(!Number.isNaN(Date.parse(updated)), `${entry.id} has a bad updated date`);
}
// Calendar status (calendar.js) on fixed dates.
const iffi = { editions: [{ year: 2026, dates: '20–28 November' }, { year: 2025, dates: '20–28 November' }] };
const on = (record, y, m, d) => festivalWhen(record, new Date(y, m - 1, d))?.status;
assert.equal(on(iffi, 2026, 11, 26), 'now');
assert.equal(on(iffi, 2026, 11, 1), 'next');
assert.equal(on(iffi, 2026, 12, 1), 'over');
assert.equal(on(iffi, 2027, 11, 22), 'month');
assert.equal(on(iffi, 2027, 3, 1), 'next');
assert.equal(on({ editions: [{ year: 2026, dates: '29 December–5 January' }] }, 2027, 1, 3), 'now');
assert.equal(on({ month: 'October–November' }, 2026, 11, 26), 'month');
assert.equal(on({ month: 'December' }, 2026, 11, 26), 'next');
assert.equal(on({ month: 'June' }, 2026, 11, 26), 'over');
assert.equal(festivalWhen({ month: 'December' }, new Date(2026, 10, 26)).brief, 'usually in December');
assert.equal(festivalWhen({ editions: [{ year: 2025 }] }), null);
assert.equal(on({ month: 'December', editions: [{ year: 2026, off: 'postponed' }] }, 2026, 11, 26), 'over');
const impact = JSON.parse(readFileSync(new URL('./data/award-impact/impact.json', import.meta.url)));
for (const [qid, record] of Object.entries(impact.films)) assert.ok(/^Q\d+$/.test(qid) && [...record.won, ...record.nominated].every(([name, award, year]) => name && /^Q\d+$/.test(award) && (year === null || Number.isInteger(year))), `award impact ${qid}`);
console.log(`Validated ${films.length} films across ${festivals.length} festivals (${shardList.length} shards), plus ${worldFestivals.length} hand-listed and ${world.length} world festivals from Wikidata.`);
