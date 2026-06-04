from fastapi.testclient import TestClient
from app.main import app
from app.data_manager import set_dataframe
from io import BytesIO

client = TestClient(app)

def test_health_endpoint():
  response = client.get("/health")

  assert response.status_code == 200
  assert response.json() == {"status": "OK"}

def test_stats_without_dataset():
  set_dataframe(None)
  response = client.get("/data/stats")

  assert response.status_code == 200
  assert response.json() == {
    "error": "No dataset uploaded"
  }

def test_ai_ask_endpoint():

  set_dataframe(None)

  response = client.post(
    "/ai/ask",
    json={
      "question": "Vilket lag har flest vinster?"
    }
  )

  assert response.status_code == 400

def test_upload_invalid_file():
  response = client.post(
    "/data/upload",
    files={
      "file": (
        "text.txt",
        BytesIO(b"Invalid file type."),
        "text/plain"
      )
    }
  )
  
  assert response.status_code == 400
  assert response.json() == {
    "detail": "Invalid CSV file."
  }