class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_ = float("inf")
        for n in nums:
            min_ = min(abs(n) ,  min_)
        return min_ if min_ in nums else -min_


        