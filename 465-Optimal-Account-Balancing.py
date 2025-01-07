from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanceDict = defaultdict(int)
        for f, t, a in transactions:
            balanceDict[f] += a
            balanceDict[t] -= a
        balances = [value for value in balanceDict.values() if value]
        def dfs(i):
            while i < len(balances) and balances[i] == 0:
                i += 1
            if i == len(balances):
                return 0
            curBalance = balances[i]
            minTran = len(balances)
            for j in range(i+1, len(balances)):
                if balances[j] * curBalance < 0:
                    balances[j] += curBalance
                    minTran = min(minTran, 1 + dfs(i+1))
                    balances[j] -= curBalance
            return minTran
        return dfs(0)
            



