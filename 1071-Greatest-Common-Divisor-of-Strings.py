class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def valid(k):
            if len(str1) % k or len(str2) % k:
                return False
            for i in range(len(str1)//k):
                if str1[i*k:i*k+k] != str2[:k]:
                    return False
            for i in range(len(str2)//k):
                if str2[i*k:i*k+k] != str1[:k]:
                    return False     
            return True
        for k in range(min(len(str1), len(str2)), 0, -1):
            if valid(k):
                return str1[:k]
        return ""       