class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        minRemove = 0
        curEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= curEnd:
                curEnd = end
            else:
                minRemove += 1
                curEnd = min(end, curEnd)
        return minRemove