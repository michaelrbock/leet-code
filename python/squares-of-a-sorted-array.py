def modified_binary_search(arr, target):
  if target < arr[0]:
    return 0
  if target > arr[-1]:
    return len(arr) - 1

  lo = 0
  hi = len(arr) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if target < arr[mid]:
      hi = mid - 1
    elif target > arr[mid]:
      lo = mid + 1
    else:  # target == arr[mid]
      return mid
  # lo = hi + 1 (so lo > hi)
  return lo if (arr[lo] - target) < (target - arr[hi]) else hi


class Solution:
  def sortedSquares(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    if not A: return []
    res = []

    # Find index of closest element to 0.
    min_index = modified_binary_search(A, 0)
    res.append(A[min_index] ** 2)
    left = min_index - 1
    right = min_index + 1
    # then walk l and r pointers out from middle,
    # adding square of smallest of abs value to res.
    while left >= 0 or right < len(A):
      if left >= 0 and right < len(A):
        if abs(A[left]) <= abs(A[right]):
          res.append(A[left] ** 2)
          left -= 1
        else:
          res.append(A[right] ** 2)
          right += 1
      elif left >= 0:
        res.append(A[left] ** 2)
        left -= 1
      else:
        res.append(A[right] ** 2)
        right += 1
    return res
