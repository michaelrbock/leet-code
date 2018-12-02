from collections import deque


class MyStack:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.q1 = deque()
    self.q2 = deque()

  def push(self, x):
    """
    Push element x onto stack.
    :type x: int
    :rtype: void
    """
    if not self.q1 and not self.q2:
      self.q1.appendleft(x)
    elif self.q1:
      self.q1.appendleft(x)
    else:
      self.q2.appendleft(x)

  def pop(self):
    """
    Removes the element on top of the stack and returns that element.
    :rtype: int
    """
    if self.q1:
      while len(self.q1) > 1:
        self.q2.appendleft(self.q1.pop())
      result = self.q1.pop()
    else:
      while len(self.q2) > 1:
        self.q1.appendleft(self.q2.pop())
      result = self.q2.pop()
    return result

  def top(self):
    """
    Get the top element.
    :rtype: int
    """
    if self.q1:
      while len(self.q1) > 1:
        self.q2.appendleft(self.q1.pop())
      result = self.q1[0]
      self.q2.appendleft(self.q1.pop())
    else:
      while len(self.q2) > 1:
        self.q1.appendleft(self.q2.pop())
      result = self.q2[0]
      self.q1.appendleft(self.q2.pop())
    return result

  def empty(self):
    """
    Returns whether the stack is empty.
    :rtype: bool
    """
    return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()