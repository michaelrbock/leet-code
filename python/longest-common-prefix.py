class Solution:
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ''
    longest = []
    i = 0
    while i < len(strs[0]):
      letter = strs[0][i]
      for j in range(1, len(strs)):
        if i >= len(strs[j]):
          return ''.join(longest)
        elif strs[j][i] != letter:
          return ''.join(longest)
      longest.append(letter)
      i += 1
    return ''.join(longest)


s = Solution()
assert s.longestCommonPrefix(["flower","flow","flight"]) == 'fl'
assert s.longestCommonPrefix(["dog","racecar","car"]) == ''
assert s.longestCommonPrefix(['hello', 'hello']) == 'hello'
