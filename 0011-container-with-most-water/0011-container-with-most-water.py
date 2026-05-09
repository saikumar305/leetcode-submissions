class Solution:
    def maxArea(self, height: List[int]) -> int:
        # l = 0
        # maxarea = 0

        # for i in range(len(height)):
        #     for j in range(i, len(height)):
        #         maxarea = max(maxarea , min(height[i], height[j]) * (j-i)) 

        # return maxarea

        l, r = 0, len(height) -1
        maxarea = 0

        while l < r:
            maxarea = max(maxarea , min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxarea

            


        