"""
"""

from collections import Counter


class Solution:
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_counter = Counter(nums)
    return max(nums_counter, key=nums_counter.get)
