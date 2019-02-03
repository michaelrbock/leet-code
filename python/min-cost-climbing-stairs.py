class Solution:
  def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    prev, curr = 0, 0
    for i in range(len(cost)):
      prev, curr = curr, cost[i] + min(prev, curr)
    return min(prev, curr)
