class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string_number = str(x)
        return int(string_number[::-1]) == x

x = 121
result = Solution().isPalindrome(x)
assert result == True
# Explanation: 121 reads as 121 from left to right and from right to left.

x = -121
result = Solution().isPalindrome(x)
assert result == False
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

x = 10
result = Solution().isPalindrome(x)
assert result == False
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.