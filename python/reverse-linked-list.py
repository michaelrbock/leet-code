# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    curr = head

    # No need for special cases for empty or 1-node lists.
    while curr is not None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    # prev is the new head.
    return prev