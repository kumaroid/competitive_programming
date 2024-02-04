class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = []
        for num in nums:
            str_num = str(num)
            for char in str_num:
                digits.append(int(char))
        return digits
