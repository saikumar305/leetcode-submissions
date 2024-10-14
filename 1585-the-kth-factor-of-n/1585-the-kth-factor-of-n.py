class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1,int(n/2)+1):
            if n%i == 0:
                factors.append(i)
        factors.append(n)
        return factors[k-1] if k<=len(factors) else -1

        