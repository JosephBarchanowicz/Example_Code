class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict = {}
        for index, num in enumerate(nums):
            comp = target - num
            print(comp)
            if comp in sum_dict:
                return [sum_dict[comp], index]
            else:
                sum_dict[num] = index
        return  None