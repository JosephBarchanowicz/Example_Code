import pytest
from divide_two_integers import Solution

def test_divide():
    instance = Solution()
    assert instance.divide(100, 3) == 33
    assert instance.divide(-100, 3) == -33
    assert instance.divide(100, -3) == -33

"""    
============================= test session starts ==============================
collecting ... collected 1 item

Divide_Two_Integers/divide_two_integers_test.py::test_divide PASSED      [100%]

============================== 1 passed in 0.02s ===============================
""" 