class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        nums1 = nums[:n]
        nums2 = nums[n:]
        for i in range(len(nums1)):
            res.append(nums1[i])
            res.append(nums2[i])
        return res
