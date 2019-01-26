from collections import defaultdict, Counter


class Solution:
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    t_counts = Counter(t)
    s_counts = defaultdict(int)
    satisfied = 0  # How many letters in the window satisfy t_counts.
    left, right = 0, 0
    min_size = float('inf')
    min_left, min_right = 0, 0
    while right < len(s):
      # Look for a valid window, grow.
      if satisfied < len(t_counts):
        if s[right] in t_counts:
          s_counts[s[right]] += 1
          if s_counts[s[right]] == t_counts[s[right]]:
            satisfied += 1
        if satisfied == len(t_counts) and right - left < min_size:
          min_size = right - left
          min_left = left
          min_right = right
      # Currently a valid window, shrink.
      while left <= right and satisfied == len(t_counts):
        if right - left < min_size:
          min_size = right - left
          min_left = left
          min_right = right
        if s[left] in t_counts:
          s_counts[s[left]] -= 1
          if s_counts[s[left]] < t_counts[s[left]]:
            satisfied -= 1
          if s_counts[s[left]] == 0:
            del s_counts[s[left]]
        left += 1
      right += 1

    return s[min_left:min_right+1] if min_size != float('inf') else ''

s = Solution()
assert s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
assert s.minWindow('HELLO', 'WORLD') == ''
assert s.minWindow('ABC', 'ABC') == 'ABC'
assert s.minWindow('B', 'BBB') == ''
assert s.minWindow('BB', 'BB') == 'BB'
assert s.minWindow('ab', 'a') == 'a'
assert s.minWindow('a', 'a') == 'a'
assert s.minWindow('ab', 'b') == 'b'
assert s.minWindow('abc', 'b') == 'b'
assert s.minWindow('cabwefgewcwaefgcf', 'cae') == 'cwae'
