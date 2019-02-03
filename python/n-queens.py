class Solution:
  def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    results = []

    def is_attacked(row, col, board):
      # Only need to check that col & diag are free.
      # Check cols.
      for i in range(len(board)):
        if board[i][col] == 'Q':
          return True
      # Check diags.
      for i in range(len(board)):
        for j in range(len(board[0])):
          if (i + j == row + col or i - j == row - col) and board[i][j] == 'Q':
            return True
      return False

    def n_queens_rec(to_place, row, board):
      if to_place == 0:
        results.append([''.join(row) for row in board])
        return
      for col in range(len(board[0])):
        if not is_attacked(row, col, board):
          board[row][col] = 'Q'
          n_queens_rec(to_place - 1, row + 1, board)
          board[row][col] = '.'

    board = [['.'] * n for _ in range(n)]
    n_queens_rec(n, 0, board)
    return results


s = Solution()
print(s.solveNQueens(4))
