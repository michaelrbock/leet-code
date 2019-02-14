class RLEIterator:
  def __init__(self, A: 'List[int]'):
    self.encoding = A
    self.index = 0
    self.inner_index = 0

  def next(self, n: 'int') -> 'int':
    while self.index < len(self.encoding):
      if self.encoding[self.index] == 0:
        self.index += 2
      elif n <= self.encoding[self.index] - self.inner_index:
        output = self.encoding[self.index + 1]
        self.inner_index += n
        return output
      else:
        n -= (self.encoding[self.index] - self.inner_index)
        self.inner_index = 0
        self.index += 2
    return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
