class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            for c in r:
                if c ==target:
                    return True
        
        return False
        