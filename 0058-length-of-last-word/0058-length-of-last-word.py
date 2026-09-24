class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0

        i = len(s) -1
        while s[i].isspace():
            i-=1

        while i >=0 and s[i].isalpha():
            c+=1
            i-=1

        return c


            
        