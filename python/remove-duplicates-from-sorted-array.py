class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    # Two pointers: slow & fast.
    slow = 0
    fast = 0
    while slow < len(nums) and fast < len(nums):
      fast += 1
      while fast < len(nums) and nums[fast - 1] == nums[fast]:
        fast += 1
      nums[slow] = nums[fast - 1]
      slow += 1
    return slow
