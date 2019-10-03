# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []

    def preorder(node):
      if not node:
        return
      result.append(node.val)
      preorder(node.left)
      preorder(node.right)

    preorder(root)
    return result
