from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        visited = set()

        for i in range(len(intervals)):
            if i in visited:
                continue

            new_range = intervals[i]

            for r in result:
                if r[0] <= new_range[0] <= r[1] or r[0] <= new_range[1] <= r[1] or \
                    new_range[0] <= r[0] <= new_range[1] or new_range[0] <= r[1] <= new_range[1]:

                    r[0] = min(new_range[0], r[0])
                    r[1] = max(new_range[1], r[1])
                    new_range = r
                    visited.add(i)
                    break

            for j in range(i+1, len(intervals)):
                if j in visited:
                    continue

                candidate = intervals[j]
                if candidate[0] <= new_range[0] <= candidate[1] or candidate[0] <= new_range[1] <= candidate[1] or \
                    new_range[0] <= candidate[0] <= new_range[1] or new_range[0] <= candidate[1] <= new_range[1]:

                    new_range[0] = min(new_range[0], candidate[0])
                    new_range[1] = max(new_range[1], candidate[1])

                    visited.add(j)

            visited.add(i)
            if not new_range in result:
                result.append(new_range)

        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
result = Solution().merge(intervals)
assert result == [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
result = Solution().merge(intervals)
assert result == [[1,5]]

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
result = Solution().merge(intervals)
assert result == [[1,10]]

intervals = [[0,0],[0,2],[1,3],[3,5],[3,5],[3,4],[4,4],[4,5],[4,6],[4,6],[5,6]]
result = Solution().merge(intervals)
assert result == [[0, 6]]

intervals = [[3,5],[0,0],[4,4],[0,2],[5,6],[4,5],[3,5],[1,3],[4,6],[4,6],[3,4]]
result = Solution().merge(intervals)
assert result == [[0, 6]]