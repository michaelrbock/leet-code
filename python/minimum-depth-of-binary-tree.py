from collections import deque


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
    # Strategy: bfs starting from root,
    #   keeping track of height for each node,
    #   return first leaf node's height.
    #   no need for visited set.
    if not root:
      return 0

    to_visit = deque([(1, root)])  # (height, node)
    while to_visit:
      height, node = to_visit.popleft()
      if not node.left and not node.right:
        return height
      if node.left:
        to_visit.append((height + 1, node.left))
      if node.right:
        to_visit.append((height + 1, node.right))
    return -1  # Something went wrong
