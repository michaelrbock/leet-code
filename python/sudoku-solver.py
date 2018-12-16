def valid_row(board, row, num):
  for cell in board[row]:
    if cell == num:
      return False
  return True


def valid_col(board, col, num):
  for row in range(len(board)):
    if board[row][col] == num:
      return False
  return True


def valid_box(board, row, col, num):
  for i in range(row, row + 3):
    for j in range(col, col + 3):
      if board[i][j] == num:
        return False
  return True


def valid_placement(board, row, col, num):
  return valid_row(board, row, num) and valid_col(
      board, col, num) and valid_box(board, row - row % 3, col - col % 3, num)


def next_row_col(board):
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == '.':
        return row, col


def solve_sudoku_rec(board):
  next_spot = next_row_col(board)
  if not next_spot:
    return True
  else:
    row, col = next_spot

  for num in range(1, 10):
    if valid_placement(board, row, col, str(num)):
      board[row][col] = str(num)
      if solve_sudoku_rec(board):  # Recurse.
        return True
      board[row][col] = '.'  # Backtrack.


class Solution:

  def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    # Strategy: recursion with backtracking.
    solve_sudoku_rec(board)
