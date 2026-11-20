# Discovery

Discovery uses the actual playtime signals in `config/discovery-profile.yaml`, not guesses. It favors survival MMOs, anime MMORPGs, JRPGs, card battlers, and open-world survival, then filters out all owned titles and ranks free/sale candidates first.

Because no live store feed or complete 243-game export is bundled here, `discover.py` works from an optional local `data/discovery-candidates.json` file and explains when that feed is absent.
