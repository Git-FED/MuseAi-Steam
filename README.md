# Muse Steam Tracker

A local, reporting-first tracker for the Steam account **Fedpromptly** (`freethyself`). This package is intentionally local-only: no repository is created, no GitHub writes are performed, and no Manus-hosted website is required.

## Snapshot

- Source profile: <https://steamcommunity.com/id/Git-FED/games/?tab=all>
- Snapshot date: 2026-11-20
- Library: 243 games — 133 played, 110 never played
- Total playtime: 2,107 hours (approximately 88 days)
- Wallet: $0.01
- Highest playtime: Undawn (1,415.2h), Trails of Cold Steel III (113.2h), Yu-Gi-Oh! Duel Links (106.4h), Neverwinter (78h), Sword Art Online: Integral Factor (66.9h)

## What Muse does

Muse syncs data when asked, checks proposed playtime caps, watches configured wishlist signals, suggests new games that fit the taste profile, and produces daily/weekly/monthly reports. It watches and reports; it does not buy games, play games, add friends, trade, post reviews, request refunds, or change account settings without Git-FED's explicit order for that exact action.

Steam has no remote hard lock that Muse can enforce. Caps are tracking, warning, and logging rules. Alerts fire at 75%, 90%, and 100%; stopping play remains a human action or a separately ordered local PC tool.

## Quick start

1. Edit the proposed values in `config/caps.yaml`, `config/watchlist.yaml`, and `config/discovery-profile.yaml`.
2. Replace the starter library notes with the complete export when available.
3. Run a report from the project root:

   ```bash
   python3 scripts/weekly-report.py
   ```

4. Open `dashboard/index.html` directly in a browser for the local visual overview. It has no network dependency and uses a custom dark animated background with drifting ink-like ribbons, not orbital graphics.

Other scripts are safe report-only tools:

```bash
python3 scripts/check-caps.py
python3 scripts/watchlist-check.py
python3 scripts/discover.py
python3 scripts/sync-library.py --dry-run
```

`sync-library.py` requires an explicitly supplied export or URL and does not log in, store cookies, or mutate Steam.

## Data boundaries

The supplied specification did not include the complete 243-game export, private Steam credentials, or Google Drive save files. The package includes the known snapshot facts and clearly marked starter/index files rather than inventing missing records. Drop real exports into `data/library/` and update the indexes in `data/saves/` when Git-FED chooses.
