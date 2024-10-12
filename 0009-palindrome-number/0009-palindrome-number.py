class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        temp = x
        while temp>0:
            print(reversed)
            reversed = reversed*10 + temp%10
            print("---", reversed)
            temp = temp//10
        print(reversed)
        return x == reversed

        
        