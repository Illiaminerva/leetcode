class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()
        def backtrack(i, curSum):
            if curSum == target:
                ans.append(subset.copy())
                return
            if i >= len(candidates):
                return
            if curSum + candidates[i] <= target:
                subset.append(candidates[i])
                backtrack(i+1, curSum + candidates[i])
                subset.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            backtrack(i+1, curSum)
        backtrack(0, 0)
        return ans
