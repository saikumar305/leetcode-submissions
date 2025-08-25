class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]
        
        max1 = max(stones)
        stones.remove(max1)
        max2 = max(stones)
        stones.remove(max2)

        if max1 - max2:
            stones.append(max1-max2)
        
        return self.lastStoneWeight(stones)

            

        