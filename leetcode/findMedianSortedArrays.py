from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not 0 <= len(nums1) <= 1000:
            return 0
        if not 0 <= len(nums2) <= 1000:
            return 0
        if not 1 <= len(nums1) + len(nums2) <= 2000:
            return 0
        
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 > 0:
            return nums[(len(nums) // 2)]
        else: 
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        
if __name__ == "__main__":
    g = Solution()
    assert g.findMedianSortedArrays([1,2], [3,4,5]) == 3
    assert g.findMedianSortedArrays([1,3], [2]) == 2
    assert g.findMedianSortedArrays([1,2], [3,4]) == 2.5