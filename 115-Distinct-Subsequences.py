from collections import defaultdict
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        if len(s) < len(t):
            return 0
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                res = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                res = dfs(i+1, j)
            dp[(i, j)] = res
            return res
        return dfs(0, 0)
            