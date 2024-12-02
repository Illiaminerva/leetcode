class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result

                

            


























        #     if i == len(nums):
        #         return
        #     for val in range(i,len(nums)):
        #         if val > i and nums[val] == nums[val-1]:
        #             continue
        #         lst.append(nums[val])
        #         ans.append(lst[:])
        #         backtrack(val+1,lst,nums,ans)
        #         lst.pop()
        # ans.append([])
        # backtrack(0,[],nums,ans)
        # return ans

        # nums.sort()
        # ans = []
        # def backtrack(i,lst,nums,ans):
        #     if i == len(nums):
        #         return
        #     for val in range(i,len(nums)):
        #             if nums[val] not in lst:
        #                 lst.append(nums[val])
        #                 if lst not in ans: ans.append([x for x in lst])
        #             backtrack(i+1,lst,nums,ans)
        #             lst.pop()
        # backtrack(0,[],nums,ans)
        # ans.append([])
        # print(ans)