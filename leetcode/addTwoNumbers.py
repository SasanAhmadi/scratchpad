
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryon = 0
        tempHead = ListNode(0)
        current = tempHead
        while l1 or l2 or carryon:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sumColumn = l1_val + l2_val + carryon
            carryon = sumColumn // 10

            current.next = ListNode(sumColumn % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return tempHead.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


l2 = ListNode(6)
l2.next = ListNode(5)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
assertion = []
while True:
    if result:
        assertion.append(result.val)
        result = result.next
    else:
        break

assert [8, 9, 7] == assertion

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
assertion = []
while True:
    if result:
        assertion.append(result.val)
        result = result.next
    else:
        break

assert [8,9,9,9,0,0,0,1] == assertion