import heapq


class MedianFinder:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.min_heap = []  # Larger numbers.
    self.max_heap = []  # Smaller numbers.

  def addNum(self, num):
    """
    :type num: int
    :rtype: void
    """
    if not self.min_heap or num >= self.min_heap[0]:
      heapq.heappush(self.min_heap, num)
    else:
      heapq.heappush(self.max_heap, num * -1.)

    # Rebalance if necessary.
    if len(self.min_heap) > len(self.max_heap) + 1:
      heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1.)
    elif len(self.max_heap) > len(self.min_heap) + 1:
      heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1.)

  def findMedian(self):
    """
    :rtype: float
    """
    if len(self.min_heap) == len(self.max_heap):
      return (self.min_heap[0] + (self.max_heap[0] * -1.)) / 2.
    elif len(self.min_heap) > len(self.max_heap):
      return self.min_heap[0]
    else:  # len(self.max_heap) > len(self.min_heap)
      return self.max_heap[0] * -1.


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
