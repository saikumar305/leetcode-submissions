class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = []
        if rowIndex == 0:
            return [1]

        for i in range(0, rowIndex+1):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)
        return pascal[rowIndex]
        