class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_prev = float('inf')
    total_profit = 0
    for price in prices:
      min_prev = min(min_prev, price)
      if price > min_prev:
        total_profit += price - min_prev
        min_prev = price  # Reset after a sell.
    return total_profit
