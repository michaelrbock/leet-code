import threading


_NEXT_FUNCTION_NAME = {
  "first": "second",
  "second": "third",
  "third": None
}


class Foo:
  def __init__(self):
    # Event for each function to wait on.
    self.events = {
      "first": None,
      "second": threading.Event(),
      "third": threading.Event()
    }

  def run_safely(self, name, print_fxn):
    if self.events[name] is not None:
      self.events[name].wait()

    print_fxn()
    next_function_name = _NEXT_FUNCTION_NAME[name]
    if next_function_name is not None:
      self.events[next_function_name].set()

  def first(self, printFirst: 'Callable[[], None]') -> None:
    self.run_safely("first", printFirst)

  def second(self, printSecond: 'Callable[[], None]') -> None:
    self.run_safely("second", printSecond)

  def third(self, printThird: 'Callable[[], None]') -> None:
    self.run_safely("third", printThird)
