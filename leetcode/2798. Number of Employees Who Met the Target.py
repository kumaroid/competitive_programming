class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        k = 0
        for x in hours:
            if x >= target:
                k += 1
        return k
