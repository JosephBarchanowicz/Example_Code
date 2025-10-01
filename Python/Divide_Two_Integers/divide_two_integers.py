"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
[−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the
quotient is strictly less than -231, then return -231.

"""

# Python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle division by zero
        if divisor == 0:
            raise ZeroDivisionError("division by zero")

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        a = -dividend if dividend < 0 else dividend
        b = -divisor if divisor < 0 else divisor

        # Build doubles of divisor and powers of two
        doubles = []
        powers = []
        power = 1
        current = b
        while current <= a:
            doubles.append(current)
            powers.append(power)
            current += current
            power += power

        # Greedy subtraction from largest double
        result = 0
        for i in range(len(doubles) - 1, -1, -1):
            if doubles[i] <= a:
                a -= doubles[i]
                result += powers[i]

        # Restore sign
        if negative:
            result = -result

        # Clamp (usually only needed for the special case already handled)
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result


