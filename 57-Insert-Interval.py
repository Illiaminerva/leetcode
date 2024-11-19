class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                output.append(interval)
            elif newInterval[1] < interval[0]:
                return output + [newInterval] + intervals[i:]
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        return output + [newInterval]