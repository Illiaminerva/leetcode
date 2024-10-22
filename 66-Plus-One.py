class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if sum(digits) == len(digits) * 9:
            return [1] + [0] * len(digits)
        elif digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            i = len(digits) - 1
            while digits[i] == 9:
                i -= 1
            digits[i] += 1
            i += 1
            while i < len(digits):
                digits[i] = 0
                i += 1
            return digits