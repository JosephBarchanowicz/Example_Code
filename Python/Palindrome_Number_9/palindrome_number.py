class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        pal_num = 0
        if num < 0:
            return False
        while num != 0:
            pal_num = (pal_num * 10 ) + num % 10
            num //= 10
        return True if pal_num == x else False



