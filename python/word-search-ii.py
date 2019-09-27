class TrieNode(object):
  def __init__(self):
    self.children = {}
    self.is_word = False


class Trie(object):
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root

    last_index = None
    for i, char in enumerate(word):
      if char in curr.children:
        curr = curr.children[char]
      else:
        last_index = i
        break

    if last_index is not None:
      for i in range(last_index, len(word)):
        curr.children[word[i]] = TrieNode()
        curr = curr.children[word[i]]

    curr.is_word = True

  def search(self, word):
    curr = self.root

    for char in word:
      if char in curr.children:
        curr = curr.children[char]
      else:
        return False

    return curr.is_word

  def is_prefix(self, prefix):
    curr = self.root

    for char in prefix:
      if char in curr.children:
        curr = curr.children[char]
      else:
        return False

    return curr.is_word or len(curr.children) > 0


OFFSETS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


class Solution(object):
  def next_moves(self, visited, board, row, col):
    moves = []

    for r_offset, c_offset in OFFSETS:
      new_row, new_col = row + r_offset, col + c_offset
      if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]):
        if (new_row, new_col) not in visited:
          moves.append((new_row, new_col))

    return moves

  def dfs(self, board, trie, row_index, col_index, so_far, visited, output):
    if trie.search(so_far):
      output.add(so_far)
    visited.add((row_index, col_index))
    for new_row, new_col in self.next_moves(visited, board, row_index, col_index):
      new_so_far = so_far + board[new_row][new_col]
      if trie.is_prefix(new_so_far):
        self.dfs(board, trie, new_row, new_col, new_so_far, visited, output)
    visited.remove((row_index, col_index))

  def findWords(self, board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    # Create Trie.
    trie = Trie()
    for word in words:
      trie.insert(word)

    # Count words on board.
    output = set()

    visited = set() # ()
    for row_index, row in enumerate(board):
      for col_index, char in enumerate(row):
        if trie.is_prefix(char):
          self.dfs(board, trie, row_index, col_index, char, visited, output)

    return list(output)
