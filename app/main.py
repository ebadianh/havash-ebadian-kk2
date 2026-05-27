from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.data_manager import set_dataframe, get_dataframe

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
    "columns": list(df.columns)
  }

@app.get("/data/stats")
def get_stats():
  current_df = get_dataframe()

  if current_df is None:
    return {"error": "No dataset uploaded"}
  
  return {
    "total_matches": len(current_df),

    "unique_teams": len(
      pd.concat([
        current_df["home_team"],
        current_df["away_team"]
      ]).unique()
    )
  }