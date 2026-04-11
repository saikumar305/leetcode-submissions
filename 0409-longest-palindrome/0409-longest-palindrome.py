class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapper = {}

        for i in s:    
            mapper[i] = mapper.get(i, 0) + 1
        c = 0
        odd = False
        for k, v in mapper.items():
            c +=(v//2) * 2 
            if v%2 == 1:
                odd =True

        return c+1 if odd else c      
        