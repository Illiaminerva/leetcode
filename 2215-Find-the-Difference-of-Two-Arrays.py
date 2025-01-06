class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        only1 = []
        only2 = []
        for num in set1:
            if num not in set2:
                only1.append(num)
        for num in set2:
            if num not in set1:
                only2.append(num)
        return [only1, only2]

        
        

        