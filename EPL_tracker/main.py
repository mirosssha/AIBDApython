import json
import re
from pathlib import Path

from tournament import Tournament
from reports import export_reports

DATA_DIR = Path(__file__).resolve().parent / "data"


def load_data():
    with open(DATA_DIR / "teams.json", encoding="utf-8") as file:
        teams = json.load(file)

    with open(DATA_DIR / "matches.json", encoding="utf-8") as file:
        matches = json.load(file)

    return Tournament(teams, matches)


def save_data(tournament):
    with open(DATA_DIR / "teams.json", "w", encoding="utf-8") as file:
        json.dump(tournament.teams, file, indent=4)

    with open(DATA_DIR / "matches.json", "w", encoding="utf-8") as file:
        json.dump(tournament.matches, file, indent=4)

    print("Data saved successfully")


def main():
    try:
        tournament = load_data()
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"Error loading data: {error}")
        return

    while True:
        print("\n===== PREMIER LEAGUE TRACKER =====")
        print("1. Add team")
        print("2. Add match")
        print("3. View teams")
        print("4. Search team and statistics")
        print("5. League standings")
        print("6. Tournament summary")
        print("7. Export CSV reports")
        print("8. Save data")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Team name: ")

            try:
                tournament.add_team(name)
                print("Team added")
            except ValueError as error:
                print(f"Error: {error}")



        elif choice == "2":
            home = input("Home team: ").strip()
            away = input("Away team: ").strip()

            try:
                score = input("Enter score (e.g. 2:1): ").strip()

                if not re.fullmatch(r"[0-9]+:[0-9]+", score):
                    raise ValueError("Invalid score format")

                home_score, away_score = map(

                    int, re.findall(r"[0-9]+", score)
                )

                tournament.add_match(
                    home, away, home_score, away_score
                )

                print("Match added successfully")


            except ValueError as error:

                print(f"Error: {error}")

        elif choice == "3":
            for team in sorted(tournament.teams):
                print(team)


        elif choice == "4":
            name = input("Search team: ").strip().lower()
            found = False

            for team in tournament.get_standings():
                if name in team.name.lower():
                    found = True

                    print(f"\nTeam: {team.name}")
                    print(f"Played: {team.played}")
                    print(f"Wins: {team.won}")
                    print(f"Draws: {team.drawn}")
                    print(f"Losses: {team.lost}")
                    print(f"Goals scored: {team.goals_for}")
                    print(f"Goals conceded: {team.goals_against}")
                    print(f"Goal difference: {team.goal_difference()}")
                    print(f"Points: {team.points}")
                    print("\nMatch history:")

                    has_matches = False

                    for match in tournament.get_team_matches(team.name):
                        print(

                            f"{match['home']} "

                            f"{match['home_score']} : "

                            f"{match['away_score']} "

                            f"{match['away']}"

                        )

                        has_matches = True

                    if not has_matches:
                        print("No matches played")

            if not found:
                print("Team not found")

        elif choice == "5":
            print("\nPREMIER LEAGUE STANDINGS\n")
            print("Pos  Team                   P  W  D  L GF GA GD Pts")

            for i, team in enumerate(tournament.get_standings(), 1):
                print(
                    f"{i:<4} {team.name:<22} "
                    f"{team.played:>2} {team.won:>2} "
                    f"{team.drawn:>2} {team.lost:>2} "
                    f"{team.goals_for:>2} {team.goals_against:>2} "
                    f"{team.goal_difference():>2} {team.points:>3}"
                )

        elif choice == "6":
            total_goals = sum(
                match["home_score"] + match["away_score"]
                for match in tournament.matches
            )

            total_matches = len(tournament.matches)

            if total_matches > 0:
                average = total_goals / total_matches
            else:
                average = 0

            print(f"Teams: {len(tournament.teams)}")
            print(f"Matches: {total_matches}")
            print(f"Total goals: {total_goals}")
            print(f"Average goals per match: {average:.2f}")


        elif choice == "7":
            try:
                export_reports(tournament)
            except OSError as error:
                print(f"Export error: {error}")

        elif choice == "8":
            try:
                save_data(tournament)
            except OSError as error:
                print(f"Save error: {error}")

        elif choice == "9":
            try:
                save_data(tournament)
            except OSError as error:
                print(f"Save error: {error}")
                continue

            print("Goodbye!")
            break


        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
