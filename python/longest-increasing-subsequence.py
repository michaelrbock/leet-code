class Solution(object):
  def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0

    max_lis = 1
    lis_reversed = [1]
    for i in range(len(nums) - 2, -1, -1):
      partial_max = 1
      for j, lis in enumerate(lis_reversed):
        if nums[len(nums) - 1 - j] > nums[i]:
          partial_max = max(partial_max, lis + 1)
      lis_reversed.append(partial_max)
      max_lis = max(max_lis, partial_max)

    return max_lis
