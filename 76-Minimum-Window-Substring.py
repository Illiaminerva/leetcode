from collectins import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return \\
        res = [1, 1]
        resLen = float(\+inf\)
        l = 0
        count_s, count_t = defaultdict(int), defaultdict(int)
        