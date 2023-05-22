class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        rows = ["" for i in range(numRows)]
        current_row = 0
        direction = 1 if numRows > 1 else 0

        for i in s:
            rows[current_row] += i
            current_row += direction
            if current_row == numRows - 1 or current_row == 0:
                direction = -1 * direction

        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
result = Solution().convert(s, numRows)
assert result == "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
result = Solution().convert(s, numRows)
assert result == "PINALSIGYAHRPI"

s = "A"
numRows = 1
result = Solution().convert(s, numRows)
assert result == "A"

s = "AB"
numRows = 1
result = Solution().convert(s, numRows)
assert result == "AB"