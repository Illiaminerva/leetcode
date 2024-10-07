class Solution:
    def countSubstrings(self, s: str) -> int:
        num_pal = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                num_pal += 1
                l, r = l-1, r+1
        for i in range(len(s)-1):
            l, r = i, i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                num_pal += 1
                l, r = l-1, r+1      
        return num_pal     