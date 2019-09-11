# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    serialized = {}
    if not root:
      return serialized

    def serialize_rec(node, index):
      serialized[index] = node.val
      if node.left:
        serialize_rec(node.left, 2 * index)
      if node.right:
        serialize_rec(node.right, 2 * index + 1)

    serialize_rec(root, 1)
    return serialized

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if not data:
      return None
    root = TreeNode(data[1])

    def deserialize_rec(node, index):
      node.val = data[index]
      left_index = 2 * index
      if left_index in data:
        node.left = TreeNode(data[left_index])
        deserialize_rec(node.left, left_index)
      right_index = 2 * index + 1
      if right_index in data:
        node.right = TreeNode(data[right_index])
        deserialize_rec(node.right, right_index)

    deserialize_rec(root, 1)
    return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
