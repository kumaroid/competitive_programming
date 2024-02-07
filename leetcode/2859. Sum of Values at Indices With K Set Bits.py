class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            tmp = bin(i)
            if tmp.count('1') == k:
                res += nums[i]
        return res
