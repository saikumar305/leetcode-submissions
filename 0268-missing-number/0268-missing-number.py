class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        n_sum = (n *(n+1) )// 2
        print(num_sum, n_sum)

        return n_sum - num_sum