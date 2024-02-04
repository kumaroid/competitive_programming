import sys
class Solution:
    sys.set_int_max_str_digits(10000)
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = ''
        for n in num:
            a += str(n)

        number = int(a) + k

        res = []

        while number:
            res.append(number%10)
            number //=10

        return reversed(res)
