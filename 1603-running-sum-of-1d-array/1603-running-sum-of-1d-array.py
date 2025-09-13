class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op = []

        for i in nums:
            if op:
                op.append(op[-1] +i)
            else:
                op.append(i)

        return op


        

        