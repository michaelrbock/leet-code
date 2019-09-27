from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
  def maxDepth(self, root):
    """
    :type root: Node
    :rtype: int
    """
    if not root:
      return 0

    max_depth = float('-inf')

    to_visit = deque([(root, 1)])

    while to_visit:
      curr, depth = to_visit.popleft()

      if not curr.children:
        max_depth = max(max_depth, depth)

      for child in curr.children:
        to_visit.append((child, depth + 1))

    return max_depth
