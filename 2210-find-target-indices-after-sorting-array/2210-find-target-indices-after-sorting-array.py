class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        op = []

        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                op.append(i)

        return op
        