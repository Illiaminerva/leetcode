class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_pre = defaultdict(list)
        for a, b in prerequisites:
            course_pre[b].append(a)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if course_pre[crs] == []:
                return True
            visiting.add(crs)
            for prereq in course_pre[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            course_pre[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        