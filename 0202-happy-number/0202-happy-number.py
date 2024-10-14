class Solution:
    def getNext(self,num):
            sum = 0
            while num>0:
                digit = num%10
                sum+= digit**2
                num//=10
            return sum

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = self.getNext(n)

        while(fast !=1 and slow != fast):
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return fast == 1
            
        