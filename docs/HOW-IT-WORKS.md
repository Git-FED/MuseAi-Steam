# How It Works

Muse follows a deliberately conservative loop:

1. **Daily sync** — when requested, read a public/exported Steam library snapshot and save a dated record.
2. **Cap check** — compare logged daily, weekly, and per-game hours with the proposed caps. Print alerts at 75%, 90%, and 100%, and write cap-hit reports.
3. **Watchlist check** — inspect configured targets or a supplied price snapshot. Report sale, price-drop, DLC, free, and new-release hits only.
4. **Discovery** — score candidate games against the taste profile, exclude the owned library, and prefer free or discounted candidates.
5. **Weekly report** — summarize hours, top games, cap events, watchlist hits, three discovery picks, and one backlog pick.

No step buys a game, launches a game, adds a friend, changes a profile, or changes Steam settings. Every external action needs Git-FED's exact order.
