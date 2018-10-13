"""
BFS.

Time: O(n)
Space: O(h)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0

    # (TreeNode, depth)
    to_visit = [(root, 1)]
    while to_visit:
      current, depth = to_visit.pop(0)
      if not current.left and not current.right:
        return depth
      if current.left:
        to_visit.append((current.left, depth + 1))
      if current.right:
        to_visit.append((current.right, depth + 1))
