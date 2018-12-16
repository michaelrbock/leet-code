class Solution:
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curr = 0
    max_sum = float('-inf')
    for num in nums:
      if num < 0:
        max_sum = max(max_sum, num)
        curr = max(0, curr + num)
      else:
        curr += num
        max_sum = max(max_sum, curr)
    return max_sum


s = Solution()
assert s.maxSubArray([-1]) == -1
assert s.maxSubArray([-1, 1]) == 1
assert s.maxSubArray([2, -1, 2]) == 3
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
print('All tests passed!')
