class Solution:
    def isHappy(self, n: int) -> bool:
        unhappy_set = set()
        while n not in unhappy_set and n != 1:
            unhappy_set.add(n)
            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n = n//10
            n = new_n
        return True if n == 1 else False