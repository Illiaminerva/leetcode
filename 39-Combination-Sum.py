class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(i, cur_sum):
            if i >= len(candidates):
                return
            if cur_sum == target:
                result.append(subset.copy())
                return
            if cur_sum > target:
                return
            subset.append(candidates[i])
            backtrack(i, cur_sum + candidates[i])
            subset.pop()
            backtrack(i + 1, cur_sum)
        backtrack(0, 0)
        return result

                

