class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        n = num

        while i<=n:
            mid = (i+n) // 2

            if mid * mid == num:
                return True
            
            elif mid * mid > num:
                n = mid -1

            else:
                i = mid+1
            
        return False

        
        