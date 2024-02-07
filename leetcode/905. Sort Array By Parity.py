class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        list1 = []
        list2 = []
        for num in nums:
            if num % 2 == 0:
                list1.append(num)
            else:
                list2.append(num)
        return (list1 + list2)
