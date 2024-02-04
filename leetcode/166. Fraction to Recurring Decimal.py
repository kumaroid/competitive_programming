import re
class Solution:
    def fractionToDecimal(self,numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator // denominator)

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)

        res.append(".")

        hashmap = {}
        while remainder != 0:
            if remainder in hashmap:
                res.insert(hashmap[remainder], "(")
                res.append(")")
                break

            hashmap[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)

        
