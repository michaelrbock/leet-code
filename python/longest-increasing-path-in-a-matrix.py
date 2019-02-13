class Solution:
  def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
    cache = {}
    longest = 0

    def dfs(row, col):
      key = (row, col)
      if key in cache:
        return cache[key]
      val = matrix[row][col]
      cache[key] = 1 + max(
        dfs(row - 1, col) if row > 0 and val > matrix[row - 1][col] else 0,
        dfs(row, col - 1) if col > 0 and val > matrix[row][col - 1] else 0,
        dfs(row + 1, col) if row + 1 < len(matrix) and val > matrix[row + 1][col] else 0,
        dfs(row, col + 1) if col + 1 < len(matrix[0]) and val > matrix[row][col + 1] else 0)
      return cache[key]

    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        longest = max(longest, dfs(row, col))

    return longest
