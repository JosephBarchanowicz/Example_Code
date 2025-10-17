class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ptr_1 = 0
        ptr_2 = len(numbers) - 1

        while ptr_1 < ptr_2:
            res =  numbers[ptr_1] + numbers[ptr_2]
            if res > target:
                ptr_2 -= 1
            elif res < target:
                ptr_1 += 1
            else:
                return [ptr_1 + 1, ptr_2 + 1]
        return [-1, -1]



s = Solution()
print(s.twoSum(numbers = [-1,0], target = -1))