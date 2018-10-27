"""Dynamic Programming."""


class Solution:

  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    grid = [[-1
             for _ in range(len(obstacleGrid[0]))]
            for _ in range(len(obstacleGrid))]
    for i in range(len(obstacleGrid)):
      for j in range(len(obstacleGrid[0])):
        if obstacleGrid[i][j] == 1:
          grid[i][j] = 0
        elif i == 0:
          grid[i][j] = 0 if grid[i][j - 1] == 0 else 1
        elif j == 0:
          grid[i][j] = 0 if grid[i - 1][j] == 0 else 1
        else:
          grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[-1][-1]
