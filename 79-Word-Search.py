class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        index_set = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or (i, j) in index_set or board[i][j] != word[k]:
                return False
            index_set.add((i,j))
            result = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            index_set.remove((i,j))
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False