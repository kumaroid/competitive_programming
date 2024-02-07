class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = 0
        if target not in nums:
            return -1 
        for i in range(len(nums)):
            if nums[i] == target:
                return i
