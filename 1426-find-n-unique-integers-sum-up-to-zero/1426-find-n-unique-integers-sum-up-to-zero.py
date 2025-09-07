class Solution:
    def sumZero(self, n: int) -> List[int]:
        op = []
        for i in range(1, n//2 + 1):
            op.extend([i,-i])
        
        if n%2 != 0:
            op.append(0)

        return op
        
        