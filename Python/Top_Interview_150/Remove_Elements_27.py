class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        arr_len = len(nums) - 1

        while pointer <= arr_len:
            if nums[pointer] == val:
                nums.pop(pointer)
                arr_len -= 1
            else:
                pointer += 1
        return len(nums)


s = Solution()
print(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
