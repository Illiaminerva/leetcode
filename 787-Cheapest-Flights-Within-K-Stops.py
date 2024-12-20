from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightDict = defaultdict(list)
        for f, t, price in flights:
            flightDict[f].append((t, price))
        visited = [float('inf')] * n
        visited[src] = 0
        queue = deque([(src, 0)])
        for i in range(k+1):
            curLen = len(queue)
            for j in range(curLen):
                city, curPrice = queue.popleft()
                for dest, price in flightDict[city]:
                    if curPrice + price < visited[dest]:
                        visited[dest] = curPrice + price
                        queue.append((dest, curPrice + price))
        return visited[dst] if visited[dst] < float("+inf") else -1




        
        