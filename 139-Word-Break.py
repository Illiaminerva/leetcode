class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                if len(w) + i <= len(s) and s[i:i + len(w)] == w and dfs(i + len(w)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)