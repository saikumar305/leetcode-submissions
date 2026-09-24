class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        l, h = 0 ,  len(nums)-1

        while l <= h:
            mid = (l+h) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else :
                h = mid-1
            
        return l



        