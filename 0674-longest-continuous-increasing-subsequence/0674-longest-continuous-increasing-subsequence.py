class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        curr_max_len = 1
        max_len = 1

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                curr_max_len += 1
            else:
                max_len = max(curr_max_len, max_len)
                curr_max_len = 1
        return max(curr_max_len, max_len)
                



        