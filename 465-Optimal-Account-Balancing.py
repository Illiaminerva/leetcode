from collections import defaultdict
import heapq
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)
        for f, t, a in transactions:
            balance[f] -= a
            balance[t] += a
        balance_list = [amount for amount in balance.values() if amount]
        n = len(balance_list)
        def dfs(cur):
            while cur < n and not balance_list[cur]:
                cur += 1
            if cur == n:
                return 0
            cost = n 
            for nxt in range(cur + 1, len(balance_list)):
                if balance_list[nxt] * balance_list[cur] < 0:
                    balance_list[nxt] += balance_list[cur]
                    cost = min(cost, 1 + dfs(cur+1))
                    balance_list[nxt] -= balance_list[cur]
            return cost
        return dfs(0)



