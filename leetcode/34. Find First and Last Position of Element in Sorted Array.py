class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        lst = []
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                lst.append(i)
        res.append(min(lst))
        res.append(max(lst))
        return res
