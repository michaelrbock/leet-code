from collections import defaultdict, deque


def _replace(word, i):
  return word[:i] + '_' + word[i+1:]


def build_graph(word_list):
  graph = defaultdict(list)
  for word in word_list:
    for i in range(len(word)):
      graph[_replace(word, i)].append(word)
  return graph


class Solution:
  def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    graph = build_graph(wordList)

    visited = set()
    to_visit = deque([(1, beginWord)])  # (steps, word)
    while to_visit:
      steps, word = to_visit.popleft()
      if word == endWord:
        return steps
      visited.add(word)
      for i in range(len(word)):
        for adjacent_word in graph[_replace(word, i)]:
          if adjacent_word not in visited:
            to_visit.append((steps + 1, adjacent_word))

    return 0


s = Solution()
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
