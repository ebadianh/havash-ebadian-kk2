from app.chain.runnable import Runnable
from app.schemas import (
  AskRequest,
  AskResponse,
  LLMResponse
)
from transformers import pipeline
from app.data_manager import (
  get_total_matches,
  get_team_with_most_wins
)


class PromptBuilder(Runnable[AskRequest, str]):
  def invoke(self, input: AskRequest) -> str:
      total_matches = get_total_matches()
      most_wins = get_team_with_most_wins()

      return f"""
Du är ett fotbollsorakel.

Använd endast informationen nedan!

Fakta från datasetet:
- Datasetet innehåller {total_matches} matcher.
- Lag med flest vinster: {most_wins}.

Svara kortfattat på användarens fråga:
Användarens fråga:
{input.question}
"""

class LLMRunner(Runnable[str, LLMResponse]):
  def __init__(self):
    self.model = pipeline(
      "text-generation",
      model="HuggingFaceTB/SmolLM2-135M-Instruct"
    )
  def invoke(self, input: str) -> LLMResponse:
    result = self.model(
      input,
      max_new_tokens=100
    )

    return LLMResponse(
      question=input,
      answer=result[0]["generated_text"]
    )

class ResponseParser(Runnable[LLMResponse, AskResponse]):
  def invoke(self, input: LLMResponse) -> AskResponse:

    return AskResponse(
      question=input.question,
      answer=input.answer,
      model="HuggingFaceTB/SmolLM2-135M-Instruct"
    )