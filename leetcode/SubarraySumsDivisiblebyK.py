from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return 0

nums = [4,5,0,-2,-3,1]
k = 5
result = Solution().subarraysDivByK(nums, k)
assert result == 7

nums = [5]
k = 9
result = Solution().subarraysDivByK(nums, k)
assert result == 0