class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _sum , prod = 0 , 1
        for i in str(n):
            i = int(i)

            _sum += i
            prod *= i

        return prod - _sum

        