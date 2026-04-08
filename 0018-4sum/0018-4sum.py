# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         # op = set()
#         # for i in range(len(nums)):
#         #     for j in range(i+1,len(nums)):
#         #         for k in range(j+1,len(nums)):
#         #             for l in range(k+1,len(nums)):
#         #                 if nums[i] + nums[j] +nums[k] + nums[l] == target:
#         #                     op.add(tuple(sorted([nums[i] , nums[j] , nums[k], nums[l]])))

#         # return sorted([list(q) for q in op])
#         op = []
#         n= len(nums)
#         nums.sort()
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue  

#             for j in range(i + 1, n):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue

#                 left = j+1
#                 right = n-1

#                 while left< right:
#                     total = nums[i] + nums[j] +nums[left] + nums[right]

#                     if total < target:
#                         left +=1
#                     elif total > target:
#                         right -=1
#                     else:
#                         op.append([nums[i] , nums[j] ,nums[left] , nums[right]])

#                         left += 1
#                         right -= 1

#                         while left < right and nums[left] == nums[left - 1]:
#                             left += 1

#                         while left < right and nums[right] == nums[right + 1]:
#                             right -= 1

#         return op


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int , start) -> List[List[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            if len(nums) - start < k:
                return []

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if nums[start] * k > target or nums[-1]*k <  target:
                return res

            if k == 2:
                return twoSum(nums, target, start)

            for i in range(start, len(nums)):
                if i == start or nums[i - 1] != nums[i]:
                    for subset in kSum(nums, target - nums[i], k - 1, i+1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int, start) -> List[List[int]]:
            res = []
            lo, hi = start, len(nums) - 1

            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > start and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (
                    hi < len(nums) - 1 and nums[hi] == nums[hi + 1]
                ):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()
        return kSum(nums, target, 4, 0)


                    
        