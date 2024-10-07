class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        min_costs = [cost[-2], cost[-1]]
        for i in range(len(cost)-3, -1, -1):
            min_costs = [cost[i] + min(min_costs), min_costs[0]]
        return min(min_costs)