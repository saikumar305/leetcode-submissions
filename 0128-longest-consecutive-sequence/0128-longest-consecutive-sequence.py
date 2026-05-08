class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_count = 0
        for num in num_set:
            if num-1 not in num_set:
                c = 0
            
                while num+c in num_set:
                    c+=1

                max_count = max(max_count , c)
            
        return max_count

        