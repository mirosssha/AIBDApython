# English Premier League Tracker

## Project Description

English Premier League Tracker is a simple command-line Python application for managing football teams and match results.

The application is based on the English Premier League and uses a sample dataset containing 20 real football clubs and 40 fictional match results.

Users can add teams, enter match results, view league standings, search for teams, calculate statistics, and export CSV reports.

## Features

- Add new football teams.
- Add match results with input validation.
- View all teams.
- Search for teams and view their statistics and match history.
- Calculate league standings automatically.
- Display a tournament summary.
- Export standings and team statistics to CSV files.
- Save and load data using JSON files.

## Project Structure

- `main.py` — command-line menu and user interaction.
- `tournament.py` — classes for managing teams, matches, and standings.
- `reports.py` — CSV reports using pandas and numerical calculations using NumPy.
- `data/teams.json` — list of football teams.
- `data/matches.json` — stored match results.
- `output/` — generated CSV reports.
- `requirements.txt` — required Python libraries.
- `syllabus_demo.py` — additional demonstrations of course concepts (to be completed).

## Requirements

- Python 3.10 or newer
- pandas
- NumPy

## Installation

1. Clone the repository:

   `git clone https://github.com/mirosssha/AIBDApython.git`

2. Open the project directory:

   `cd AIBDApython/sports_tournament_tracker`

3. Create a virtual environment:

   `python -m venv .venv`

4. Activate the virtual environment.

   Windows PowerShell:

   `.\.venv\Scripts\Activate.ps1`

   macOS/Linux:

   `source .venv/bin/activate`

5. Install the dependencies:

   `python -m pip install -r requirements.txt`

## Running the Application

Start the application with:

`python main.py`

The program displays the following menu:

1. Add team
2. Add match
3. View teams
4. Search team and statistics
5. League standings
6. Tournament summary
7. Export CSV reports
8. Save data
9. Exit

Enter the number of the required option.

## Sample Dataset

The application includes 20 Premier League clubs and 40 fictional matches.

The sample data is stored in two JSON files.

**teams.json**

Contains a list of team names, for example:

`["Arsenal", "Chelsea", "Liverpool"]`

**matches.json**

Contains a list of match records. Each record is a dictionary with four fields:

- `home` — home team name
- `away` — away team name
- `home_score` — goals scored by the home team
- `away_score` — goals scored by the away team

For example:

`{"home": "Arsenal", "away": "Chelsea", "home_score": 2, "away_score": 1}`

The initial match results are fictional - or how else one imagine Tottenham beating Arsenal?

## League Standings

Teams receive:

- 3 points for a win.
- 1 point for a draw.
- 0 points for a loss.

Standings are sorted by total points, goal difference, and goals scored. Team names are used as a final ordering rule when these values are equal.

## CSV Reports

The application uses pandas to create two CSV reports:

- `standings.csv` — league positions, matches played, wins, draws, losses, goals, goal difference, and points.
- `team_statistics.csv` — team performance statistics, including win rate.

NumPy is used to calculate average goals per match.

Reports are generated in the `output` directory after selecting option 7.

## Python Course Syllabus

The following table shows where the concepts from Sections 1–12 are used.

| Section | File and implementation |
|---|---|
| 1 | `main.py`, `tournament.py` — variables and data types |
| 2 | `main.py` — input, output, conditions, arithmetic |
| 3 | `main.py`, `tournament.py` — loops and collections |
| 4 | `main.py` — reusable functions; equality and identity demonstration pending |
| 5 | `tournament.py` — methods, arguments, mathematical operations and lists; recursion demonstration pending |
| 6 | `tournament.py` — `get_standings()` with `sorted()` and lambda; `main.py` — `map()`; `filter()` pending |
| 7 | `main.py` — score validation with `re.fullmatch()` and `re.findall()`; `re.search()` and `re.match()` pending |
| 8 | `main.py` — `load_data()` and `save_data()` |
| 9 | `main.py` — exception handling; `else` and `finally` demonstration pending |
| 10 | `tournament.py` — `Team` and `Tournament` classes; inheritance and polymorphism pending |
| 11 | `tournament.py` — `get_team_matches()` generator; `main.py` — iterator and generator expression; `reports.py` — `announce_export()` decorator |
| 12 | `reports.py` — `export_reports()` using pandas and NumPy |

