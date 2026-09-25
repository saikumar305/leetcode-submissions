class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = ''.join([str(x) for x in digits])
        res = int(number) + 1

        res = list(str(res))

        return [int(x) for x in res]
        