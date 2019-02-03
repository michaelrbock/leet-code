# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def is_bst_rec(node, gt, lt):
      if not node:
        return True
      if node.val <= gt or node.val >= lt:
        return False
      return (
        is_bst_rec(node.left, gt, node.val) and
        is_bst_rec(node.right, node.val, lt))

    return is_bst_rec(root, float('-inf'), float('inf'))
