import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append((point[0] ** 2 + point[1] ** 2, point[0], point[1]))
        heapq.heapify(distances)
        res = []
        while k and distances:
            _, x, y = heapq.heappop(distances)
            res.append([x,y])
            k -= 1
        return res