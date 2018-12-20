class Solution:
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    # Strategy:
    #   min on line 0 = triangle[0]
    #   min of spot i on line n = triangle[n][i] + min(prev[i-1], prev[i])
    prev = [triangle[0][0]]  # Base case.
    curr = []
    for row in range(1, len(triangle)):
      for i in range(len(triangle[row])):
        if i == 0:
          curr.append(triangle[row][i] + prev[i])
        elif i == len(triangle[row]) - 1:
          curr.append(triangle[row][i] + prev[i-1])
        else:
          curr.append(triangle[row][i] + min(prev[i], prev[i-1]))
      prev = curr
      curr = []
    return min(prev)
