class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum