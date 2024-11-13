class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            backtrack(i)
        backtrack(0)
        return result