from typing import Generic, TypeVar

Input = TypeVar("Input")
Output = TypeVar("Output")

class Runnable(Generic[Input, Output]):
  def invoke(self, input:Input) -> Output:
    raise NotImplementedError
  
  def __or__(self, other):
    return RunnableSequence(self, other)
  
class RunnableSequence(Runnable[Input, Output]):
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def invoke(self, input):
    return self.second.invoke(
      self.first.invoke(input)
    )
  
class RunnableLambda(Runnable[Input, Output]):
  def __init__(self, func):
    self.func = func

  def invoke(self, input: Input) -> Output:
    return self.func(input)