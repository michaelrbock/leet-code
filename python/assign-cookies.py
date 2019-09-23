class Solution(object):
  def findContentChildren(self, g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    satisfied = 0

    g.sort(reverse=True)
    s.sort(reverse=True)

    g_index = 0
    s_index = 0

    while g_index < len(g) and s_index < len(s):
      if g[g_index] <= s[s_index]:
        satisfied += 1
        g_index += 1
        s_index += 1
      else:
        g_index += 1

    return satisfied
