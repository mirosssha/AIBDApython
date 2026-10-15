import json
from pathlib import Path
class Team:
    def __init__(self, name):
        self.name = name
        self.played = 0
        self.won = 0
        self.drawn = 0
        self.lost = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

    def record_result(self, goals_for, goals_against):
        self.played += 1
        self.goals_for += goals_for
        self.goals_against += goals_against

        if goals_for > goals_against:
            self.won += 1
            self.points += 3

        elif goals_for == goals_against:
            self.drawn += 1
            self.points += 1

        else:
            self.lost += 1

    def goal_difference(self):
        return self.goals_for - self.goals_against

class Tournament:
    def __init__(self, teams, matches):
        self.teams = []
        self.matches = []

        for team in teams:
            self.add_team(team)

        for match in matches:
            self.add_match(
                match["home"],
                match["away"],
                match["home_score"],
                match["away_score"]
            )

    def add_team(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Team name cannot be empty")

        name = name.strip()

        for team in self.teams:
            if team.lower() == name.lower():
                raise ValueError("Team already exists")

        self.teams.append(name)

    def add_match(self, home, away, home_score, away_score):
        if home not in self.teams or away not in self.teams:
            raise ValueError("Team does not exist")

        if home == away:
            raise ValueError("A team cannot play against itself")

        if not isinstance(home_score, int) or not isinstance(away_score, int):
            raise ValueError("Scores must be integers")

        if home_score < 0 or away_score < 0:
            raise ValueError("Scores cannot be negative")

        for match in self.matches:
            if match["home"] == home and match["away"] == away:
                raise ValueError("This match already has a result")

        match = {
            "home": home,
            "away": away,
            "home_score": home_score,
            "away_score": away_score
        }

        self.matches.append(match)

    def get_standings(self):
        statistics = {}

        for name in self.teams:
            statistics[name] = Team(name)

        for match in self.matches:
            home = statistics[match["home"]]
            away = statistics[match["away"]]

            home.record_result(
                match["home_score"],
                match["away_score"]
            )

            away.record_result(
                match["away_score"],
                match["home_score"]
            )

        standings = sorted(
            statistics.values(),
            key=lambda team: (
                -team.points,
                -team.goal_difference(),
                -team.goals_for,
                team.name
            )
        )

        return standings

    def get_team_matches(self, team_name):
        for match in self.matches:
            if match["home"] == team_name or match["away"] == team_name:
                yield match


if __name__ == "__main__":
    data_dir = Path(__file__).resolve().parent / "data"

    with open(data_dir / "teams.json", encoding="utf-8") as file:
        teams = json.load(file)

    with open(data_dir / "matches.json", encoding="utf-8") as file:
        matches = json.load(file)

    tournament = Tournament(teams, matches)
    standings = tournament.get_standings()

    print("\nPREMIER LEAGUE STANDINGS\n")

    print(
        f"{'Pos':<4} {'Team':<22} "
        f"{'P':>2} {'W':>2} {'D':>2} {'L':>2} "
        f"{'GF':>3} {'GA':>3} {'GD':>3} {'Pts':>4}"
    )

    for position, team in enumerate(standings, 1):
        print(
            f"{position:<4} {team.name:<22} "
            f"{team.played:>2} {team.won:>2} "
            f"{team.drawn:>2} {team.lost:>2} "
            f"{team.goals_for:>3} {team.goals_against:>3} "
            f"{team.goal_difference():>3} {team.points:>4}"
        )
