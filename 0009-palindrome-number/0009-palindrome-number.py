class Solution:
    def isPalindrome(self, x: int) -> bool:

        ans = 0
        ip = x
        if x < 0:
            return False
        
        while x:
            ans = (ans * 10) + (x % 10)
            if not -2**31 <= ans <= 2**31 - 1:
                return False
            x //= 10

        ans = int(ans)

        return ip == ans
        