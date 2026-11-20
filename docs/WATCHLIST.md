# Watchlist

`config/watchlist.yaml` is a starter list. Fill it with games Git-FED actually wants monitored and set target prices in USD where relevant.

Supported report signals are sale, price drop, new DLC, free, and new release. The checker reads a supplied local price snapshot or future provider adapter. It emits hits only; it never buys, adds to a wishlist, or opens checkout.
