class Solution:
    def intToRoman(self, num: int) -> str:
        coding = zip(
            [1000,900,500,400,100,90,50,40,10,9,5,4,1],
            ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        )
        
        def decToRoman(num):
            result = []
            for d, r in coding:
                while num >= d:
                    result.append(r)
                    num -= d
            return ''.join(result)
        return decToRoman(num)
