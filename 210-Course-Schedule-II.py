from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        adjList = defaultdict(list)
        output = []
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output



        

            
            


