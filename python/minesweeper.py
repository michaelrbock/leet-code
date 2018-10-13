"""
BFS.
"""


from collections import deque


def directions():
  return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class Solution:

  def updateBoard(self, board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    # Sorry :(
    if board[click[0]][click[1]] == 'M':
      board[click[0]][click[1]] = 'X'
      return board
    # BFS
    to_visit = deque([click])
    while to_visit:
      row, col = to_visit.popleft()
      if board[row][col] == 'E':
        mines = 0
        possibly_visit = []
        for i, j in directions():
          new_row = row + i
          new_col = col + j
          if new_row < 0 or new_row >= len(
              board) or new_col < 0 or new_col >= len(board[0]):
            continue
          if board[new_row][new_col] == 'M':
            mines += 1
          elif board[new_row][new_col] == 'E':
            possibly_visit.append((new_row, new_col))
        if mines == 0:
          to_visit += possibly_visit
          board[row][col] = 'B'
        elif mines > 0:
          board[row][col] = str(mines)
    return board
