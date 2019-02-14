import heapq
import math


def distance(x1, y1, x2, y2):
  return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


class Solution:
  def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
    # Strategy: keep a max heap of at most K elements
    # which are closest to origin by euclidean distance.
    heap = []  # Stores Tuple(dist: int, Point: List[int])

    for point in points:
      # Negative to make Python heap into max heap.
      dist = distance(0, 0, point[0], point[1]) * -1
      # Eject max if heap at capacity, heap[i][0] is -dist.
      if len(heap) == K:
        if dist > heap[0][0]:
          heapq.heappushpop(heap, (dist, point))
      # Else add to heap.
      else:
        heapq.heappush(heap, (dist, point))
    return [value[1] for value in heap]  # Just return points (index 1).
