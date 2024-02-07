class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        btoi = int("".join(list(map(str,b))))
        return pow(a,btoi,1337)
