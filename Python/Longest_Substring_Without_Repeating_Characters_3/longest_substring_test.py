import pytest
from longest_substring import Solution

def test_longest_substring():
    instance = Solution()
    assert instance.lengthOfLongestSubstring("abcabcbb") == 3
    assert instance.lengthOfLongestSubstring("bbbbb") == 1
    assert instance.lengthOfLongestSubstring("pwwkew") == 3

"""
============================= test session starts ==============================
collecting ... collected 1 item

Longest_Substring_Without_Repeating_Characters_3/longest_substring_test.py::test_longest_substring PASSED [100%]

============================== 1 passed in 0.01s ===============================

Process finished with exit code 0
"""
