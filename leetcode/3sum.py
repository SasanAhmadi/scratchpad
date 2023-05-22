from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def two_sum(i):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                two_sum(i)

        return result


nums = [-1, 0, 1, 2, -1, -4]
result = Solution().threeSum(nums)
assert result == [[-1, -1, 2], [-1, 0, 1]]

nums = [0, 1, 1]
result = Solution().threeSum(nums)
assert result == []

nums = [0, 0, 0]
result = Solution().threeSum(nums)
assert result == [[0, 0, 0]]
