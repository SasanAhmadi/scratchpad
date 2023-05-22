from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) -1

        while l<r:
            logical_height = min(height[l], height[r])
            current_area = logical_height * (r-l)
            area = max(current_area, area)

            if height[l] >= height[r]:
                r-=1
            else:
                l+=1

        return area


height = [1,8,6,2,5,4,8,3,7]
result = Solution().maxArea(height)
assert result == 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

height = [1,1]
result = Solution().maxArea(height)
assert result == 1