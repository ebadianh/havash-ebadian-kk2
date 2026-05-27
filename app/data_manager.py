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