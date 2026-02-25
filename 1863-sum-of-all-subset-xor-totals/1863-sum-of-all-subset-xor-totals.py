class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack(index, curr_xor):
            if index == len(nums):
                return curr_xor

            return (backtrack(index+1, curr_xor) + backtrack(index+1 , curr_xor^nums[index]))

        return backtrack(0,0)
        