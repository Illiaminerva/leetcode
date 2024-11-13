class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(i, curStr):
            if i >= len(digits):
                res.append(curStr)
                return
            for d in digitMap[digits[i]]:
                backtrack(i+1, curStr + d)
        backtrack(0, "")
        return res 

                
