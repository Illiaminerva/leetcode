class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = {}
        def dfs(i, j, k):
            if i == len(s1) and j == len(s2):
                return True
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if (i, j) in dp:
                return dp[(i, j)]
            result = (s1[i] == s3[k] and dfs(i+1, j, k+1)) or (s2[j] == s3[k] and dfs(i, j+1, k+1))
            dp[(i, j)] = result
            return result
        return dfs(0, 0, 0)
