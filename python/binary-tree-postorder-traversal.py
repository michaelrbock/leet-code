# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root: return []

    result = []

    def postorder_rec(node):
      if node.left:
        postorder_rec(node.left)
      if node.right:
        postorder_rec(node.right)
      result.append(node.val)

    postorder_rec(root)
    return result
