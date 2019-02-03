# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and not l2: return None
    elif not l1: return l2
    elif not l2: return l1

    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0
    while l1 or l2:
      l1_val = l1.val if l1 else 0
      l2_val = l2.val if l2 else 0
      next_val = l1_val + l2_val + carry
      carry = next_val // 10
      curr.next = ListNode(next_val % 10)
      curr = curr.next
      if l1: l1 = l1.next
      if l2: l2 = l2.next
    if carry:
      curr.next = ListNode(carry)

    return dummy_head.next
