import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const { festivals, films, honors, worldFestivals = [] } = JSON.parse(readFileSync(new URL('./catalog.json', import.meta.url)));
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
console.log(`Validated ${films.length} films across ${festivals.length} festivals, plus ${worldFestivals.length} listed as work in progress.`);
