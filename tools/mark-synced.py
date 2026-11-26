"""Stamp data/<name>/sync.json with the time and record count after an extractor changed its shard.

The home page's Data freshness panel reads it for every source listed in sync.json.
Usage: python3 tools/mark-synced.py <name>
"""
import datetime
import json
import pathlib
import sys


def size(value):
    if isinstance(value, dict) and isinstance(value.get('count'), int):  # a shard can state its own record count
        return value['count']
    # shortcut: counts the longest top-level list (or the keys of a dict of records); pass a real count if a shard is shaped differently.
    lists = [item for item in (value.values() if isinstance(value, dict) else [value]) if isinstance(item, list)]
    return max(map(len, lists)) if lists else len(value) if isinstance(value, dict) else 0


name = sys.argv[1]
shard = pathlib.Path('data', name)
assert shard.is_dir(), f'{shard} does not exist'
records = sum(size(json.loads(path.read_text())) for path in sorted(shard.rglob('*.json')) if path.name != 'sync.json')
stamp = {'updated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'records': records}
(shard / 'sync.json').write_text(json.dumps(stamp, indent=2) + '\n')
print(f'{name}: {records} records, updated {stamp["updated"]}')
