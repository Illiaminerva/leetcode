class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1,2]
        if n <= 2:
            return memo[n-1]
        for i in range(n-2):
            memo.append(memo[-1] + memo[-2])
        return memo[-1]