class Solution:
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
      return []
    visited = set()
    result = []
    row = 0
    col = 0
    direction = 'RIGHT'  # DOWN, LEFT, UP
    while len(visited) < len(matrix) * len(matrix[0]):
      result.append(matrix[row][col])
      visited.add((row, col))
      if direction == 'RIGHT':
        new_col = col + 1
        if new_col >= len(matrix[0]) or (row, new_col) in visited:
          direction = 'DOWN'
          row += 1
        else:
          col = new_col
      elif direction == 'DOWN':
        new_row = row + 1
        if new_row >= len(matrix) or (new_row, col) in visited:
          direction = 'LEFT'
          col -= 1
        else:
          row = new_row
      elif direction == 'LEFT':
        new_col = col - 1
        if new_col < 0 or (row, new_col) in visited:
          direction = 'UP'
          row -= 1
        else:
          col = new_col
      elif direction == 'UP':
        new_row = row - 1
        if new_row < 0 or (new_row, col) in visited:
          direction = 'RIGHT'
          col += 1
        else:
          row = new_row
    return result
