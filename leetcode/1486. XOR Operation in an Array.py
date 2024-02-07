class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        s = 0
        for x in nums:
            s ^= x
        return s
