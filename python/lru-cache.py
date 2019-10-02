class LRUNode:
  def __init__(self, key=None, val=None):
    self.key = key
    self.val = val
    self.prev_node = None
    self.next_node = None


class LRUCache(object):
  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.capacity = capacity
    self.cache = {}  # key: LRUNode.

    # MRU is at head, LRU at tail.
    # When head.next_node == tail, the cache is empty.
    self.head = LRUNode()
    self.tail = LRUNode()
    self.head.next_node = self.tail
    self.tail.prev_node = self.head

  def _insert_at_head(self, node):
    node.next_node = self.head.next_node
    node.prev_node = self.head
    self.head.next_node.prev_node = node
    self.head.next_node = node

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    if key in self.cache:
      ret = self.cache[key].val
      # Move to head.
      move = self.cache[key]
      # Take out.
      move.prev_node.next_node = move.next_node
      move.next_node.prev_node = move.prev_node
      self._insert_at_head(move)
    else:
      ret = -1

    return ret

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: None
    """
    if key in self.cache:
      self.cache[key].val = value
      # Move to head.
      move = self.cache[key]
      # Take out.
      move.prev_node.next_node = move.next_node
      move.next_node.prev_node = move.prev_node
      self._insert_at_head(move)
    else:
      self.cache[key] = LRUNode(key, value)
      self._insert_at_head(self.cache[key])

    if len(self.cache) > self.capacity:
      remove = self.tail.prev_node
      self.tail.prev_node = remove.prev_node
      remove.prev_node.next_node = self.tail
      del self.cache[remove.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
