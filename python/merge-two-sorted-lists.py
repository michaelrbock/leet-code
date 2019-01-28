# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1: return l2
    if not l2: return l1
    head = None
    if l1.val <= l2.val:
      head = l1
      l1 = l1.next
    else:
      head = l2
      l2 = l2.next
    curr = head
    curr1, curr2 = l1, l2
    while curr1 and curr2:
      if curr1.val <= curr2.val:
        curr.next = curr1
        curr1 = curr1.next
      else:
        curr.next = curr2
        curr2 = curr2.next
      curr = curr.next
    if curr1:
      curr.next = curr1
    elif curr2:
      curr.next = curr2
    return head

s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

res = s.mergeTwoLists(l1, l2)
res_list = []
while res:
  res_list.append(res.val)
  res = res.next
assert res_list == [1, 1, 2, 3, 4, 4]
