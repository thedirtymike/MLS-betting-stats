import pandas as pd
import soccerdata as sd

def fetch_and_export_mls_betting_data():
    print("--- Initializing FBref MLS Scraper ---")
    fbref = sd.FBref(leagues="USA-Major League Soccer", seasons="2026")

    # 1. SCHEDULE & FIXTURES
    print("1. Extracting Match Schedule & Times...")
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
    print("3. Extracting Team Match Stats (Corners & SOT)...")
    try:
        team_match_df = fbref.read_team_match_stats(stat_type="schedule").reset_index()
        team_match_df.to_csv("mls_team_corners_sot.csv", index=False)
        print("-> Saved mls_team_corners_sot.csv")
    except Exception as e:
        print(f"Error fetching team stats: {e}")

    print("--- Scraping Complete ---")

if __name__ == "__main__":
    fetch_and_export_mls_betting_data()
