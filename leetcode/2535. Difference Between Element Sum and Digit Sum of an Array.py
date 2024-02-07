class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        sd = 0
        for x in nums:
            while x:
                sd += x%10
                x //= 10
        return abs(s - sd)
