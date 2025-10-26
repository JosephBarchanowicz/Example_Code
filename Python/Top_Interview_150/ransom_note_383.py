class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each character in magazine
        magazine_count = {}
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        # Check if we can construct ransomNote
        for char in ransomNote:
            if magazine_count.get(char, 0) == 0:
                return False
            magazine_count[char] -= 1

        return True

s = Solution()
print(s.canConstruct(ransomNote = "a", magazine = "b"))
print(s.canConstruct(ransomNote = "aa", magazine = "ab"))
print(s.canConstruct(ransomNote = "aa", magazine = "aab"))