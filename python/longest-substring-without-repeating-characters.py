from collections import defaultdict


class Solution:
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Strategy: Walk fast pointer, adding char counts to dict until overlap.
    #   Once overlap, walk slow pointer until overlap eliminated.
    #   Keep track of longest during process and return.
    slow = 0
    fast = 0
    longest = 0
    counts = defaultdict(int)
    while fast < len(s):
      counts[s[fast]] += 1
      while slow < fast and counts[s[fast]] > 1:
        counts[s[slow]] -= 1
        slow += 1
      longest = max(longest, fast - slow + 1)
      fast += 1
    return longest


s = Solution()
assert s.lengthOfLongestSubstring('') == 0
assert s.lengthOfLongestSubstring('abcabccbb') == 3
assert s.lengthOfLongestSubstring('bbbb') == 1
assert s.lengthOfLongestSubstring('pwwkew') == 3
