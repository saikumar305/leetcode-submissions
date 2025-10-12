class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        ans, c = 2, 2
        for i in range(2, n):
            if nums[i] == nums[i-1] + nums[i-2]:
                c += 1
            else:
                c = 2
            ans = max(ans, c)
        return ans


            
            
        