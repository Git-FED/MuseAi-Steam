#!/usr/bin/env python3
from common import ROOT, read_log, parse_simple_yaml, today
from collections import defaultdict

def main():
    cfg = parse_simple_yaml(ROOT / 'config/caps.yaml')
    rows = read_log()
    daily = defaultdict(float)
    for row in rows:
        try:
            daily[row['game']] += float(row['hours_delta'] or 0)
        except ValueError:
            continue
    alerts = []
    for game, limits in cfg.get('per_game', {}).items():
        key = game.replace('_', ' ')
        actual = daily.get(key, daily.get(game, 0))
        cap = float(limits.get('daily', 0))
        if cap:
            pct = actual / cap * 100
            for threshold in cfg.get('alert_at', [75, 90, 100]):
                if pct >= threshold:
                    alerts.append(f'{key}: daily {actual:.2f}/{cap:g}h ({pct:.0f}%) — threshold {threshold}%')
    if alerts:
        out = ROOT / 'reports/cap-alerts' / f'{today()}-cap.md'
        body = '# Cap Alerts — ' + today() + '\n\n' + '\n'.join('- ' + a for a in alerts) + '\n'
        out.write_text(body, encoding='utf-8')
        print('\n'.join(alerts))
        print(f'Wrote {out}')
    else:
        print('No cap thresholds crossed in the current playtime log.')

if __name__ == '__main__':
    main()
