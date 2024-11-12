from copy import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        output = []
        prev_comb = self.permute(nums[:-1])
        new_num = nums[-1]
        for comb in prev_comb:
            for i in range(len(nums)-1):
                new_comb = comb[:i] + [new_num] + comb[i:]
                output.append(new_comb)
            output.append(comb + [new_num])
        return output


        

