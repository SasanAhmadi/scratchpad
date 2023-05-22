from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        if len(strs) == 1:
            return result

        for i in range(0, len(strs)):
            result = result[:min(len(strs[i]), len(result))]
            for j in range(min(len(strs[i]), len(result))):
                if strs[i][:j+1] != result[:j+1]:
                    result = result[:j]
                    break

        return result


strs = ["flower", "flow", "flight"]
result = Solution().longestCommonPrefix(strs)
assert result == "fl"

strs = ["dog", "racecar", "car"]
result = Solution().longestCommonPrefix(strs)
assert result == ""

strs = strs = ["ab", "a"]
result = Solution().longestCommonPrefix(strs)
assert result == "a"
