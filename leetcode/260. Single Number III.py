class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        str(nums)
        res = []
        for x in nums:
            if nums.count(x) == 1:
                res.append(x)

        return res
