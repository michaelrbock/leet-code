"""
Run binary search on the first column, then binary search on that row.

Better: treat the matrix like a sorted list - O(logn).

Time: O(logn + logm)
"""

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


class Solution:
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
