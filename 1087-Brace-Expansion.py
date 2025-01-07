class Solution:
    def expand(self, s: str) -> List[str]:
        answer = []
        def dfs(i, word):
            if i == len(s):
                answer.append(word)
                return
            if s[i] != "{":
                dfs(i+1, word + s[i])
            else:
                i += 1
                posChars = [s[i]]
                while s[i+1] == ",":
                    posChars.append(s[i+2])
                    i += 2
                posChars.sort()
                for ch in posChars:
                    dfs(i+2, word + ch)
        dfs(0, "")
        return answer



        