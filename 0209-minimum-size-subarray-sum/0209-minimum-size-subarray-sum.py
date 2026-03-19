class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        
        min_len = float('inf')
        l = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                
                min_len = min(min_len, i-l+ 1)
                
                curr_sum -= nums[l]
                l+=1

        return min_len if min_len != float("inf") else 0
            
        return min_len

        

        