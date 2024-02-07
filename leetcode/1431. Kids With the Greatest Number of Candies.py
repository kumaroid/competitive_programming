class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        mx = max(candies)
        for x in candies:
            if x + extraCandies >= mx:
                res.append(True)
            else: res.append(False)
        return res
