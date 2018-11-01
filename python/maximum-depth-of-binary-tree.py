from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0
    max_depth = 0
    to_visit = deque([(root, 1)])
    while to_visit:
      node, depth = to_visit.popleft()
      max_depth = max(depth, max_depth)
      new_depth = depth + 1
      if node.left:
        to_visit.append((node.left, new_depth))
      if node.right:
        to_visit.append((node.right, new_depth))
    return max_depth
