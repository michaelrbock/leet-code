"""
Backtracking/Recursion.
"""

def generate_parens_rec(so_far, opens, closes):
  if opens == 0 and closes == 0:
    return [so_far]
  results = []
  if opens > 0:
    results.extend(generate_parens_rec(so_far + '(', opens - 1, closes))
  if opens < closes:
    results.extend(generate_parens_rec(so_far + ')', opens, closes - 1))
  return results


class Solution:
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    return generate_parens_rec('(', n - 1, n)
