# Caps

The values in `config/caps.yaml` are **PROPOSED, not set**. Git-FED must edit them before treating them as personal limits.

Muse calculates `usage / cap * 100` for total daily, total weekly, and configured per-game caps. It reports the first crossed thresholds at 75%, 90%, and 100%, then records any overrun. Daily values reset by calendar date; weekly values use ISO weeks. Quiet hours are a notification preference, not a hard block.

At 100%, Muse reports the cap hit and time over the proposed boundary. It cannot stop Steam remotely. If a future hard lock is desired, it would require a separately ordered local tool on the PC.
