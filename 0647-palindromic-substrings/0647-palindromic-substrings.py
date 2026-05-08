class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        def ispalindrome(ss):
            return ss == ss[::-1]
        
        res = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if ispalindrome(s[i:j+1]):
                    c+=1
        

        return c