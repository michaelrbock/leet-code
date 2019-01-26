class Solution:
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    n -= 1
    result = []
    while n >= 0:
      digit = n % 26
      result.append(chr(digit + ord('A')))
      n = (n // 26) - 1
    return ''.join(reversed(result))


s = Solution()
assert s.convertToTitle(1) == 'A'
assert s.convertToTitle(2) == 'B'
assert s.convertToTitle(27) == 'AA'