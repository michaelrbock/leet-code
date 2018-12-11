from collections import Counter


class Solution:
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Counting sort.
    # Better: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    # Time: O(n)
    # Space: O(n)
    nums_counter = Counter(nums)
    index = 0
    for num in range(3):
      for _ in range(nums_counter[num]):
        nums[index] = num
        index += 1


test_cases = [
  [[2,0,2,1,1,0], [0,0,1,1,2,2]],
  [[], []],
  [[0], [0]],
  [[1], [1]],
  [[2], [2]],
  [[1,2], [1,2]],
  [[2,0], [0,2]],
  [[2,0,1], [0,1,2]],
  [[1,2,0], [0,1,2]],
]

s = Solution()
for case, expected in test_cases:
  s.sortColors(case)
  assert case == expected
