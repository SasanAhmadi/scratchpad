from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sub_array = result = nums[0]

        for i in nums[1:]:
            current_sub_array = max(i, current_sub_array + i)
            result = max(result, current_sub_array)
        return result


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = Solution().maxSubArray(nums)
assert result == 6

nums = [1]
result = Solution().maxSubArray(nums)
assert result == 1

nums = [5, 4, -1, 7, 8]
result = Solution().maxSubArray(nums)
assert result == 23
