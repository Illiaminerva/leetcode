from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjList = defaultdict(list)

        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjList[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            return True
        return dfs(0, -1) and len(visited) == n