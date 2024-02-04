class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        k = 0
        for i in range(len(heights)):
            if exp[i] != heights[i]:
                k += 1
        return k
