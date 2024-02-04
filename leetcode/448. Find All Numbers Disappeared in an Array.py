class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = []
        num_set = set(nums)
        for i in range(1, n+1):
            if i not in num_set:
                missing.append(i)
        return missing

            
