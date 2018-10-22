class Solution:
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_to_index = {}
    for index, num in enumerate(nums):
      match = target - num
      if match in num_to_index:
        return sorted([index, num_to_index[match]])
      num_to_index[num] = index
