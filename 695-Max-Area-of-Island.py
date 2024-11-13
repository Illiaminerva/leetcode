class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == 1:
                visited.add((r,c))
                return 1 + dfs(r,c+1) + dfs(r, c-1) + dfs(r-1, c) + dfs(r+1,c)
            return 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea

            
            
                

