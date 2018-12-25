from collections import Counter


class Solution:
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    counts = Counter(s)
    for index, char in enumerate(s):
      if counts[char] == 1:
        return index
    return -1


s = Solution()
assert s.firstUniqChar('leetcode') == 0
assert s.firstUniqChar('loveleetcode') == 2
