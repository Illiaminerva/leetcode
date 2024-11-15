from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])
        for j in range(cols):
            if board[0][j] == "O":
                q.append((0,j))
            if board[rows-1][j] == "O":
                q.append((rows-1,j))
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i,0))
            if board[i][cols-1] == "O":
                q.append((i,cols-1))
        visited = set(q)      
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                if (x+dx,y+dy) not in visited and 0 <= x+dx < rows and 0<= y+dy < cols and board[x+dx][y+dy] == "O":
                    q.append((x+dx,y+dy))
                    visited.add((x+dx,y+dy))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    board[r][c] = "X"
           

        