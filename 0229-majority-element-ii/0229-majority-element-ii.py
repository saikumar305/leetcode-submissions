class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        op = []
        for k,v in hashmap.items():
            if v > len(nums)//3:
                op.append(k)
            
        return op

        