from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.pointMap = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointMap[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for x, y in list(self.pointMap.keys()):
            if abs(x-point[0]) != abs(y-point[1]) or x == point[0] or y == point[1]:
                continue
            res += self.pointMap[(x,y)] * self.pointMap[(x,point[1])] * self.pointMap[(point[0], y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)