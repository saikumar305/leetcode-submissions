class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) -2):
            j, k =i+1 , len(nums) -1

            while j<k:
                curr_sum = nums[i] +nums[j] + nums[k]
                if abs(closest_sum -target) > abs(curr_sum -target):
                    closest_sum  = curr_sum
                if curr_sum < target:
                    j +=1
                elif curr_sum > target:
                    k -= 1
                else:
                    return curr_sum

        return closest_sum