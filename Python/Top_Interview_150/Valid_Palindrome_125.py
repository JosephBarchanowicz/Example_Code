class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_start = 0
        pointer_end = (len(s) - 1)
        while pointer_start <= pointer_end:
            while pointer_start < pointer_end and not s[pointer_start].isalnum():
                pointer_start += 1
            while pointer_end > pointer_start and not s[pointer_end].isalnum():
                pointer_end -=1
            if s[pointer_start].lower() != s[pointer_end].lower():
                return False
            pointer_start += 1
            pointer_end -= 1
        return True

s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(s.isPalindrome(s = "race a car"))
print(s.isPalindrome(s = "0P"))
