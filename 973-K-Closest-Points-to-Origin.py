import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(x**2 + y**2, x, y) for x, y in points]
        heapq.heapify(minHeap)
        output = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            output.append([x,y])
        return output