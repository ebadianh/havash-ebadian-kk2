# KK2 – Fotbollsoraklet


## Projektbeskrivning
Fotbollsoraklet är en FastAPI-applikation som kombinerar dataanalys med artificiell intelligens. Användaren kan ladda upp ett CSV-dataset med fotbollsmatcher, få statistik om datat och ställa frågor på naturligt språk.

Applikationen använder Pandas för datahantering och SmolLM2-135M-Instruct från HuggingFace för att generera svar. AI-flödet byggs upp genom en egen Runnable-kedja bestående av PromptBuilder, LLMRunner och ResponseParser.

## AI-kedjan
PromptBuilder
↓
LLMRunner
↓
ResponseParser

Kedjan byggs med Runnable-objekt och |-operatorn.

## Funktioner
- Ladda upp CSV-filer
- Visa statistik från datasetet
- Ställa frågor om datat på naturligt språk
- AI-genererade svar med SmolLM
- Felhantering för ogiltiga filer och saknade dataset
- Automatiserade tester med pytest

## Projektstruktur
HAVASH-EBADIAN-KK2
│
├── app
│   ├── chain
│   ├── data
│   ├── tester
│   ├── data_manager.py
│   ├── main.py
│   ├── query_handler.py
│   └── schemas.py
│
├── README.md
├── reflektion.md
├── .gitignore
└── requirements.txt

## Installation
Klona repot:
git clone <repo-url>
cd havash-ebadian-kk2

Installera beroenden:
pip install -r requirements.txt

## Dataset
Projektet använder ett dataset med internationella fotbollsmatcher från 1972 till 2026 som finns i:

app/data/

## Starta applikationen
uvicorn app.main:app --reload

Swagger finns på:
http://127.0.0.1:8000/docs

## Endpoints
GET /health
Kontrollerar att API är igång.

Svar:
{
  "status": "OK"
}

## POST /data/upload
Laddar upp ett CSV-dataset.

Svar:
{
  "rows": 49287,
  "columns": [...],
  "dtypes": {...}
}

## GET /data/stats
Returnerar statistik från det uppladdade datasetet.

## POST /ai/ask
Tar emot en fråga och returnerar ett AI-genererat svar.

Exempel:
{
  "question": "Vilket lag har flest vinster?"
}

Svar:
{
  "question": "Vilket lag har flest vinster?",
  "answer": "Brazil har flest vinster.",
  "model": "HuggingFaceTB/SmolLM2-135M-Instruct"
}

## Tester
Kör alla tester:
python -m pytest app/tester -v

Projektet innehåller tester för:
Runnable-kedjan
API-endpoints
Felhantering
Filuppladdningar

## Kända begränsningar
SmolLM kan generera felaktiga svar eller hallucinationer.
Dataset måste laddas upp innan /ai/ask används.
Endast CSV-filer accepteras.
Dataset lagras endast i minnet under applikationens livstid.