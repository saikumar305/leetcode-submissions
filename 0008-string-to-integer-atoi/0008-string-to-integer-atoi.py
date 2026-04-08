class Solution:
    def myAtoi(self, s: str) -> int:
        

        s = s.strip()
        if not s:
            return 0

        num = 0
        i=0
        sign = 1
        if s[i] == "-" or s[i] == '+':
            sign = -1 if s[i] == '-' else 1
            i+=1
        

        int_max = 2**31 -1
        int_min = -2**31
        while i < len(s) and s[i].isdigit():
            if num > (int_max - int(s[i])) // 10:
                return int_max if sign ==1 else int_min

            num = num*10 +int(s[i])
            i+=1
             
        return sign * num


        

        