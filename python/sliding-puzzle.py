import copy
from collections import deque


# RIGHT, DOWN, UP, LEFT
_DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def _find_zero(board):
  """Returns row, col location of 0 in board."""
  for r_index, row in enumerate(board):
    for c_index, num in enumerate(row):
      if num == 0:
        return r_index, c_index


def _possible_moves(state):
  row, col = _find_zero(state)
  for dy, dx in _DIRECTIONS:
    new_state = copy.deepcopy(state)
    new_row, new_col = row + dy, col + dx
    if new_row in (0, 1) and new_col in (0, 1, 2):
      new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
      yield new_state


def _hashable(state):
  return tuple(state[0]), tuple(state[1])


class Solution:
  def slidingPuzzle(self, board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    # Strategy: BFS where nodes are states, moves are edges.
    visited = set()
    to_visit = deque([(board, 0)])  # (state, moves so far)
    while to_visit:
      state, moves = to_visit.popleft()
      if state == [[1,2,3], [4, 5, 0]]:
        return moves
      visited.add(_hashable(state))
      for next_state in _possible_moves(state):
        if _hashable(next_state) not in visited:
          to_visit.append((next_state, moves + 1))
    return -1

s = Solution()
assert s.slidingPuzzle([[1,2,3],[4,0,5]]) == 1
assert s.slidingPuzzle([[1,2,3],[5,4,0]]) == -1
assert s.slidingPuzzle([[4,1,2],[5,0,3]]) == 5
assert (s.slidingPuzzle([[3,2,4],[1,5,0]])) == 14
print('All tests passed!')
