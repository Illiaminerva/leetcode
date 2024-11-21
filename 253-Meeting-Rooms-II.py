import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for interval in intervals:
            time.append((interval[0], 1))
            time.append((interval[1], -1))
        cur_rooms = 0
        max_rooms = 0
        time.sort()
        for _, room in time:
            cur_rooms += room
            max_rooms = max(max_rooms, cur_rooms)
        return max_rooms 
