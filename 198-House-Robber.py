class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            rob1, rob2 = max(rob1, rob2), rob1 + nums[i]
        return max(rob1, rob2)