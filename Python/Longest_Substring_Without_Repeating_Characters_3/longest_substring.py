from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_counter = Counter()
        left = right = 0
        value = 0
        while right < len(s):
            r = s[right]
            c_counter[r] += 1
            while c_counter[r] > 1:
                l = s[left]
                c_counter[l] -= 1
                left += 1
            value = max(value, right - left + 1)
            right += 1
        return value

s=Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
