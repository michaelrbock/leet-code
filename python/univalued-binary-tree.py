# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isUnivalTree(self, root: 'TreeNode') -> 'bool':
    if not root: return True

    def is_unival_tree(node, val):
      if not node: return True
      if node.val != val: return False
      l = is_unival_tree(node.left, node.val)
      r = is_unival_tree(node.right, node.val)
      return l and r

    return is_unival_tree(root, root.val)
