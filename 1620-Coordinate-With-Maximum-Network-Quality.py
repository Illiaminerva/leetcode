class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = float("-inf")
        max_point = None
        for x in range(0, 51):
            for y in range(0, 51):
                cur_quality = 0
                for x_t, y_t, q in towers:
                    d = ((x_t - x) ** 2 + (y_t - y) ** 2) ** 0.5
                    if d <= radius:
                        cur_quality += floor(q / (1 + d))
                if cur_quality > max_quality:
                    max_quality = cur_quality 
                    max_point = [x, y]
        return max_point