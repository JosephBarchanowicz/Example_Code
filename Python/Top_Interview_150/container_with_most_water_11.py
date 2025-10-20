class Solution:
    def maxArea(self, height: list[int]) -> int:
        str_ptr = 0
        end_ptr = len(height) - 1
        max_ar = -1

        while str_ptr <= end_ptr:
            length = end_ptr - str_ptr
            height_var = min(height[str_ptr], height[end_ptr])
            area =  height_var * length
            if area > max_ar:
                max_ar = area
            if height[str_ptr] > height[end_ptr]:
                end_ptr -= 1
            else:
                str_ptr += 1
        return max_ar


s = Solution()
print(s.maxArea(height=[1,8,6,2,5,4,8,3,7]))