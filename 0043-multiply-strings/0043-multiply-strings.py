class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        mul = 1 
        ans = 0

        for i in range(len(num1)-1 , -1, -1):
            innmul = 1
            innans = 0

            for j in range(len(num2) -1 , -1, -1):
                innans += int(num2[j]) * int(num1[i]) * innmul
                innmul *=10
            
            ans += innans * mul
            mul *= 10

        return str(ans)
        
        