class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        s = words
        s = [i for i in s if i]
        return " ".join(s[::-1])
        