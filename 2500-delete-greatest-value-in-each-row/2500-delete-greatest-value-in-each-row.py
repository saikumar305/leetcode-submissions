class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for row in grid:
            row.sort()

        res = 0

        for c in range(len(grid[0]) -1 , -1, -1):

            res += max([row[c] for row in grid])

        return res


        