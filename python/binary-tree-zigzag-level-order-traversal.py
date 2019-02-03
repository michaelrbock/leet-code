# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    results = []
    to_visit = deque([(0, root)])  # (level, node)
    next_level = []
    while to_visit:
      level, curr = to_visit.popleft()
      if level > len(results):
        if len(results) % 2 == 0:
          results.append(next_level)
        else:
          results.append(next_level[::-1])
        next_level = []
      next_level.append(curr.val)
      if curr.left:
        to_visit.append((level + 1, curr.left))
      if curr.right:
        to_visit.append((level + 1, curr.right))
    if len(results) % 2 == 0:
      results.append(next_level)
    else:
      results.append(next_level[::-1])
    return results
