class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = -1
        for row in accounts:
            if sum(row) > mx:
                mx = sum(row)
        return mx
