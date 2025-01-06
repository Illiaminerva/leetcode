class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            ch = chars[i]
            j = i + 1
            while j < len(chars) and chars[j] == ch:
                j += 1
            num = j - i
            chars[res] = ch
            res += 1
            numLen = len(str(num))
            if num > 1:
                chars[res:res+numLen] = list(str(num))
                res += numLen
            i = j
        return res
            