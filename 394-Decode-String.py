class Solution:
    def decodeString(self, s):
        if len(s) == 0:
            return \\
        if s[0] not in \123456789\:
            return s[0] + self.decodeString(s[1:])
        i = 0
        while i < len(s) and s[i] in \0123456789\:
            i += 1
        #i at this moment is the location of first left bracket
        left, right = 1, 0
        start_sub = i + 1
        while left != right:
            i += 1
            if s[i] == \[\:
                left += 1
            elif s[i] == \]\:
                right += 1
        return int(s[:start_sub-1]) * self.decodeString(s[start_sub:i]) + self.decodeString(s[i+1:])
        