class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        op = []
        for i in range(numRows):

            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = op[i-1][j-1] +op[i-1][j]

            op.append(row)


        return op

            
        