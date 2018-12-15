class Solution:
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Strategy: DFS (via recursion) on graph where at each point you can add
    #   one of the nums in 'nums' into 'so_far'.
    results = []

    def permute_rec(nums, so_far):
      if not nums:
        results.append(so_far)
      for i in range(len(nums)):
        permute_rec(nums[:i] + nums[i+1:], so_far + [nums[i]])

    permute_rec(nums, [])
    return results


s = Solution()
assert s.permute([1]) == [[1]]
assert s.permute([1, 2]) == [[1, 2], [2, 1]]
assert len(s.permute([1, 2, 3])) == 6
print('All tests passed!')
