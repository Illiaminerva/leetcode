from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
        comp = 0
        for i in range(n):
            if i not in visited:
                comp += 1
                dfs(i)
        return comp


        