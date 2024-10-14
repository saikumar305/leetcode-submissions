class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        c=1
        for i in range(2,int(n/2)+1):
            if n%i == 0:
                factors.append(i)
                c+=1
                if c == k:
                    return factors[k-1]
        factors.append(n)
        return factors[k-1] if k<=len(factors) else -1

        