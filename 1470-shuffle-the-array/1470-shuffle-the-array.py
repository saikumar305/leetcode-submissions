class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x= nums[:n]
        y = nums[n:]
        print(x, y)
        op = []

        for i in range(n):
            op.extend([x[i], y[i]])

        return op
        




        