class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(n):
            if n<2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True

        def isPal(n):
            s = str(n)
            if s == s[::-1]:
                return True
            return False

        while True:
            if isPrime(n) and isPal(n):
                return n
            n+=1
            if n > 10**7 and n < 10**8:
                n = 10**8
                        
