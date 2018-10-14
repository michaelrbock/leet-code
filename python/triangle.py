"""
Dynamic Programming.
"""

class Solution:
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    # Keep track of min paths per row so far, start at bottom row.
    min_paths = triangle[-1]
    for i, row in enumerate(triangle[::-1]):
      if i == 0:
        # Skip bottom row.
        continue
      next_level = []
      for j, elem in enumerate(row):
        next_level.append(min(min_paths[j], min_paths[j+1]) + elem)
      min_paths = next_level
    return min_paths[0]


class Solution1:
  """Doesn't pass OJ's Time Limit."""
  def minimum_total_rec(self, triangle, memo, row, spot):
    if row == len(triangle) - 1:
      return triangle[row][spot]
    left = memo.get((row + 1, spot), self.minimum_total_rec(triangle, memo, row + 1, spot))
    if (row + 1, spot) not in memo:
      memo[(row + 1, spot)] = left
    right = memo.get((row + 1, spot + 1), self.minimum_total_rec(triangle, memo, row + 1, spot + 1))
    if (row + 1, spot + 1) not in memo:
      memo[(row + 1, spot + 1)] = right
    return triangle[row][spot] + min(left, right)

  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    memo = {}
    return self.minimum_total_rec(triangle, memo, 0, 0)
