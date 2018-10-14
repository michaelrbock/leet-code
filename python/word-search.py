"""
Backtracking.
"""


_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


class Solution:

  def exist_rec(self, board, word, row, col, visited):
    if len(word) == 1:
      return True
    word = word[1:]
    visited.add((row, col))
    for i, j in _DIRECTIONS:
      new_row = row + i
      new_col = col + j
      if new_row < 0 or new_row >= len(board) or new_col < 0 or new_col >= len(
          board[0]):
        continue
      if board[new_row][new_col] == word[0] and (new_row,
                                                 new_col) not in visited:
        if self.exist_rec(board, word, new_row, new_col, visited):
          return True
    visited.remove((row, col))
    return False

  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if len(board) * len(board[0]) < len(word):
      return False

    for row in range(len(board)):
      for col in range(len(board[0])):
        if board[row][col] == word[0]:
          if self.exist_rec(board, word, row, col, set()):
            return True
    return False
