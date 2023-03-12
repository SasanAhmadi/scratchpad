from collections import deque
import queue

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_copy = nums1[:m]
        p1 = 0
        p2 = 0
        for p in range(m+n):
            if p2 >= n or (p1 < m and nums1_copy[p1] < nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1+=1
            else:
                nums1[p] = nums2[p2]
                p2+=1


nums1 = [4,5,6,0,0,0]
m = 3
n = 3
nums2 = [1,2,3]
Solution().merge(nums1=nums1, m=m, n=n, nums2=nums2)
assert nums1 == [1,2,3,4,5,6]            

nums1 = [1,2,3,4,0,0,0]
m = 4
n = 3
nums2 = [4,5,6]
Solution().merge(nums1=nums1, m=m, n=n, nums2=nums2)
assert nums1 == [1,2,3,4,4,5,6]    

nums1 = [-1,0,2,3,4,7,0,0,0,0,0]
m = 6
n = 5
nums2 = [1,2,3,5,6]
Solution().merge(nums1=nums1, m=m, n=n, nums2=nums2)
assert nums1 == [-1,0,1,2,2,3,3,4,5,6,7]

nums1 = [1,2,3,0,0,0]
m = 3 
n = 3
nums2 = [2,5,6]
Solution().merge(nums1=nums1, m=m, n=n, nums2=nums2)
assert nums1 == [1,2,2,3,5,6]

nums1 = [1]
m = 1
n = 0
nums2 = []
Solution().merge(nums1=nums1, m=m, n=n, nums2=nums2)
assert nums1 == [1]

nums1 = [0]
m = 0
n = 1
nums2 = [1]
Solution().merge(nums1=nums1, m=m, n=n, nums2=nums2)
assert nums1 == [1]
