from collections import deque


class Solution:
  def isBipartite(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    color = {}  # red (0) or blue (1)

    def bfs(start):
      to_visit = deque([start])
      while to_visit:
        node = to_visit.popleft()
        for neighbor in graph[node]:
          if neighbor in color and color[neighbor] == color[node]:
            return False
          elif neighbor not in color:
            color[neighbor] = 1 - color[node]
            to_visit.append(neighbor)
      return True

    for node in range(len(graph)):
      if node not in color:
        color[node] = 0
      if not bfs(node):
        return False
    return True


s = Solution()
assert s.isBipartite([[1,3], [0,2], [1,3], [0,2]]) == True
assert s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]) == False
assert s.isBipartite([[],[3],[],[1],[]]) == True
assert s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]) == False
