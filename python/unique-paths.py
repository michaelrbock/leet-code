"""Dynamic Programming."""

class Solution:
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    grid = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
      for j in range(m):
        if i == 0 or j == 0:
          grid[i][j] = 1
        else:
          grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]
