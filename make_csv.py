import json
import csv
import urllib.request
import sys

MATCHES = {
    3869685: "wc2022_final_argentina_france.csv",
    3943043: "euro2024_final_spain_england.csv",
    3906390: "wwc2023_final_spain_england.csv",
    4020846: "weuro2025_final_england_spain.csv",
}

BASE_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{}.json"

FIELDS = ["minute", "second", "team", "type", "player", "shot_statsbomb_xg", "shot_outcome", "dribble_outcome"]

def fetch(match_id):
    url = BASE_URL.format(match_id)
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def flatten(events):
    rows = []
    for e in events:
        row = {
            "minute": e.get("minute"),
            "second": e.get("second"),
            "team": (e.get("team") or {}).get("name"),
            "type": (e.get("type") or {}).get("name"),
            "player": (e.get("player") or {}).get("name", ""),
            "shot_statsbomb_xg": "",
            "shot_outcome": "",
            "dribble_outcome": "",
        }
        if "shot" in e:
            row["shot_statsbomb_xg"] = e["shot"].get("statsbomb_xg", "")
            row["shot_outcome"] = (e["shot"].get("outcome") or {}).get("name", "")
        if "dribble" in e:
            row["dribble_outcome"] = (e["dribble"].get("outcome") or {}).get("name", "")
        rows.append(row)
    return rows

for match_id, filename in MATCHES.items():
    print(f"Fetching match {match_id}...")
    events = fetch(match_id)
    rows = flatten(events)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    teams = sorted(set(r["team"] for r in rows if r["team"]))
    print(f"  Saved {filename} -- {len(rows)} rows, teams: {teams}")

print("Done.")
