class Solution:
    def expand(self, s: str) -> List[str]:
        answer = []
        def dfs(output, i):
            if i == len(s):
                answer.append(output)
                return
            if s[i] == "{":
                i += 1
                charSet = set()
                while s[i+1] == ",":
                    charSet.add(s[i])
                    i += 2
                charSet.add(s[i])
                charSet = sorted(charSet)
                for char in charSet:
                    dfs(output + char, i + 2)
            else:
                dfs(output + s[i], i + 1)
        dfs("", 0)
        return answer



        