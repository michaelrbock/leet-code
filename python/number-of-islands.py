"""
DFS.

Time: O(m * n)
"""


from collections import deque


class Solution:

  def __init__(self):
    self.visited = set()

  def numIslands(self, grid):
    count = 0
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if (row, col) not in self.visited and grid[row][col] == '1':
          self.dfs(grid, row, col)
          count += 1
    return count

  def dfs(self, grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(
        grid[0]) or (row, col) in self.visited or grid[row][col] != '1':
      return
    self.visited.add((row, col))
    self.dfs(grid, row + 1, col)  # UP
    self.dfs(grid, row - 1, col)  # DOWN
    self.dfs(grid, row, col + 1)  # LEFT
    self.dfs(grid, row, col - 1)  # RIGHT


class Solution1:

  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    visited = set()
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if (row, col) not in visited and grid[row][col] == '1':
          self.bfs(grid, row, col, visited)
          count += 1
    return count

  def bfs(self, grid, start_row, start_col, visited):
    to_visit = deque([(start_row, start_col)])
    while to_visit:
      row, col = to_visit.popleft()
      visited.add((row, col))
      to_visit += self.possible_moves(grid, row, col, visited)

  def possible_moves(self, grid, row, col, visited):
    result = []
    # UP, LEFT, DOWN, RIGHT
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for row_offset, col_offset in offsets:
      new_row = row + row_offset
      new_col = col + col_offset
      new_tup = (new_row, new_col)
      if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(
          grid[0]) and new_tup not in visited and grid[new_row][new_col] == '1':
        result.append(new_tup)
    return result
