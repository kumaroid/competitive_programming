class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged_list = list(itertools.chain(*matrix))
        if target in merged_list:
            return True
        return False
