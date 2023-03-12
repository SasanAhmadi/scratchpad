class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for l in range(len(s) - i):
                substr = s[i: l]
                if substr == reversed(substr):
                    if len(result) < len(substr):
                        result = substr
                        
        return result
    
result = Solution().longestPalindrome("babad")
print(result)