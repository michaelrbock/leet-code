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
