class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robSimple(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(robSimple(nums[:-1]), robSimple(nums[1:]))