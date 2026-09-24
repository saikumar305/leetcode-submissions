class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0

        for num in nums:
            if num != val:
                nums[j] = num
                j+=1

        return j
            

            
        