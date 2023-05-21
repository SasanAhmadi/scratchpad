from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -math.inf
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                result = max(result, current_sum)

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
