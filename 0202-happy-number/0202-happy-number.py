class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        def sumofnumbers(n):
            add = 0
            if n<=3:
                return n
            for i in str(n):
                add += (int(i) **2)
            if add in sum_set:
                return 0
            else:
                sum_set.add(add)
            return sumofnumbers(add)

        return True if sumofnumbers(n)==1 else False
            
        