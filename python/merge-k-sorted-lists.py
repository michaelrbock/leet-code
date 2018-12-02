import heapq

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    # value, index, node
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    head = ListNode(0)
    current = head
    while heap:
      val, index, node = heapq.heappop(heap)
      current.next = node
      current = current.next
      if node.next:
        heapq.heappush(heap, (node.next.val, index, node.next))
    return head.next
