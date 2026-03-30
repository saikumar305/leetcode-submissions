class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = sorted(heights)
        c = 0

        for i in range(len(heights)):
            if heights[i] != new[i]:
                c+=1
        return c
        