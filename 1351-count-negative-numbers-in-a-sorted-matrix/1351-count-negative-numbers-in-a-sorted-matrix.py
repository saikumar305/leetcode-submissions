class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        m = len(grid) - 1
        n = len(grid[0])
        j = 0

        while (m >= 0 and j < n):
            if grid[m][j] >= 0: j+=1
            else:
                c += n -j
                m-=1

        return c

        