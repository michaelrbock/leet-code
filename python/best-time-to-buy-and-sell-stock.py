class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices: return 0
    min_prev = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
      max_profit = max(max_profit, prices[i] - min_prev)
      min_prev = min(min_prev, prices[i])
    return max_profit
