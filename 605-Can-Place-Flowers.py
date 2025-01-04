class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        extra = 0
        if len(flowerbed) == 1:
            return n == 0 or (n == 1 and flowerbed[0] == 0)
        if flowerbed[0] == 0:
            if flowerbed[1] == 0:
                flowerbed[0] = 1
                extra += 1
        if flowerbed[-1] == 0:
            if flowerbed[-2] == 0:
                flowerbed[-1] = 1
                extra += 1
        for i in range(1, len(flowerbed)-1):
            if not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]:
                flowerbed[i] = 1
                extra += 1
        return extra >= n                 