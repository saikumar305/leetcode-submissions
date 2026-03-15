class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left , right = 0, n - 1
        res = [0] * n

        for i in range(len(nums) -1 , -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left +=1
            else:
                res[i] = nums[right] ** 2
                right -=1

        return res

        




        