class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur_profit = 0
        max_turns = 0
        max_profit = 0
        cur_waiting = 0
        for i in range(len(customers)):
            cur_waiting += customers[i]
            if cur_waiting >= 4:
                cur_waiting -= 4
                cur_profit += 4 * boardingCost
                cur_profit -= runningCost
            else:
                cur_profit += cur_waiting * boardingCost
                cur_profit -= runningCost        
                cur_waiting = 0
            if cur_profit > max_profit:
                max_profit = cur_profit
                max_turns = i + 1
        serveAllProfit = cur_profit + cur_waiting * boardingCost - ((cur_waiting - 1) // 4 + 1) * runningCost
        serveWithoutLast = cur_profit + (cur_waiting - cur_waiting % 4) * boardingCost - (cur_waiting // 4) * runningCost
        print(cur_profit)
        if max_profit >= max(max_profit, serveAllProfit, serveWithoutLast, 1):
            return max_turns
        if serveWithoutLast >= max(max_profit, serveAllProfit, serveWithoutLast, 1):
            return len(customers) + cur_waiting // 4   
        if serveAllProfit >= max(max_profit, serveAllProfit, serveWithoutLast, 1):
            return len(customers) + ((cur_waiting - 1) // 4 + 1) 
        return -1
        