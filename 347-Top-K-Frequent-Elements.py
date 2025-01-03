class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        i = len(nums) - 1
        while len(res) < k:
            res += freq[i]
            i -= 1
        return res