class Solution:
  def change(self, amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    memo = [0] * (amount + 1)
    memo[0] = 1
    for coin in coins:
      for amt in range(1, amount + 1):
        if amt >= coin:
          memo[amt] += memo[amt - coin]

    return memo[amount]

s = Solution()
assert s.change(3, [2]) == 0
assert s.change(10, [10]) == 1
assert s.change(5, [1, 2, 5]) == 4


class Solution1:
  def change(self, amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    count = [0]

    def change_rec(amount, index):
      if amount < 0:
        return
      elif amount == 0:
        count[0] += 1
      for i in range(index, len(coins)):
        change_rec(amount - coins[i], i)

    change_rec(amount, 0)
    return count[0]

s = Solution1()
assert s.change(3, [2]) == 0
assert s.change(10, [10]) == 1
assert s.change(5, [1, 2, 5]) == 4
