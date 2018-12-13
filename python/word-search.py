OFFSETS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(board, word, visited, row, col):
  if len(word) == 1:
    return True
  word = word[1:]
  visited.add((row, col))
  for r_offset, c_offset in OFFSETS:
    new_row, new_col = row + r_offset, col + c_offset
    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
      if board[new_row][new_col] == word[0] and (new_row, new_col) not in visited:
        if dfs(board, word, visited, new_row, new_col):
          return True
  visited.remove((row, col))
  return False


class Solution:
  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if len(board) * len(board[0]) < len(word):
      return False

    # Strategy: DFS w/ backtracking starting from each letter that == word[0].
    for row in range(len(board)):
      for col in range(len(board[0])):
        if board[row][col] == word[0]:
          if dfs(board, word, set(), row, col):
            return True
    return False
