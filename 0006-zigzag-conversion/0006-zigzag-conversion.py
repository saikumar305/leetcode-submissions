class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        curr_row, d = 0, 1
        res = [""]* numRows

        for ch in s:

            if curr_row ==0:
                d = 1
            elif curr_row == numRows -1:
                d = -1

            res[curr_row] += ch
            curr_row +=d

            

        return ''.join(res)