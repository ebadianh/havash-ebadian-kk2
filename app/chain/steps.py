from app.chain.runnable import Runnable
from app.schemas import AskRequest, AskResponse
from transformers import pipeline
from app.data_manager import get_total_matches


class PromptBuilder(Runnable[AskRequest, str]):
  def invoke(self, input: AskRequest) -> str:
      total_matches = get_total_matches()

      return f"""
Du är ett fotbollsorakel.

Datasetet innehåller {total_matches} matcher.

Användarens fråga:
{input.question}

"""

class LLMRunner(Runnable[str, str]):
  def __init__(self):
    self.model = pipeline(
      "text-generation",
      model="HuggingFaceTB/SmolLM2-135M-Instruct"
    )
  def invoke(self, input: str) -> str:
    result = self.model(
      input,
      max_new_tokens=100
    )

    return result[0]["generated_text"]

class ResponseParser(Runnable[str, AskResponse]):
  def invoke(self, input: str) -> AskResponse:

    return AskResponse(
      question="Testfråga",
      answer=input,
      model="MockLLM"
    )