class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedStr = ""
        for i in range(min(len(word1), len(word2))):
            mergedStr += word1[i]
            mergedStr += word2[i]
        if len(word1) > len(word2):
            mergedStr += word1[len(word2):]
        if len(word2) > len(word1):
            mergedStr += word2[len(word1):]
        return mergedStr

        

            


