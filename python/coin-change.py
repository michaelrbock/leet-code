class Solution:
  def __init__(self):
    self.cache = {}

  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    return self.coin_change_dp(coins, amount)

  def coin_change_rec(self, coins, amount):
    if amount in self.cache:
      return self.cache[amount]
    if amount == 0:
      return 0
    min_count = float('inf')
    for coin in reversed(coins):
      if coin <= amount:
        res = self.coin_change_rec(coins, amount - coin)
        if res != -1:
          min_count = min(min_count, res + 1)
    self.cache[amount] = min_count if min_count != float('inf') else -1
    return self.cache[amount]

  def coin_change_dp(self, coins, amount):
    memo = [0]  # index = amount, value = min number of coins.
    for i in range(1, amount + 1):
      min_count = float('inf')
      for coin in coins:
        diff = i - coin
        if diff >= 0 and memo[diff] != -1:
          min_count = min(min_count, memo[diff] + 1)
      memo.append(min_count if min_count != float('inf') else -1)
    return memo[-1]


# print(Solution().coinChange([1, 2, 5], 11))
assert Solution().coinChange([1, 2, 5], 11) == 3
assert Solution().coinChange([2], 3) == -1
assert Solution().coinChange([186, 419, 83, 408], 6249) == 20
assert Solution().coinChange([94, 485, 208, 129, 301, 312, 479, 254], 4589) == 10
assert Solution().coinChange([235, 326, 180, 11, 61, 483, 464, 125, 403, 241], 5926) == 14
print('All tests passed!')
