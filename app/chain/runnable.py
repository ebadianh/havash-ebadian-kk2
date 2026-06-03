from typing import Generic, TypeVar

Input = TypeVar("Input")
Output = TypeVar("Output")

class Runnable(Generic[Input, Output]):
  def invoke(self, input:Input) -> Output:
    raise NotImplementedError
  
class RunnableSequence(Runnable[Input, Output]):
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def invoke(self, input):
    return self.second.invoke(
      self.first.invoke(input)
    )