class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, r):
            if r == target and i == len(nums):
                return 1
            if i == len(nums):
                return 0
            if (i, r) in dp:
                return dp[(i, r)]
            dp[(i, r)] = dfs(i+1, r - nums[i]) + dfs(i+1, r + nums[i])
            return dp[(i, r)]
        return dfs(0, 0)


        