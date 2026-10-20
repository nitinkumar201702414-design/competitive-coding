class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Only overflow case: -2^31 / -1 = 2^31, which doesn't fit in 32 bits
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Result is negative if exactly one input is negative
        negative = (dividend < 0) != (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        result = 0

        # Binary long division: try the largest shifts first
        for i in range(31, -1, -1):
            if (a >> i) >= b:
                a -= (b << i)
                result += (1 << i)

        return -result if negative else result