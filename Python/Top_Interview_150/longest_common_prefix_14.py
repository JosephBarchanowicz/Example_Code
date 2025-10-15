class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(x) for x in strs)
        start = 1
        end = min_len
        while start <= end:
            mid = (start + end) // 2
            if self.common_prefix(strs, mid):
                start = mid + 1
            else:
                end = mid - 1
        return strs[0][: (start + end) // 2]

    def common_prefix(self, strs, x):
        str1 = strs[0][:x]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True