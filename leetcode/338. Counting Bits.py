class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            tmp = str(bin(i)[2:])
            res.append(tmp.count('1'))
        return res
