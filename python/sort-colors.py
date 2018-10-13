"""
Counting sort.

Better: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

Time: O(n)
Space: O(n)
"""

from collections import Counter


class Solution:
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums_counter = Counter(nums)
    index = 0
    for num, count in nums_counter.items():
      for _ in range(count):
        nums[index] = num
        index += 1a
