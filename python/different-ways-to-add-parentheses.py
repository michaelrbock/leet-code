"""
Divide & Conquer, Recursion.
"""


def operate(a, b, operator):
  a = int(a)
  b = int(b)
  if operator == '+':
    return a + b
  elif operator == '-':
    return a - b
  elif operator == '*':
    return a * b


class Solution:
  def diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    if input.isdigit():
      return [int(input)]
    results = []
    for i in range(len(input)):
      if input[i] in set('+-*'):
        sub_results1 = self.diffWaysToCompute(input[:i])
        sub_results2 = self.diffWaysToCompute(input[i+1:])
        for sub1 in sub_results1:
          for sub2 in sub_results2:
            results.append(operate(sub1, sub2, input[i]))
    return results
