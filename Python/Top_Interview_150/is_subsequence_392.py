class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s, ptr_t  = 0, 0
        while ptr_t <= len(t) - 1:
            if t[ptr_t] == s[ptr_s]:
                ptr_s += 1
            if ptr_s >= len(s):
                return True
            ptr_t += 1
        return False

s = Solution()
print(s.isSubsequence(s="abc", t="ahbgdc"))
print(s.isSubsequence(s="axc", t="ahbgdc"))