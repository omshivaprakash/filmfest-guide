"""Big Five extractor: editions, line-ups, winners and nominees of Cannes, Venice, Berlin, Toronto and Sundance.

    python3 tools/extractors/big-five/extract.py            # writes data/big-five/catalog.json
    python3 tools/extractors/big-five/extract.py --check    # self-test only, no network

Same sources, rules and licence as the world-editions extractor, whose code it reuses with its own festival list.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'world-editions'))
import extract as editions  # noqa: E402  (world-editions/extract.py)

editions.check()  # its self-test uses its own festival list, so run it before swapping ours in

editions.FESTIVALS = {'Q42369': 'Cannes', 'Q49024': 'Venice', 'Q130871': 'Berlinale', 'Q390018': 'TIFF', 'Q189887': 'Sundance'}
editions.HAND_IDS = {'Q42369': 'cannes', 'Q49024': 'venice'}  # hand-listed names differ from Wikidata's
editions.EXTRA_AWARDS = {}
editions.OUT = os.path.join(editions.ROOT, 'data', 'big-five', 'catalog.json')
editions.EXTRACTOR = 'tools/extractors/big-five/extract.py'

if __name__ == '__main__':
    editions.main()
