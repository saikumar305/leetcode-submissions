class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # number = ''.join([str(x) for x in digits])
        # res = int(number) + 1

        # res = list(str(res))

        # return [int(x) for x in res]


        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] +=1

                return digits
            digits[i] = 0
        if i==0:
            return [1] + digits

        