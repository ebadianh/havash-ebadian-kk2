
current_df = None

def set_dataframe(df):
  global current_df
  current_df = df

def get_dataframe():
  return current_df