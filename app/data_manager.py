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
    ),

def get_most_common_tournament():
  return current_df["tournament"].mode(0)

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
