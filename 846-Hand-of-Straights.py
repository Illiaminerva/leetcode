from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for num in hand:
            start = num
            while count[start] > 0:
                start -= 1
            while start <= num:
                while count[start] > 0:
                    for i in range(start, start + groupSize):
                        if count[i] == 0:
                            return False
                        count[i] -= 1
                start += 1
        return True