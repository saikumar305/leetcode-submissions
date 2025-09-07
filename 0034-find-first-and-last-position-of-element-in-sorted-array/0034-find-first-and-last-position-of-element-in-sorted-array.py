class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        first = self.first(nums, target)
        if first == -1 or nums[first] != target:
            return [-1, -1]

        second = self.second(nums, target, first)
        
        return [first, second-1]

    def first(self, nums, target):
        h, l = len(nums)-1 , 0
        first =0
        while l <= h:
            mid = (l+h) // 2
            if nums[mid] >= target:
                first = mid
                h = mid-1
            else:
                l = mid+1
        return first

       

    def second(self, nums, target, first):
        h, l = len(nums)-1 , 0
        last = len(nums)
        while l <= h:
            mid = (l+h) // 2
            if nums[mid] > target:
                last = mid
                h = mid-1
            else:
                l = mid +1

        return last
    
        