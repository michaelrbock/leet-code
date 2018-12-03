"""
Strategy:
  For each index in s:
    Call another function that walks two pointers, start (index - 1)
    and end (index + 1) away in opposite direction as long as in-bounds
    and the chars at s[start] and s[end] are equal and returns palin.
  Additionally, if s[index] == s[index+1], then call that function with
    start (index - 1) and end (index + 2).
  Store and return longest.
"""

def _find_palin(s, start, end):
  if start < 0 or end >= len(s) or s[start] != s[end]:
    return s[start+1:end]
  while start >= 0 and end < len(s) and s[start] == s[end]:
    start -= 1
    end += 1
  return s[start+1:end]

class Solution:
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    longest = ''
    for index, char in enumerate(s):
      palin = _find_palin(s, index - 1, index + 1)
      if len(palin) > len(longest):
        longest = palin
      if index < len(s) - 1 and char == s[index + 1]:
        palin = _find_palin(s, index - 1, index + 2)
        if len(palin) > len(longest):
          longest = palin
    return longest
