class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums = sorted(nums3)
        mid = len(nums)//2
        if len(nums)%2 == 1:
            return nums[mid]
        if len(nums)%2 == 0:
            return ((nums[mid]+nums[mid-1])/2)
