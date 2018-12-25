class Solution:
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Strategy: Two pointers, only move pointer in from shorter wall.
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
      max_area = max(max_area,
                     min(height[left], height[right]) * (right - left))
      if height[left] <= height[right]:
        left += 1
      else:  # height[right] > height[left]
        right -= 1

    return max_area


s = Solution()
assert s.maxArea([1,4,5,3]) == 6
assert s.maxArea([1,8,6,2,5,4,3]) == 16
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
