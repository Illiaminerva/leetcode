import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone2 > stone1:
                heapq.heappush(stones, stone1 - stone2)
        return 0 if not stones else -stones[0]
            