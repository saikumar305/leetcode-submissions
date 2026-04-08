class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # op = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             for l in range(k+1,len(nums)):
        #                 if nums[i] + nums[j] +nums[k] + nums[l] == target:
        #                     op.add(tuple(sorted([nums[i] , nums[j] , nums[k], nums[l]])))

        # return sorted([list(q) for q in op])
        op = []
        n= len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j+1
                right = n-1

                while left< right:
                    total = nums[i] + nums[j] +nums[left] + nums[right]

                    if total < target:
                        left +=1
                    elif total > target:
                        right -=1
                    else:
                        op.append([nums[i] , nums[j] ,nums[left] , nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return op


                    
        