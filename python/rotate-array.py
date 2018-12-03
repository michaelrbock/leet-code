def _reverse(arr, start, end):
  """Reverses arr from start to end (inclusive) in-place."""
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1


class Solution:
  def rotate(self, nums, k):
    """
    Strategy:
      Reverse array, reverse arr up to k, reverse arr after k.
    """
    if k <= 0 or len(nums) < 2:
      return
    # Mod by length of arr to account for multiple rotational shifts.
    k = k % len(nums)
    _reverse(nums, 0, len(nums) - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, len(nums) - 1)

  def rotate1(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Mod by length of arr to account for multiple rotational shifts.
    k = k % len(nums)
    if k <= 0 or not nums:
      return
    start, index = 0, 0  # start and current index.
    next_num = nums[index]
    for iteration in range(len(nums)):
      #print(iteration)
      destination = index - (len(nums) - k)
      next_num, nums[destination] = nums[destination], next_num
      # Convert possibly negative indexes to positive for next itertion.
      index = destination if destination >= 0 else len(nums) + destination
      if index == start:  # Make sure we avoid loops.
        index += 1
        start = index
        next_num = nums[index]
