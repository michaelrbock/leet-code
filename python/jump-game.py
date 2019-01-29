class Solution:
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    memo = [False for _ in range(len(nums))]
    memo[-1] = True
    for i in range(len(nums) - 2, -1, -1):
      for j in range(min(len(nums) - 1, i + nums[i]), i - 1, -1):
        if memo[j]:
          memo[i] = True
          break
    return memo[0]


s = Solution()
assert s.canJump([2,3,1,1,4])
assert not s.canJump([3,2,1,0,4])
assert s.canJump([1])
assert s.canJump([2,3,1,0,4])
assert not s.canJump([2,2,1,0,4])
