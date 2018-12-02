class Solution:
  def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    J_set = set(J)
    count = 0
    for stone in S:
      if stone in J_set:
        count += 1
    return count
