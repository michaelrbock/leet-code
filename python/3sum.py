class Solution:
  def _find_pairs(self, nums, start, end, target):
    while start < end:
      total = nums[start] + nums[end]
      if total == target:
        yield nums[start], nums[end]
        start += 1
        end -= 1
      elif total < target:
        start += 1
      else:  # total > target
        end -= 1

  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    if len(nums) < 3: return results
    nums.sort()

    results_set = set()
    for i in range(len(nums) - 2):
      diff = 0 - nums[i]
      for pair in self._find_pairs(nums, i + 1, len(nums) - 1, diff):
        result = [nums[i], pair[0], pair[1]]
        if tuple(result) not in results_set:
          results_set.add(tuple(result))
          results.append(result)

    return results


s = Solution()
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2],[-1, 0, 1]]
