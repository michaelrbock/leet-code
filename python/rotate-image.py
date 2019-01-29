class Solution:
  def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # 1. Flip over horizontal axis.
    for i in range(len(matrix) // 2):
      matrix[i], matrix[-1 - i] = matrix[-1 - i], matrix[i]

    # 2. Transpose over top-left to bottom-right diag.
    for i in range(len(matrix)):
      for j in range(i + 1, len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


s = Solution()

test1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(test1)
assert test1 == [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

test2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(test2)
assert test2 == [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
