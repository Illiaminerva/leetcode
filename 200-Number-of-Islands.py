from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == "1":
                visited.add((r,c))
                dfs(r+1, c)
                dfs(r ,c+1)
                dfs(r-1, c)
                dfs(r, c-1)
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r,c)
                    total += 1
        return total

