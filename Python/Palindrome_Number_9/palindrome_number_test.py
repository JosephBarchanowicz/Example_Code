import pytest
from palindrome_number import Solution

def test_palidrome_number():
    instance = Solution()
    assert instance.isPalindrome(12321) == True
    assert instance.isPalindrome(1221) == True
    assert instance.isPalindrome(1231) == False
    assert instance.isPalindrome(2321) == False
    assert instance.isPalindrome(-12321) == False

"""
============================= test session starts ==============================
collecting ... collected 1 item

Palindrome_Number_9/palindrome_number_test.py::test_palidrome_number PASSED [100%]

============================== 1 passed in 0.02s ===============================

Process finished with exit code 0

"""