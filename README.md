# Momentum Lab

A browser-based tool that turns a football match's event data into a "momentum seismograph" — a chart showing which team was dominating at every point in the match, with an automatically detected turning point.

Built for the Sports Analytics Hackathon (IUS Sarajevo, 11–13 November 2026) — Challenge 05: Match Momentum Lab.

**Live app:** https://claude.ai/artifact/7ZkZJ3XQnB6nUaDGsXfFvq

## What it does

Upload a StatsBomb-format match events CSV (one match, event-level data) and the app:

- Computes a weighted momentum score per team (shot quality / xG, pressing, dribbling) in rolling 5-minute windows
- Renders it as a diverging area chart — above the line = Team A dominant, below = Team B dominant
- Automatically detects and marks the biggest momentum swing ("turning point") of the match
- Marks goals on the timeline
- Lets you tune the weights live with sliders
- Validates the uploaded file and explains clearly what's missing if the format doesn't match (instead of failing silently)

Everything runs client-side in the browser — no backend, no install.

## Files

- `momentum_lab.html` — the app itself. Open it directly in any browser, or use the hosted link above.
- `make_csv.py` — fetches a match from [StatsBomb Open Data](https://github.com/statsbomb/open-data) and converts it into the CSV format the app expects.
- `data/` — four ready-to-upload sample matches, generated with `make_csv.py`:
  - 2022 World Cup Final — Argentina 3–3 France
  - Euro 2024 Final — Spain 2–1 England
  - 2023 Women's World Cup Final — Spain 1–0 England
  - Women's Euro 2025 Final — England 1–1 Spain

## Generating more matches

```bash
python make_csv.py
```

Edit the `MATCHES` dictionary at the top of the script with any `match_id` from StatsBomb's Open Data (see their [competitions list](https://github.com/statsbomb/open-data/blob/master/data/competitions.json)).

## Data & credit

Match data: [StatsBomb Open Data](https://github.com/statsbomb/open-data), free to use with attribution.
