from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = 0
        healthy = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    healthy += 1
        while healthy and q:
            time += 1
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x+dx][y+dy] == 1:
                        healthy -= 1
                        grid[x+dx][y+dy] = 2
                        q.append((x+dx, y+dy))
        return -1 if healthy else time
        