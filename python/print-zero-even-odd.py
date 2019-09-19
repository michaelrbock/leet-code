import threading


class ZeroEvenOdd(object):
  def __init__(self, n):
    self.n = n

    self.zero_event = threading.Event()
    self.zero_event.set()
    self.odd_event = threading.Event()
    self.even_event = threading.Event()

  # printNumber(x) outputs "x", where x is an integer.
  def zero(self, printNumber):
    """
    :type printNumber: method
    :rtype: void
    """
    for i in range(self.n):
      self.zero_event.wait()
      self.zero_event.clear()
      printNumber(0)

      if i % 2 == 0:
        self.odd_event.set()
      else:
        self.even_event.set()

  def odd(self, printNumber):
    """
    :type printNumber: method
    :rtype: void
    """
    for i in range(1, self.n + 1, 2):
      self.odd_event.wait()
      self.odd_event.clear()
      printNumber(i)

      self.zero_event.set()

  def even(self, printNumber):
    """
    :type printNumber: method
    :rtype: void
    """
    for i in range(2, self.n + 1, 2):
      self.even_event.wait()
      self.even_event.clear()
      printNumber(i)

      self.zero_event.set()
