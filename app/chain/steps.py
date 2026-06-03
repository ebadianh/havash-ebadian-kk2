from app.chain.runnable import Runnable
from app.schemas import AskRequest
from app.schemas import AskResponse

class PromptBuilder(Runnable[AskRequest, str]):
  def invoke(self, input: AskRequest) -> str:

    return f"""
Du är ett fotbollsorakel.

Användarens fråga:
{input.question}

"""

class LLMRunner(Runnable[str, str]):
  def invoke(self, input: str) -> str:
    return f"LLM received: {input}"

class ResponseParser(Runnable[str, AskResponse]):
  def invoke(self, input: str) -> AskResponse:

    return AskResponse(
      question="Testfråga",
      answer=input,
      model="MockLLM"
    )