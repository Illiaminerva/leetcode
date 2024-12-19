from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)
        for f, t, a in transactions:
            balance[f] -= a
            balance[t] += a
        netBal = [value for value in balance.values() if value]
        def dfs(i):
            while i < len(netBal) and netBal[i] == 0:
                i += 1
            if i == len(netBal):
                return 0
            minTran = len(netBal)
            for nxt in range(i+1, len(netBal)):
                if netBal[i] * netBal[nxt] < 0:
                    netBal[nxt] += netBal[i]
                    minTran = min(minTran, 1 + dfs(i+1))
                    netBal[nxt] -= netBal[i]
            return minTran
        return dfs(0)



