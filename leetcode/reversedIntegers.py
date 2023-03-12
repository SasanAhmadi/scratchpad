class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        input = str(abs(x))
        result = sign * int(input[::-1])
        if -2**31 <= result <= (2**31) - 1:
            return result
        else:
            return 0

result = Solution().reverse(-1232)
print(result)