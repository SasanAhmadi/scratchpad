
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = min(height[left], height[right]) * (right - left)
                result = max(area, result) 
        return result 
    
result = Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])
print(result)