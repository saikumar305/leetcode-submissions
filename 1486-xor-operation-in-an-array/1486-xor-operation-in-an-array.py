class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*i for i  in range(n)]
        res = 0

        for i in nums:
            res ^=i

        return res
        