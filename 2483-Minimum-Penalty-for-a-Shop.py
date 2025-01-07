class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curProfit = 0
        maxClos = 0
        maxProfit = 0
        for i, customer in enumerate(customers):
            if customer == "Y":
                curProfit += 1
                if curProfit > maxProfit:
                    maxClos = i + 1
                    maxProfit = curProfit
            else:
                curProfit -= 1
        return maxClos
