import pandas as pd
import numpy as np
from pathlib import Path
from functools import wraps


OUTPUT_DIR = Path(__file__).resolve().parent / "output"

def announce_export(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting CSV export...")

        result = func(*args, **kwargs)

        print("CSV export completed")
        return result

    return wrapper

@announce_export
def export_reports(tournament):
    OUTPUT_DIR.mkdir(exist_ok=True)

    standings = tournament.get_standings()

    table_rows = []
    team_stats = []

    for position, team in enumerate(standings, 1):
        table_rows.append({
            "Position": position,
            "Team": team.name,
            "P": team.played,
            "W": team.won,
            "D": team.drawn,
            "L": team.lost,
            "GF": team.goals_for,
            "GA": team.goals_against,
            "GD": team.goal_difference(),
            "Points": team.points
        })

        if team.played > 0:
            win_rate = team.won / team.played * 100
        else:
            win_rate = 0

        team_stats.append({
            "Team": team.name,
            "Played": team.played,
            "Wins": team.won,
            "Draws": team.drawn,
            "Losses": team.lost,
            "Goals scored": team.goals_for,
            "Goals conceded": team.goals_against,
            "Win rate (%)": round(win_rate, 2)
        })

    standings_table = pd.DataFrame(table_rows)
    statistics_table = pd.DataFrame(team_stats)

    standings_table.to_csv(
        OUTPUT_DIR / "standings.csv", index=False
    )

    statistics_table.to_csv(
        OUTPUT_DIR / "team_statistics.csv", index=False
    )

    goals = []

    for match in tournament.matches:
        goals.append(match["home_score"] + match["away_score"])

    if len(goals) > 0:
        average_goals = np.mean(goals)
    else:
        average_goals = 0

