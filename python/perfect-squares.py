from collections import deque

class Solution:
  def numSquares(self, n):
    # Strategy: bottoms up recursion.
    memo = [0]
    for i in range(1, n + 1):
      memo.append(1 + min(memo[i - x*x] for x in range(i//2+1, 0, -1) if x*x <= i))
    return memo[-1]


s = Solution()
assert s.numSquares(12) == 3
assert s.numSquares(13) == 2
assert s.numSquares(492) == 3
assert s.numSquares(7168) == 4
print('All tests passed!')


class Solution1:
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
