class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for i in nums:
            if i in numMap:
                return True
            else: numMap[i] = 1
        return False

        