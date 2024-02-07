class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        flat_grid = []
        k = 0
        for row in grid:
            for number in row:
                flat_grid.append(number)
        for x in flat_grid:
            if x < 0:
                k += 1
        return k
