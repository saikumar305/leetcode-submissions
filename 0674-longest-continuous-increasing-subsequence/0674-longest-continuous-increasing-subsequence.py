class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr_max_len = 1
        prev_max_len = 1
        max_len = 1

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                print(max_len)
                curr_max_len += 1
            else:
                prev_max_len = curr_max_len
                curr_max_len = 1
                max_len = max(prev_max_len, max_len)
        print(prev_max_len, curr_max_len)
        return max(curr_max_len, max_len)
                



        