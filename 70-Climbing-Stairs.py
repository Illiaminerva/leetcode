class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        if n <= 2:
            return n
        prev, cur = 1, 2
        for i in range(n-2):
            cur += prev
            prev = cur - prev
        return cur