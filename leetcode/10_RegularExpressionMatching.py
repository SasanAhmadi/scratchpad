class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not 1 <= len(s) <= 20:
            return False
        if not 1 <= len(p) <= 30:
            return False
        if s.lower() != s:
            return False
        input = p.replace('.', '').replace('*', '')
        if not (input.isalpha() and input.lower() == input or input == ''):
            return False
        
        return self._match(s, p)

    def _match(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self._match(s, p[2:]) or
                    first_match and self._match(s[1:], p))
        else:
            return first_match and self._match(s[1:], p[1:])
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.isMatch(s = "aa", p = "a") == False
    assert sol.isMatch(s = "aa", p = "a*") == True
    assert sol.isMatch(s = "ab", p = ".*") == True
        