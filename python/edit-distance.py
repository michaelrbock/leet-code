class Solution:
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    cache = {}
    def min_distance_rec(i, j):
      print(i, j)
      if i == 0:
        return j
      if j == 0:
        return i
      match = min_distance_rec(i - 1, j - 1) + (1 if word1[i] != word2[j] else 0)
      insert = min_distance_rec(i, j - 1) + 1
      delete = min_distance_rec(i - 1, j) + 1
      return min(match, insert, delete)
    return min_distance_rec(len(word1) - 1, len(word2) - 1)


s = Solution()
print(s.minDistance('horse', 'rose'))
