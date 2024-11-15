from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_list = defaultdict(list)
        for crs, pre in prerequisites:
            dep_list[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            visited.add(crs)
            for pre in dep_list[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            dep_list[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



