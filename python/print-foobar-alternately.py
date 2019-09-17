import threading


class FooBar(object):
  def __init__(self, n):
    self.n = n
    self.foo_event = threading.Event()
    self.foo_event.set() # Print "foo" first.
    self.bar_event = threading.Event()

  def foo(self, printFoo):
    """
    :type printFoo: method
    :rtype: void
    """
    for i in xrange(self.n):
      self.foo_event.wait()
      # printFoo() outputs "foo". Do not change or remove this line.
      printFoo()
      self.foo_event.clear()
      self.bar_event.set()

  def bar(self, printBar):
    """
    :type printBar: method
    :rtype: void
    """
    for i in xrange(self.n):
      self.bar_event.wait()
      # printBar() outputs "bar". Do not change or remove this line.
      printBar()
      self.bar_event.clear()
      self.foo_event.set()
