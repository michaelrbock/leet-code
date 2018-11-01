PAIRS = {
  ')': '(',
  '}': '{',
  ']': '[',
}


class Solution:
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for char in s:
      if char in PAIRS.values():  # is open symbol
        stack.append(char)
      else:  # is close symbol
        if not stack:
          return False
        prev_char = stack.pop()
        if PAIRS[char] != prev_char:
          return False
    return not stack
