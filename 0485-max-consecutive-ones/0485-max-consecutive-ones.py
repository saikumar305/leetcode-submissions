class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        max_ = 0
        curr = 0
        for num in nums:
            
            if num:
                curr+=1
            else:
                curr=0

            max_ = max(curr,max_)

        return max_
        