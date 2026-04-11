class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = 0
        if k ==1:
            return nums[-1]

        for i in range(k):
            max_sum += nums[-1]
            val = nums.pop()
            nums.append(val+1)

        return max_sum
            
        