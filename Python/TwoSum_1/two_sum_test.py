import pytest
from two_sum import Solution

def test_two_sum():
    instance = Solution()
    assert instance.twoSum(nums = [2,7,11,15], target = 9) == [0,1]
    assert instance.twoSum(nums = [3,2,4], target = 6) == [1, 2]
    assert instance.twoSum(nums = [3,3], target = 6) == [0, 1]
    assert instance.twoSum(nums=[], target=6) is None


"""
============================= test session starts ==============================
collecting ... collected 1 item

TwoSum_1/two_sum_test.py::test_two_sum PASSED                            [100%]7
2
3
4
2
3
3


============================== 1 passed in 0.02s ===============================

Process finished with exit code 0
"""
