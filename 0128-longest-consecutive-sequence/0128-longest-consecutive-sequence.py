class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_len = 1

                while current_num+1 in num_set:
                    current_len+=1
                    current_num+=1

                max_len = max(current_len, max_len)
        
        return max_len
