class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        start , end = 0 , len(str(x))-1

        str_x = str(x)

        while start < end:
            if str_x[start] == str_x[end]:
                start +=1
                end -= 1
            
            else:
                return False

        return True
        