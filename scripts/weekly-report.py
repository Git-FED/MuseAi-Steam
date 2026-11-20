#!/usr/bin/env python3
from common import ROOT, read_log, today
from collections import defaultdict

def main():
    rows=read_log(); totals=defaultdict(float)
    for r in rows:
        try: totals[r['game']]+=float(r['hours_delta'] or 0)
        except ValueError: pass
    lines=['# Weekly Muse Report — '+today(),'','## Hours this week',f'- Logged delta: {sum(totals.values()):.2f}h','', '## Top games in the current log']
    lines += [f'- {g}: {h:.2f}h' for g,h in sorted(totals.items(), key=lambda x:x[1], reverse=True)[:5]] or ['- No new playtime rows logged.']
    lines += ['','## Caps','- Run `python3 scripts/check-caps.py` for threshold details.','', '## Watchlist','- Run `python3 scripts/watchlist-check.py` for supplied price-feed hits.','', '## Discovery','- Run `python3 scripts/discover.py` for three candidate picks.','', '## Backlog pick','- Warframe (starter try-first list; confirm ownership before treating as a recommendation).']
    out=ROOT/'reports/weekly'/f'{today()}.md'; out.write_text('\\n'.join(lines)+'\\n', encoding='utf-8'); print(f'Wrote {out}')
if __name__ == '__main__': main()
