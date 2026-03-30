class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b = 0
        op = 0

        for i in s:
            if i == 'R':
                b-=1
            if i == 'L':
                b+=1
            if b == 0:
                op +=1

        return op

        