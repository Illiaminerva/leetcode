from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter1, counter2 = Counter(word1), Counter(word2)
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        return Counter(counter1.values()) == Counter(counter2.values())
