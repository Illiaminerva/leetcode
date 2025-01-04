class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        cur_prod = 1
        for i in range(len(nums) - 1):
            cur_prod *= nums[i]
            res[i+1] *= cur_prod
        cur_prod = 1
        for i in range(len(nums) - 1, 0, -1):
            cur_prod *= nums[i]
            res[i-1] *= cur_prod
        return res