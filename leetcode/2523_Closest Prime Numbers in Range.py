class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            primes = [True] * (n + 1)
            p = 2
            while p**2 <= n:
                if primes[p]:
                    for i in range(p**2, n + 1, p):
                        primes[i] = False
                p += 1
            prime_numbers = [x for x in range(2, n + 1) if primes[x]]
            return prime_numbers

        prime_numbers = sieve_of_eratosthenes(right)
        prime_numbers = [x for x in prime_numbers if left <= x <= right]

        if len(prime_numbers) < 2:
            return [-1, -1]

        prime_numbers.sort()
        min_diff = float('inf')
        pair1 = None
        pair2 = None

        for i in range(1, len(prime_numbers)):
            diff = prime_numbers[i] - prime_numbers[i-1]
            if diff < min_diff:
                min_diff = diff
                pair1 = prime_numbers[i-1]
                pair2 = prime_numbers[i]

        return [pair1, pair2]
