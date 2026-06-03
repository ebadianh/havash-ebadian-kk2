from app.chain.runnable import Runnable
from app.schemas import AskRequest

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