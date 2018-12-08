def binary_row(rows, target):
  if len(rows) == 1:
    return 0, None
  if len(rows) == 2:
    return (1, None) if target >= rows[1] else (0, None)
  lo = 0
  hi = len(rows)
  while lo < hi:
    mid = (lo + hi) // 2
    if rows[mid] == target:
      return mid, True
    if mid == len(rows) - 1:
      return len(rows) - 1, None
    if rows[mid] < target and rows[mid + 1] > target:
      return mid, None
    elif  target > rows[mid]:
      lo = mid
    else:
      hi = mid
  return len(rows) - 1, None


def binary_search(lst, target):
  if not lst:
    return False
  if len(lst) == 1:
    return lst[0] == target
  lo = 0
  hi = len(lst)
  while lo <= hi:
    mid = (lo + hi) // 2
    if lst[mid] == target:
      return True
    elif target > lst[mid]:
      if lo == mid:
        break
      lo = mid
    elif target < lst[mid]:
      hi = mid
  return False


class Solution1:
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0] or matrix[0][0] > target:
      return False
    row, result = binary_row([row[0] for row in matrix], target)
    if result is not None:
      return result
    return binary_search(matrix[row], target)


def _translate(index, rows, cols):
  """Returns (row, col) for overall index."""
  row = index // cols
  col = index % cols
  return row, col


class Solution:
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]:
      return False
    # Strategy: binary search, but treat the matrix as if
    #   it was one long array. Translate overall index into
    #   row/col indices.
    m, n = len(matrix), len(matrix[0])  # num row, num cols
    start = 0  # indices as if matrix was one long list
    end = m * n - 1  # incluive
    while start <= end and start >= 0 and end < m * n:
      mid = (start + end) // 2
      row, col = _translate(mid, m, n)
      if target == matrix[row][col]:
        return True
      elif target > matrix[row][col]:
        start = mid + 1
      else:  # target < matrix[row][col]
        end = mid - 1
    return False


s = Solution()
assert not s.searchMatrix([[-10,-8,-8,-8],[-5,-4,-2,0]], 7)
assert s.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 3)
assert not s.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 13)
assert not s.searchMatrix([[1, 1]], 0)
assert not s.searchMatrix([[1, 1]], 2)
assert not s.searchMatrix([[-10,-8,-8,-8],[-5,-4,-2,0]], 7)
print('All tests passed!')
