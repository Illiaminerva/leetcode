from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightDict = defaultdict(list)
        for f, t, p in flights:
            flightDict[f].append((t, p))
        visit_cost = [float("+inf")] * n
        visit_cost[src] = 0
        queue = deque([(src, 0)])
        for i in range(k+1):
            curLen = len(queue)
            for _ in range(curLen):
                node, price = queue.popleft()
                for flightDest, extra in flightDict[node]:
                    if price + extra < visit_cost[flightDest]:
                        visit_cost[flightDest] = price + extra
                        queue.append((flightDest, price + extra))
            print(queue)
        return visit_cost[dst] if visit_cost[dst] < float("+inf") else -1




        
        