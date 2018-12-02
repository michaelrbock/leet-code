VALUES = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}


class Solution:
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Strategy:
    #   Keep running total
    #   Start an index at 0 and walk through s.
    #   If s[index] < s[index+1] or index == last,
    #     treat it as a pair (skip index +=2)
    #   else as one digit (index += 1)
    total = 0
    index = 0
    while index < len(s):
      if index == len(s) - 1 or VALUES[s[index]] >= VALUES[s[index+1]]:
        total += VALUES[s[index]]
        index += 1
      else:  # s[index] < s[index+1]
        total += VALUES[s[index+1]] - VALUES[s[index]]
        index += 2
    return total
