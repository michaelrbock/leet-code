class Solution:
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    # memo[i][j] represents the edit distance between the first i chars of word1
    # and j chars of word2.
    memo = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
      for j in range(len(word2) + 1):
        # If word1 is empty, must insert the rest of word2.
        if i == 0:
          memo[i][j] = j
        # If word2 is empty, must insert the rest of word1.
        elif j == 0:
          memo[i][j] = i
        # If the previous characters are the same, do not add to edit distance.
        elif word1[i-1] == word2[j-1]:
          memo[i][j] = memo[i-1][j-1]
        # Otherwise, take the min of replace, remove, insert.
        else:
          memo[i][j] = 1 + min(memo[i-1][j-1], memo[i-1][j], memo[i][j-1])
    print(memo)
    return memo[-1][-1]



s = Solution()
assert s.minDistance('', 'rose') == 4
assert s.minDistance('rose', '') == 4
assert s.minDistance('horse', 'ros') == 3
assert s.minDistance('intention', 'execution') == 5


class Solution1:
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    cache = {}

    def min_distance_rec(i, j):
      if (i, j) in cache:
        return cache[(i, j)]
      """i and j are length of word1 and word2 respectively."""
      if i == 0:
        return j
      if j == 0:
        return i
      if word1[i - 1] == word2[j - 1]:
        res = min_distance_rec(i - 1, j - 1)
      else:
        res = 1 + min(
            min_distance_rec(i - 1, j - 1),  # Replace.
            min_distance_rec(i - 1, j),  # Remove.
            min_distance_rec(i, j - 1))  # Insert.
      cache[(i, j)] = res
      return res

    return min_distance_rec(len(word1), len(word2))


s = Solution1()
assert s.minDistance('', 'rose') == 4
assert s.minDistance('rose', '') == 4
assert s.minDistance('horse', 'ros') == 3
assert s.minDistance('intention', 'execution') == 5
