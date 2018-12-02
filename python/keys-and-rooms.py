from collections import deque

class Solution:
  def canVisitAllRooms(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    visited = set()
    to_visit = deque([0])
    while to_visit:
      current = to_visit.popleft()
      visited.add(current)
      for key in rooms[current]:
        if key not in visited:
          to_visit.append(key)
    return len(visited) == len(rooms)
