"""
https://en.wikipedia.org/wiki/Maximum_subarray_problem
Could also be solved vya divide & conquer.

Time: O(n)
"""

class Solution:
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_total = float('-inf')
    current_total = 0

    for num in nums:
      if num > 0:
        if current_total < 0:
          # If num is positive and current_total is negative,
          # start a new sub-list.
          current_total = num
        else:
          current_total += num
      else:  # num is <= 0
        if num > max_total:
          # Make sure we capture the max non-positive number.
          current_total = num
        else:
          current_total += num

      if current_total > max_total:
        max_total = current_total

    return max_total
