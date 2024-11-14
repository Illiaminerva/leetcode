from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        distance = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        empty = 0
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
                elif rooms[i][j] > 0:
                    empty += 1
        while empty and q:
            distance += 1
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(rooms) and 0 <= new_y < len(rooms[0]) and rooms[new_x][new_y] == 2 ** 31 - 1:
                        rooms[new_x][new_y] = distance
                        empty -= 1
                        q.append((new_x, new_y))
                             
        
        
                
        


        


