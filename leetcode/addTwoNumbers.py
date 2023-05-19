
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def calc_sum_remainder(self, l1, l2, carryon):
        n1 = 0
        n2 = 0
        if l1:
            n1 = l1.val
        if l2:
            n2 = l2.val

        sum_current = n1 + n2 + carryon
        if sum_current > 9:
            sum_current = sum_current - 10
            carryon = 1
        else:
            carryon = 0

        return sum_current, carryon

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryon = 0
        cl1 = l1
        cl2 = l2

        master_node = None
        while cl1 or cl2:
            current, carryon = self.calc_sum_remainder(cl1, cl2, carryon)
            cl1 = cl1.next if cl1 else None
            cl2 = cl2.next if cl2 else None
            if not master_node:
                master_node = ListNode(current)
                node = master_node
            else:
                node.next = ListNode(current)
                node = node.next

            if not cl1 and not cl2:
                if carryon > 0:
                    node.next = ListNode(carryon)

        return master_node


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