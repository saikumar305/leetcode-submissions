class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        numsMap = {}

        for i in nums:
            
            if i in numsMap and numsMap[i] >= 2:
                return False
            
            numsMap[i] = numsMap.get(i,0) +1
            print(i, "->" ,numsMap[i])

        print(numsMap)

        return True