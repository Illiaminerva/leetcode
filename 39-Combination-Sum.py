class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = []
        def dfs(i, curSum):
            if curSum == target:
                result.append(subset.copy())
                return
            if i == len(candidates):
                return
            if curSum + candidates[i] <= target:
                subset.append(candidates[i])
                dfs(i, curSum + candidates[i])
                subset.pop()
            dfs(i+1, curSum)
        dfs(0, 0)
        return result

                

