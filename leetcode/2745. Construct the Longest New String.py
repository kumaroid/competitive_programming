class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        xy = 2 * min(x, y) + (x != y)
        return 2 * (xy + z)
