class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        cycle, visit = set(), set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit: 
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output

        