class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0
        is_negative = False
        if x < 0:
            x = abs(x)
            is_negative = True
        
        while x:
            ans = (ans * 10) + (x % 10)
            if not -2**31 <= ans <= 2**31 - 1:
                return 0
            x //= 10

        return int(ans) if not is_negative else -ans
        