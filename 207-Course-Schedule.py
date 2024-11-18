from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            visited.add(crs)
            for dep in adjList[crs]:
                if not dfs(dep):
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True
        for crs, dep in prerequisites:
            adjList[crs].append(dep)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                