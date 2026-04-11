class Solution:
    def minimumMoves(self, s: str) -> int:
        i =0
        c = 0
        while i < len(s):
            if s[i] == 'X':
                i+=3
                c+=1
            else:
                i+=1

        return c

            
            