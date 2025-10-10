class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = {}
        for num in nums:
            if num not in element:
                element[num] = 1
            else:
                element[num] += 1
        max_key = max(element, key=element.get)
        return max_key


s = Solution()
print(s.majorityElement([3,2,3]))