from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def add_number(digit, combinations):
            chars = letters[digit[0]]
            result = []
            if combinations:
                for j in combinations:
                    for i in chars:
                        result.append(j+i)
            else:
                for i in chars:
                    result.append(i)
                    
            if len(digit) > 1:
                result = add_number(digit[1:], result)
            
            return result
        
        return add_number(digits, [])
            
result = Solution().letterCombinations("23")
assert result == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

result = Solution().letterCombinations("")
assert result == []

result = Solution().letterCombinations("2")
assert result == ["a", "b", "c"]