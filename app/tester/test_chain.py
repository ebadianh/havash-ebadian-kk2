import pandas as pd
from app.chain.steps import PromptBuilder
from app.schemas import AskRequest
from app.data_manager import set_dataframe

def test_prompt_builder_includes_question():
  df = pd.DataFrame(
    {
      "home_team": ["Brazil"],
      "away_team": ["Sweden"],
      "home_score": [2],
      "away_score": [1]
    }
  )
  set_dataframe(df)
  
  prompt_builder = PromptBuilder()

  result = prompt_builder.invoke(
    AskRequest(
      question="Vilket lag har flest vinster?"
    )
  )

  assert "Vilket lag har flest vinster?" in result