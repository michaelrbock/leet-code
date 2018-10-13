"""
DFS, generating graph on the fly, keeping track of visited and depth so far.
"""


from collections import deque


class Solution:
  def openLock(self, deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    to_visit = deque([('0000', 0)])
    visited = set(['0000'])
    deadends_set = set(deadends)
    while to_visit:
      current, depth = to_visit.popleft()
      if current in deadends_set:
        continue
      for i in range(4):
        change = int(current[i])
        forward = current[:i] + str((change + 1) % 10) + current[i+1:]
        if change == 0:
          back = current[:i] + '9' + current[i+1:]
        else:
          back = current[:i] + str(change - 1) + current[i+1:]
        if forward == target or back == target:
          return depth + 1
        if forward not in visited:
          visited.add(forward)
          to_visit.append((forward, depth+1))
        if back not in visited:
          visited.add(back)
          to_visit.append((back, depth+1))
    return -1
