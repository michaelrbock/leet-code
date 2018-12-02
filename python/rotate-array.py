class Solution:
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Mod by length of nums to account for multiple rotational shifts.
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
