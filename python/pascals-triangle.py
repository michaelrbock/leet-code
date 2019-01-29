class Solution:
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0: return []
    triangle = []
    for i in range(numRows):
      next_row = []
      for j in range(i + 1):
        if j == 0 or j == i:
          next_row.append(1)
        else:
          next_row.append(triangle[-1][j-1] + triangle[-1][j])
      triangle.append(next_row)
    return triangle
