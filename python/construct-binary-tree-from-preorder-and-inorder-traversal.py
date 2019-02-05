# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    def search(target, after, before):
      for i in range(after, before):
        if inorder[i] == target:
          return i

    pre_index = [0]

    def build_tree_rec(after, before):
      if after >= before:
        return

      val = preorder[pre_index[0]]
      pre_index[0] += 1
      node = TreeNode(val)
      split_index = search(val, after, before)
      node.left = build_tree_rec(after, split_index)
      node.right = build_tree_rec(split_index + 1, before)
      return node

    return build_tree_rec(0, len(inorder))
