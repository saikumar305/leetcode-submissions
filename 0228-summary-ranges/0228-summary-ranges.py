class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        if not nums:
            return res

        s = nums[0]
        end = nums[0]

        for i in range(len(nums)-1):
            num= nums[i]
            if num+1 in nums:
                end = num+1
                continue
            else:
                if s == end:
                    res.append(str(s))
                else:
                    res.append(f"{s}->{end}")
            s = nums[i+1]
            end = nums[i+1]

        if s == end:
            res.append(str(s))
        else:
            res.append(str(s) + "->" + str(end))

        return res


            

        