from collections import Counter


class Solution:
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return Counter(s) == Counter(t)


s = Solution()
assert s.isAnagram('anagram', 'nagaram')
assert not s.isAnagram('rat', 'car')
