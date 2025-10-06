# Tested with O(N) Time Complexity
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer_start = 0
        pointer_check = 1
        k = 1

        while pointer_check < len(nums):
            if nums[pointer_start] != nums[pointer_check]:
                pointer_start += 1
                nums[pointer_start] = nums[pointer_check]
                pointer_check += 1
                k += 1
            else:
                pointer_check += 1
        return k


s = Solution()
print(s.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))
