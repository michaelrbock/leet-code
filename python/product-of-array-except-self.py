#   [ 1,  2, 3,4]
# l [ X,  1, 2,6]
# r [24,12,  4,X]
# o [24,12,  8,6]

class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    to_left = [1]
    to_right = [1]

    product = 1
    for i in range(len(nums) - 1):
      product *= nums[i]
      to_left.append(product)

    product = 1
    for i in range(len(nums) - 1, 0, -1):
      product *= nums[i]
      to_right.append(product)
    to_right = to_right[::-1]

    output = []
    for i in range(len(nums)):
      output.append(to_left[i] * to_right[i])

    return output
