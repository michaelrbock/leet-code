"""
Dynamic Programming.

max_buy[i] = max(-price, buy[i-1])
max_sell[i] = max(buy[i-1] + price, sell[i-1])
"""


class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    prev_sell, sell, prev_buy, buy = 0, 0, float('-inf'), float('-inf')
    for price in prices:
      prev_buy = buy
      buy = max(0 - price, prev_buy)
      prev_sell = sell
      sell = max(prev_buy + price, prev_sell)
    return sell
