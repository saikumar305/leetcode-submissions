class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        j = 0
        for i in range(len(t)):
            if  j<len(s) and t[i] == s[j]:
                j+=1
        
        return len(s) == j
        