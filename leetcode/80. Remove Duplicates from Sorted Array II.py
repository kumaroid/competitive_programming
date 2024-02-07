class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = 0
        for i in range(0, len(nums) - 2):
            if nums[i + 1] < nums[i]:
                break
            elif nums[i + 1] == nums[i]:
                count = 1
                x = i + 2
                while nums[x] == nums[i]:
                    nums.remove(nums[x])
                    nums.append(-1111)
            else:
                continue
        for i in nums:
            if i != -1111:
                d += 1
        return d
                
