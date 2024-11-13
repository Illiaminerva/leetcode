class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPali(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True
            
        res = []
        part = []
        def backtrack(i, j):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            if isPali(s, i, j):
                part.append(s[i:j+1])
                backtrack(j+1, j+1)
                part.pop()
            backtrack(i, j+1)
        backtrack(0, 0)
        return res



