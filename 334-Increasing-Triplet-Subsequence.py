class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum = float("+inf")
        secondNum = float("+inf")
        for num in nums:
            if num < firstNum:
                firstNum = num
            if num > firstNum and num < secondNum:
                secondNum = num
            if num > secondNum:
                return True
        return False
