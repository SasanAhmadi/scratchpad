# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List,Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for i in lists:
            l = i
            while l:
                result.append(l.val)
                l = l.next
    
        result.sort()
        return result
    
lists = [[1,4,5],[1,3,4],[2,6]]
result = Solution().mergeKLists(lists)
print(result)
lists = []
result = Solution().mergeKLists(lists)
print(result)
lists = [[]]
result = Solution().mergeKLists(lists)
print(result)