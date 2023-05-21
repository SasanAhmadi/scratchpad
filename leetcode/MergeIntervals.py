from typing import List
import copy


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        sorted_input = sorted(copy.deepcopy(intervals), key=lambda x: x[0])

        for i in sorted_input:
            last_item = result[-1:]

            if last_item and last_item[0][1] >= i[0]:
                last_item[0][1] = max(i[1], last_item[0][1])
            else:
                result.append(i)

        return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = Solution().merge(intervals)
assert result == [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
result = Solution().merge(intervals)
assert result == [[1, 5]]

intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
result = Solution().merge(intervals)
assert result == [[1, 10]]

intervals = [[0, 0], [0, 2], [1, 3], [3, 5], [3, 5], [3, 4], [4, 4], [4, 5], [4, 6], [4, 6], [5, 6]]
result = Solution().merge(intervals)
assert result == [[0, 6]]

intervals = [[3, 5], [0, 0], [4, 4], [0, 2], [5, 6], [4, 5], [3, 5], [1, 3], [4, 6], [4, 6], [3, 4]]
result = Solution().merge(intervals)
assert result == [[0, 6]]
