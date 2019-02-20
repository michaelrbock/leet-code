class Solution:
  def matrixReshape(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
    if r * c != len(nums) * len(nums[0]): return nums

    row, col = 0, 0  # In current nums matrix.
    new_matrix = []
    for i in range(r):
      new_matrix.append([])
      for j in range(c):
        new_matrix[i].append(nums[row][col])
        col += 1
        if col >= len(nums[0]):
          col = 0
          row += 1

    return new_matrix
