class Solution:
  def __init__(self):
    self.cache = {}

  def maxProfit(self, prices):
    def max_profit_rec(i, owns):
      key = (i, owns)
      if key in self.cache:
        return self.cache[key]

      if i >= len(prices):
        res = 0
      elif owns is not None:
        sell = prices[i] + max_profit_rec(i + 2, None)
        hold = max_profit_rec(i + 1, owns)
        res = max(sell, hold)
      else:
        hold = max_profit_rec(i + 1, None)
        buy = max_profit_rec(i + 1, prices[i]) - prices[i]
        res = max(hold, buy)

      self.cache[key] = res
      return res

    return max_profit_rec(0, None)


assert Solution().maxProfit([]) == 0
assert Solution().maxProfit([0, 2]) == 2
assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3
assert Solution().maxProfit([7, 6, 5, 4, 3]) == 0
