import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const { festivals, films, honors } = JSON.parse(readFileSync(new URL('./dist/catalog.json', import.meta.url)));
assert.equal(new Set(films.map(film => film.id)).size, films.length);
for (const record of [...films, ...honors]) {
  assert.ok(festivals.some(festival => festival.id === record.festival && festival.editions.some(edition => edition.year === record.year)));
  for (const url of [...(record.sources || []), ...(record.awards || [record.award]).map(award => award[1])]) {
    assert.equal(new URL(url).protocol, 'https:');
  }
}
for (const format of ['Feature', 'Short film', 'Documentary']) assert.ok(films.some(film => film.format === format));
console.log(`Validated ${films.length} films across ${festivals.length} festivals.`);
