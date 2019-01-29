def valid_section(section):
  nums = set()
  for cell in section:
    if cell == '.':
      continue
    if cell in nums:
      return False
    nums.add(cell)
  return True


class Solution:
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check rows.
    for row in board:
      if not valid_section(row):
        return False
    # Check cols.
    for i in range(len(board[0])):
      col = [board[j][i] for j in range(len(board))]
      if not valid_section(col):
        return False
    # Check boxes.
    for row_start in range(0, 7, 3):
      for col_start in range(0, 7, 3):
        box = []
        for i in range(3):
          for j in range(3):
            box.append(board[row_start+i][col_start+j])
        if not valid_section(box):
          return False
    return True


s = Solution()
test1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
assert s.isValidSudoku(test1)

test2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
assert not s.isValidSudoku(test2)
