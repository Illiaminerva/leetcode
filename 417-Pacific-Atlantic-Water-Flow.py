from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pac_q = deque()
        atl_q = deque()
        pac_set = set()
        atl_set = set()
        for j in range(cols):
            pac_q.append((0, j))
            pac_set.add((0, j))
        for i in range(rows):
            pac_q.append((i, 0))
            pac_set.add((i, 0))
        for j in range(cols):
            atl_q.append((rows - 1, j))
            atl_set.add((rows - 1, j))
        for i in range(rows):
            atl_q.append((i, cols - 1))
            atl_set.add((i, cols - 1))
        while pac_q:
            x, y = pac_q.popleft()
            for dx, dy in dirs:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and heights[x+dx][y+dy] >= heights[x][y] and (x+dx, y+dy) not in pac_set:
                    pac_set.add((x+dx, y+dy))
                    pac_q.append((x+dx, y+dy))
        while atl_q:
            x, y = atl_q.popleft()
            for dx, dy in dirs:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and heights[x+dx][y+dy] >= heights[x][y] and (x+dx, y+dy) not in atl_set:
                    atl_set.add((x+dx, y+dy))
                    atl_q.append((x+dx, y+dy)) 
        answer = []
        for x, y in pac_set:
            if (x, y) in atl_set:
                answer.append([x, y])
        return answer       
                
                
                
        

                