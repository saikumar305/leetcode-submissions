class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drop = 0
        
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                drop +=1
        if nums[0] < nums[n -1] :
            drop +=1
        print(drop)
        return drop <=1


        