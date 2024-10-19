class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        if rowIndex ==0:
            return row

        for i in range(rowIndex):
            row = [left + right for left, right in zip([0]+row, row+[0])]
        return row
