from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0, len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return [i+1, j+1]


numbers = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(numbers, target)
assert result == [1, 2]

numbers = [2, 3, 4]
target = 6
result = Solution().twoSum(numbers, target)
assert result == [1, 3]

numbers = [-1, 0]
target = -1
result = Solution().twoSum(numbers, target)
assert result == [1, 2]
