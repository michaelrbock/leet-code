class Solution:
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
      return nums[0]
    # Strategy: modified binary search. Comparing elem to final.
    start, end = 0, len(nums) - 1  # start and end are inclusive.
    while start <= end:
      mid = (start + end) // 2
      if nums[mid] < nums[mid-1]:
        return nums[mid]
      elif nums[mid] > nums[-1]:
        start = mid + 1
      elif nums[mid] < nums[-1]:
        end = mid - 1
