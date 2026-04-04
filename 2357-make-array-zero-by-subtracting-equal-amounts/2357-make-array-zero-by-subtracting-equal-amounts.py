class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0

        while any(nums):
            x = min(n for n in nums if n>0)
            for i,num in enumerate(nums):
                if num> 0:
                    nums[i] -= x

            c+=1

            
        return c

    
        