class Solution:
    def addDigits(self, num: int) -> int:

        num_str = str(num)
        if len(num_str) == 1:
            return num
        sum_ = 0
        for s in num_str:
            sum_+= int(s)

        return self.addDigits(sum_)
        
        