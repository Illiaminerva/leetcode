class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum = float("inf")
        secondNum = float("inf")
        for n in nums:
            if n < firstNum:
                firstNum = n
            if n > firstNum and n < secondNum:
                secondNum = n
            if n > secondNum:
                return True
        return False