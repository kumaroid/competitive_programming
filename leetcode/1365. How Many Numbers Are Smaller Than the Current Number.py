class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            k = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    k+=1
            res.append(k)
        return res
