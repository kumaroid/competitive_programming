from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps_dict = defaultdict(int)
        ps_dict[0] = 1
        prefix_sum = 0
        res = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            key = prefix_sum-k
            if ps_dict[key]:
                res += ps_dict[key]
            ps_dict[prefix_sum] += 1
        return res 
