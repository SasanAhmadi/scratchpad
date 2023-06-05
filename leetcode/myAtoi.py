class Solution:
    def myAtoi(self, s: str) -> int:
        stripped = s.lstrip()
        if len(stripped) == 0:
            return 0

        number_range = [-2**31, (2**31)-1]

        sign = 1
        if stripped[0] in ["-", "+"]:
            sign = -1 if stripped[0] == "-" else 1
            stripped = stripped[1:]

        nlen = 0
        for i in range(len(stripped)):
            if not stripped[i].isnumeric():
                break
            nlen += 1

        result = stripped[:nlen]
        result = 0 if len(result) == 0 else result
        result = int(result) * sign
        if result < number_range[0]:
            result = number_range[0]
        elif result > number_range[1]:
            result = number_range[1]

        return result

s = ""
result = Solution().myAtoi(s)
assert result == 0

s = "42"
result = Solution().myAtoi(s)
assert result == 42

s = "   -42"
result = Solution().myAtoi(s)
assert result == -42

s = "4193 with words"
result = Solution().myAtoi(s)
assert result == 4193

s = "words and 987"
result = Solution().myAtoi(s)
assert result == 0
