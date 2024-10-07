class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        max_robs = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            max_robs.append(max(max_robs[-1], max_robs[-2] + nums[i]))
        return max_robs[-1]