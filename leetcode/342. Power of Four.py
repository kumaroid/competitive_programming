class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        pow = [1,4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        if n in pow:
            return True
        return False
#brut force
