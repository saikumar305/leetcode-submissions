class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        m = len(image)
        n = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image
        def dfs(sr, sc):

            if (sr >= 0 and sc >= 0 and sr < m and sc < n ) and image[sr][sc] == original:
                image[sr][sc] = color
            else:
                return

            dfs(sr-1, sc)
            dfs(sr, sc-1)
            dfs(sr+1, sc)
            dfs(sr,sc+1)

        dfs(sr, sc)


        return image

        


        