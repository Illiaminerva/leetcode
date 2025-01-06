# 1. Find the occurance 
# 2. iterate through the values and see if there is repeition (through set)
from collections import Counter 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurences = list(counts.values())
        return len(occurences) == len(set(occurences))
            
      