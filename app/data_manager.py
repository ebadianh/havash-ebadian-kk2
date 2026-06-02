import pandas as pd

current_df = None

def set_dataframe(df):
  global current_df
  current_df = df

def get_dataframe():
  return current_df

def get_total_matches():
  return len(current_df)

def get_unique_teams():
  return len(
      pd.concat([
        current_df["home_team"],
        current_df["away_team"]
      ]).unique()
    )

def get_most_common_tournament():
  return current_df["tournament"].mode()[0]

def get_highest_home_score():
    return int(current_df["home_score"].max())

def get_highest_away_score():
    return int(current_df["away_score"].max())

def get_team_with_most_wins():
   home_wins = current_df[current_df["home_score"] > current_df["away_score"]]["home_team"]
   away_wins = current_df[current_df["away_score"] > current_df["home_score"]]["away_team"]

   all_wins = pd.concat([home_wins, away_wins])

   return all_wins.value_counts().idxmax()

def get_team_with_most_goals():
   home_goals = current_df.groupby("home_team")["home_score"].sum()
   away_goals = current_df.groupby("away_team")["away_score"].sum()

   total_goals = home_goals.add(away_goals, fill_value=0)

   top_team = total_goals.idxmax()

   return {
      "team": top_team,
      "goals": int(total_goals.max())
   }

def get_team_with_highest_win_percentage():
   home_matches = current_df["home_team"].value_counts()
   away_matches = current_df["away_team"].value_counts()
   total_matches = home_matches.add(away_matches, fill_value=0)
   eligible_teams = total_matches[total_matches >= 300]

   home_wins = current_df[
      current_df["home_score"] > current_df["away_score"]
      ]["home_team"].value_counts()

   away_wins = current_df[
      current_df["away_score"] > current_df["home_score"]
      ]["away_team"].value_counts()
   
   total_wins = home_wins.add(away_wins, fill_value=0)

   win_percentage = (
      total_wins[eligible_teams.index] / eligible_teams
   ) * 100

   top_team = win_percentage.idxmax()

   return {
      "team": top_team,
      "win_percentage": round(float(win_percentage.max()), 2)
   }

def get_tournament_with_highest_average_goals():
   goals_per_match = (
      current_df["home_score"]
      + current_df["away_score"]
   )

   tournament_average_goals = goals_per_match.groupby(
      current_df["tournament"]
   ).mean()

   top_tournament = tournament_average_goals.idxmax()

   return {
      "tournament": top_tournament,
      "average_goals": round(
         float(tournament_average_goals.max()), 2)
   }

def get_team_with_most_draws():
   draw_matches = current_df[
    current_df["home_score"] == current_df["away_score"]
]
   home_draws = draw_matches["home_team"].value_counts()
   away_draws = draw_matches["away_team"].value_counts()
   total_draws = home_draws.add(away_draws, fill_value=0)

   top_team = total_draws.idxmax()

   return {
      "team": top_team,
      "draws": int(total_draws.max())
   }

def get_team_with_highest_average_goals():

    home_goals = current_df.groupby("home_team")["home_score"].sum()

    away_goals = current_df.groupby("away_team")["away_score"].sum()

    total_goals = home_goals.add(away_goals, fill_value=0)

    home_matches = current_df["home_team"].value_counts()

    away_matches = current_df["away_team"].value_counts()

    total_matches = home_matches.add(away_matches, fill_value=0)

    average_goals = total_goals / total_matches

    top_team = average_goals.idxmax()

    return {
        "team": top_team,
        "average_goals": round(float(average_goals.max()), 2)
    }

def get_year_with_most_played_matches():
   
   dates = pd.to_datetime(current_df["date"])
   
   years = dates.dt.year

   matches_per_year = years.value_counts()

   top_year = matches_per_year.idxmax()

   return {
      "year": int(top_year),
      "matches": int(matches_per_year.max())
   }