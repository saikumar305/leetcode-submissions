class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        min_len = float("inf")
        left = 0

        for right in range(len(nums)):
            print(curr_sum, right)
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right-left +1)
                curr_sum -= nums[left]
                left +=1
                

        return 0 if min_len == float("inf") else min_len
            

        