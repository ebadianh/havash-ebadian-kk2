import pandas as pd
from app.chain.steps import (
  PromptBuilder,
  ResponseParser
)
from app.schemas import (
  AskRequest,
  LLMResponse
)
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

def test_response_parser_returns_ask_response():

  parser = ResponseParser()

  result = parser.invoke(
    LLMResponse(
      question="Vilket lag har flest vinster?",
      answer="Brazil har flest vinster."
    )
  )

  assert result.question == "Vilket lag har flest vinster?"
  assert result.answer == "Brazil har flest vinster."
  assert result.model == "HuggingFaceTB/SmolLM2-135M-Instruct"

def test_response_parser_sets_model_name():
  
  parser = ResponseParser()

  result = parser.invoke(
    LLMResponse(
      question="Test",
      answer="Testsvar"
    )
  )

  assert result.model == "HuggingFaceTB/SmolLM2-135M-Instruct"