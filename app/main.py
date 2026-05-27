from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

current_df = None

@app.get("/health")
def health():
  return {"status": "OK"}

@app.post("/data/upload")
async def upload_data(file: UploadFile = File(...)):
  global current_df

  df = pd.read_csv(file.file)

  current_df = df

  return {
    "rows": len(df),
    "columns": list(df.columns)
  }

@app.get("/data/stats")
def get_stats():
  global current_df

  if current_df is None:
    return {"error": "No dataset uploaded"}
  
  return {
    "total_matches": len(current_df)
  }