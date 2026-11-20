#!/usr/bin/env python3
import json
from common import ROOT

def main():
    p=ROOT/'data/watchlist-snapshot.json'
    if not p.exists(): print('No local price snapshot supplied; no watchlist action taken.'); return
    data=json.loads(p.read_text()); hits=[x for x in data if x.get('hit')]
    print('Watchlist hits (report only):')
    for x in hits: print(f"- {x.get('game','?')}: {x.get('reason','signal')}")
    if not hits: print('- None')
if __name__ == '__main__': main()
