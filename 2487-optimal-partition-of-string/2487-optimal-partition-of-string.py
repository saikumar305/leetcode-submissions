class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        sub = ''
        for i in s:
            if  i not in sub:
                sub +=i
            else:
                sub = ''+i
                res+=1
        return res+1
        