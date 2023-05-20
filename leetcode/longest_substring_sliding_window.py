# from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        mpc = {}
        for j in range(len(s)):
            if s[j] in mpc:
                i = max(i, mpc[s[j]])

            ans = max(ans, j-i+1)
            mpc[s[j]] = j+1
        return ans

s = "abcabcbb"
assert Solution().lengthOfLongestSubstring(s) == 3

s = "bbbbb"
assert Solution().lengthOfLongestSubstring(s) == 1

s = "pwwkew"
assert Solution().lengthOfLongestSubstring(s) == 3

result = Solution().lengthOfLongestSubstring(s = " ")
assert result == 1