class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n in (0,1):
                return 1
            return n * fact(n-1)

        num = fact(n)
        count = 0
        while num % 10 == 0:
            count += 1
            num = num // 10
        return count
    
