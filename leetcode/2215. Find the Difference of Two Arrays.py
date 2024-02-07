class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m,n = set(nums1),set(nums2)
        return [list(m-n), list(n-m)]
