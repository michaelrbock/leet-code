class Solution:
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []

    def subsets_rec(nums, so_far):
      if not nums:
        results.append(so_far)
        return
      subsets_rec(nums[1:], so_far)  # Don't take nums[0].
      subsets_rec(nums[1:], so_far + [nums[0]]) # Take nums[0].

    subsets_rec(nums, [])
    return results


s = Solution()
assert s.subsets([]) == [[]]
assert s.subsets([1]) == [[], [1]]
assert len(s.subsets([1, 2])) == 4
assert len(s.subsets([1, 2, 3])) == 8
print('All tests passed')
