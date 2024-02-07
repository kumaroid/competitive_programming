class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        return res
