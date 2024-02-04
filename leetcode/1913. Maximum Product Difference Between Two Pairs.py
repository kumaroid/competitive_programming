class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mn1 = min(nums)
        mx1 = max(nums)
        nums.remove(mn1)
        nums.remove(mx1)
        mn2 = min(nums)
        mx2 = max(nums)
        return (mx1 * mx2) - (mn1 * mn2)
