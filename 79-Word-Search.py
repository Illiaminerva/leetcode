# 1. Find a match when the first letter is the same 
# 2. Search the four dimensions within the boundaries 
    # -> if match: continue 
    # -> if not match: go to different direction

    # -> go through (x,y)+[(1,0), (0,1), (-1,0), (0,-1)]
    # dfs(x, y, i): 
        # if i == len(words): 
            # return True 
        # check if visited? 
            # if yes -> return 
        # check if it is a match for word[i]: 
            # if yes: 
            # put (x,y) into visited 
            # if not
                #add it into visited: {S}
            # recurse(x, y, i+1) within boundaries 
            # free up the specific visited value 
        #return False 


# visited: capture position that we found 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set() #(r,c)
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not 0 <= r < rows or not 0 <= c < cols or (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r,c))
            result = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visited.remove((r,c))
            return result
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False