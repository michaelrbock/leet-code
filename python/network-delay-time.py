"""
Create graph; run Dijkstra's; return max cost if all nodes can be reached, -1
otherwise.
"""


from collections import defaultdict
import heapq


class Solution:
  def networkDelayTime(self, times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    graph = defaultdict(dict)
    for (u, v, w) in times:
      graph[u][v] = w

    frontier = []
    heapq.heappush(frontier, (0, K))  # (priority, node)
    node_times = {}
    node_times[K] = 0
    while frontier:
      current = heapq.heappop(frontier)[1]
      for node, time in graph[current].items():
        new_time = node_times[current] + time
        if node not in node_times or new_time < node_times[node]:
          node_times[node] = new_time
          heapq.heappush(frontier, (new_time, node))

    for node in range(1, N+1):
      if node not in node_times:
        return -1
    return max(node_times.values())
