from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from app.query_handler import handle_question
from app.chain.pipeline import oraklet
from app.schemas import AskRequest
from app.data_manager import (
    set_dataframe,
    get_dataframe,
    get_total_matches,
    get_unique_teams,
    get_most_common_tournament,
    get_highest_home_score,
    get_highest_away_score,
    get_team_with_most_wins,
    get_team_with_most_goals,
    get_team_with_highest_win_percentage,
    get_tournament_with_highest_average_goals,
    get_team_with_most_draws,
    get_team_with_highest_average_goals,
    get_year_with_most_played_matches
)

app = FastAPI()

@app.get("/health")
def health():
  return {"status": "OK"}

@app.post("/data/upload")
async def upload_data(file: UploadFile = File(...)):

  df = pd.read_csv(file.file)

  set_dataframe(df)

  return {
    "rows": len(df),
    "columns": list(df.columns),
    "dtypes": {
      col: str(dtype)
      for col, dtype in df.dtypes.items()
    }
  }

@app.get("/data/stats")
def get_stats():
  current_df = get_dataframe()

  if current_df is None:
    return {"error": "No dataset uploaded"}
  
  return {
    "total_matches": get_total_matches(),
    "unique_teams": get_unique_teams(),
    "most_common_tournament": get_most_common_tournament(),
    "highest_home_score": get_highest_home_score(),
    "highest_away_score": get_highest_away_score(),
    "team_with_most_wins": get_team_with_most_wins(),
    "team_with_most_goals": get_team_with_most_goals(),
    "team_with_highest_win_percentage": get_team_with_highest_win_percentage(),
    "tournament_with_highest_average_goals": get_tournament_with_highest_average_goals(),
    "team_with_most_draws": get_team_with_most_draws(),
    "team_with_highest_average_goals": get_team_with_highest_average_goals(),
    "year_with_most_played_matches": get_year_with_most_played_matches()
  }

@app.post("/query")
def query(question: str):
  return handle_question(question)

@app.post("/ai/ask")
def ask(request: AskRequest):
  if get_dataframe() is None:
    raise HTTPException(
      status_code=400,
      detail="No dataset uploaded"
    )
  return oraklet.invoke(request)