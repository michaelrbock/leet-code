class Solution1:
  def __init__(self):
    self.cache = {}

  def maxProfit(self, prices):
    print(self.cache)

  def max_profit_rec(self, prices, index, owns, cooldown):
    key = (index, owns, cooldown)
    if key in self.cache:
      return self.cache[key]

    if index == len(prices):
      # Base case.
      res = 0
    elif cooldown:
      # Forced cooldown.
      res = self.max_profit_rec(prices, index + 1, owns, False)
    elif owns is not None:
      # Sell or hold.
      res = max(
        prices[index] + self.max_profit_rec(prices, index + 1, None, True),
        self.max_profit_rec(prices, index + 1, owns, False))
    else:
      # Buy or hold nothing.
      res = max(
        self.max_profit_rec(prices, index + 1, prices[index], False) - prices[index],
        self.max_profit_rec(prices, index + 1, None, False))
    self.cache[key] = res
    return res


# class Solution:
#   def maxProfit(self, prices):



assert Solution1().maxProfit([]) == 0
assert Solution1().maxProfit([0, 2]) == 2
assert Solution1().maxProfit([1, 2, 3, 0, 2]) == 3
assert Solution1().maxProfit([7, 6, 5, 4, 3]) == 0
