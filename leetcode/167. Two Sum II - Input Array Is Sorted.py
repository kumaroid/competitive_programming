class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left_ptr = 0
        right_ptr = n - 1

        while left_ptr <= right_ptr:
            if (numbers[left_ptr] + numbers[right_ptr]) > target:
                right_ptr -= 1
            elif (numbers[left_ptr] + numbers[right_ptr]) < target:
                left_ptr += 1
            else:
                return [left_ptr + 1, right_ptr + 1]
