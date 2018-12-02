DELTA = [-1, 0, 1]


def neighborhood_sum(row, col, board):
  total = 0
  for dy in DELTA:
    for dx in DELTA:
      new_row = row + dy
      new_col = col + dx
      if new_row >= 0 and new_row < len(
          board) and new_col >= 0 and new_col < len(board[0]):
        total += board[new_row][new_col]
  return total


class Solution:

  def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    prev = [0] * len(board[0])
    curr = [0] * len(board[0])
    for r_index, row in enumerate(board):
      for c_index, cell in enumerate(row):
        neighborhood = neighborhood_sum(r_index, c_index, board)
        if neighborhood == 3:
          curr[c_index] = 1
        elif neighborhood == 4:
          curr[c_index] = cell
        else:
          curr[c_index] = 0
      if r_index > 0:
        board[r_index - 1] = prev
      prev = curr[:]
    board[-1] = prev
