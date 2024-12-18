class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = 0
        cur_penalty = 0
        min_index = len(customers)
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == "Y":
                cur_penalty += 1
            else:
                cur_penalty -= 1
            if cur_penalty <= min_penalty:
                min_index = i
                min_penalty = cur_penalty
        return min_index
