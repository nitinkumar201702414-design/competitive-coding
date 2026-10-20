class Solution:
    def trailingZeroes(self, n: int) -> int:
        j = 0
        a = 5
        while n // a > 0:
            j = j + (n//a)
            a = a*5

        return j

        