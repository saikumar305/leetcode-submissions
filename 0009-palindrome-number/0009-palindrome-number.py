class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # reversed = 0
        # temp = x
        # while temp>0:
        #     reversed = reversed*10 + temp%10
        #     temp = temp//10

        # return x == reversed
        return str(x) == str(x)[::-1]

        
        