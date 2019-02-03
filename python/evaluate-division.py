from collections import defaultdict, deque


def build_graph(equations, values):
  graph = defaultdict(dict)
  for i in range(len(equations)):
    first, second = equations[i]
    graph[first][second] = values[i]
    graph[second][first] = 1/values[i]
  return graph


def execute(query, graph):
  start, end = query
  if start not in graph or end not in graph:
    return -1.0
  visited = set()
  to_visit = deque([(1.0, start)])  # total, variable
  while to_visit:
    total, curr = to_visit.popleft()
    if curr == end:
      return total
    visited.add(curr)
    for neighbor in graph[curr]:
      if neighbor not in visited:
        to_visit.append((total * graph[curr][neighbor], neighbor))
  return -1.0


class Solution:
  def calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    # 1. Build graph.
    graph = build_graph(equations, values)

    # 2. Execute each query.
    results = []
    for query in queries:
      results.append(execute(query, graph))

    return results
