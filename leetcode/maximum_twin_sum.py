# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        all_nodes = []

        current = head
        while True:
            all_nodes.append(current.val)
            if current.next:
                current = current.next
            else:
                break

        result = 0
        twin_count = len(all_nodes)//2
        for i in range(twin_count):
            twin_sum = all_nodes[i] + all_nodes[-i-1]
            if twin_sum > result:
                result = twin_sum

        return result


