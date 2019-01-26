def find_pair(nums, start, end, target):
  while start < end:
    sub_total = nums[start] + nums[end]
    if target == sub_total:
      yield nums[start], nums[end]
      start += 1
      end -= 1
    elif target > sub_total:
      start += 1
    else:  # target < sub_total
      end -=1


class Solution:
  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    results = []
    result_set = set()
    for start in range(len(nums) - 3):
      for end in range(len(nums) - 1, start + 2, -1):
        sub_total = nums[start] + nums[end]
        diff = target - sub_total
        for middle_nums in find_pair(nums, start + 1, end - 1, diff):
          result = [nums[start], middle_nums[0], middle_nums[1], nums[end]]
          if tuple(result) not in result_set:
            results.append(result)
            result_set.add(tuple(result))
    return results


s = Solution()
assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2],[-2,  0, 0, 2],[-1,  0, 0, 1]]
assert s.fourSum([2, 7, 4, 0, 9, 5, 1, 3], 20) == [[0, 4, 7, 9], [1, 3, 7, 9], [2, 4, 5, 9]]
assert s.fourSum([], 0) == []
assert s.fourSum([0, 0, 0], 0) == []
assert s.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
assert s.fourSum([-3,-1,0,2,4,5], 0) == [[-3, -1, 0, 4]]
assert s.fourSum([-5,5,4,-3,0,0,4,-2], 4) == [[-5,0,4,5],[-3,-2,4,5]]
