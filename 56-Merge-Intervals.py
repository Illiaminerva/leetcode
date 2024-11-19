class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key = lambda x: x[0])
        curStart, curEnd = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            if curEnd < interval[0]:
                output.append([curStart, curEnd])
                curStart, curEnd = interval
            else:
                curEnd = max(curEnd, interval[1])
        output.append([curStart, curEnd])
        return output