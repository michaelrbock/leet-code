# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution:
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    results = [[]]
    # Strategy: do a BFS and keep track of level
    to_visit = deque([(1, root)])  # (level, node)
    while to_visit:
      level, curr = to_visit.popleft()
      if level > len(results):
        results.append([])
      results[-1].append(curr.val)
      if curr.left:
        to_visit.append((level + 1, curr.left))
      if curr.right:
        to_visit.append((level + 1, curr.right))
    return results
