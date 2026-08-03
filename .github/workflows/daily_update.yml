import json
import os
from pathlib import Path
import pandas as pd

# 1. DYNAMICALLY REGISTER MLS IN SOCCERDATA CONFIG
def setup_soccerdata_config():
    config_dir = Path.home() / "soccerdata" / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    
    league_dict = {
        "USA-Major League Soccer": {
            "FBref": "Major League Soccer",
            "season_start": "Feb",
            "season_end": "Dec"
        }
    }
    
    config_file = config_dir / "league_dict.json"
    with open(config_file, "w") as f:
        json.dump(league_dict, f, indent=4)
    print(f"Registered custom MLS config at {config_file}")

# Execute config setup before importing soccerdata
setup_soccerdata_config()

import soccerdata as sd

def fetch_and_export_mls_betting_data():
    print("--- Initializing FBref MLS Scraper ---")
    
    # Initialize FBref scraper for Major League Soccer
    fbref = sd.FBref(leagues="USA-Major League Soccer", seasons="2026")

    # 1. SCHEDULE & FIXTURES
    print("1. Extracting Match Schedule...")
    try:
        schedule_df = fbref.read_schedule().reset_index()
        schedule_df.to_csv("mls_schedule.csv", index=False)
        print("-> Saved mls_schedule.csv")
    except Exception as e:
        print(f"Error fetching schedule: {e}")

    # 2. PLAYER SOT & SHOOTING STATS
    print("2. Extracting Player Shooting & SOT Stats...")
    try:
        player_shooting = fbref.read_player_match_stats(stat_type="shooting").reset_index()
        player_shooting.to_csv("mls_player_sot.csv", index=False)
        print("-> Saved mls_player_sot.csv")
    except Exception as e:
        print(f"Error fetching player SOT: {e}")

    # 3. TEAM CORNERS & SHOTS
    print("3. Extracting Team Match Stats...")
    try:
        team_match_df = fbref.read_team_match_stats(stat_type="schedule").reset_index()
        team_match_df.to_csv("mls_team_corners_sot.csv", index=False)
        print("-> Saved mls_team_corners_sot.csv")
    except Exception as e:
        print(f"Error fetching team stats: {e}")

    print("--- Scraping Complete ---")

if __name__ == "__main__":
    fetch_and_export_mls_betting_data()
