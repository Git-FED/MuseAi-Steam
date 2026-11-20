#!/usr/bin/env python3
import json
from common import ROOT

def main():
    candidates=json.loads((ROOT/'data/discovery-candidates.json').read_text())
    owned={r['game'].lower() for r in __import__('common').read_log()}
    terms={'survival','mmo','anime','jrpg','card','open-world','free-to-play'}
    picks=[]
    for c in candidates:
        if c['title'].lower() in owned: continue
        score=len(terms & set(t.lower() for t in c.get('tags',[]))) + (3 if c.get('price_usd')==0 else 0)
        picks.append((score,c))
    print('Discovery picks — report only, not purchases:')
    for score,c in sorted(picks, key=lambda item: item[0], reverse=True)[:3]: print(f"- {c['title']} | score {score} | ${c.get('price_usd', 'unknown')}")
if __name__ == '__main__': main()
