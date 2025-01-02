class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        numsMap = {}

        for i in nums:
            numsMap[i] = numsMap.get(i,0) +1
        
        for k, v in numsMap.items():
            if v > 2:
                return False

        return True