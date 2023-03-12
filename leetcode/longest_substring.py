from collections import Counter
from email.policy import default

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(exp: str):
            storage = set()
            for c in exp:
                if c in storage:
                    return False
                else:
                    storage.add(c)
            return True
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                selection = s[i:j+1]
                if check(selection) and len(selection) > result:
                    result = len(selection)
        return result
    
result = Solution().lengthOfLongestSubstring(s = "abcabcbb")
assert result == 3
print(result )

result = Solution().lengthOfLongestSubstring(s = "bbbbb")
assert result == 1
print(result )

result = Solution().lengthOfLongestSubstring(s = "pwwkew")
assert result == 3
print(result )

result = Solution().lengthOfLongestSubstring(s = " ")
assert result == 1
print(result )


d = []
d.sor
            
        