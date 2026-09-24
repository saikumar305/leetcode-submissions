class Solution:
    def romanToInt(self, s: str) -> int:

        mapper = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        val = 0

        for  i in range(len(s)-1):
            if (mapper[s[i+1]] > mapper[s[i]]):
                val -= mapper[s[i]]

            else:
                val += mapper[s[i]]

        return val + mapper[s[-1]]
        
