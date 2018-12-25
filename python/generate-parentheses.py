class Solution:
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    # Strategy: recursive DFS over a tree where you can either place
    #   a left or right paren, pruning when we've created an un-balanced
    #   string.
    results = []

    def parens_rec(to_place, so_far, left_parens):
      if left_parens < 0:
        return  # prune tree.

      if to_place == 0:
        if left_parens == 0:
          results.append(so_far)
        return
      parens_rec(to_place - 1, so_far + '(', left_parens + 1)
      parens_rec(to_place - 1, so_far + ')', left_parens - 1)

    parens_rec(n * 2, '', 0)
    return results


s = Solution()
assert len(s.generateParenthesis(1)) == 1
assert len(s.generateParenthesis(2)) == 2
assert len(s.generateParenthesis(3)) == 5
assert len(s.generateParenthesis(4)) == 14
print(len(s.generateParenthesis(5)))
print(len(s.generateParenthesis(6)))
print(len(s.generateParenthesis(7)))
print(len(s.generateParenthesis(8)))
