"""
BFS.
"""


from collections import deque


class Solution:
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    squares = [i*i for i in range(n + 1) if i*i <= n]
    to_visit = deque([(n, 0)])
    while to_visit:
      remaining, depth = to_visit.popleft()
      for square in reversed(squares):
        result = remaining - square
        if result == 0:
          return depth + 1
        if result > 0:
          to_visit.append((result, depth + 1))
