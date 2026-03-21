class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        # gifts.sort()

        # for i in range(k):
        #     val = gifts.pop()
        #     gifts.append(math.floor(val**0.5))
        #     gifts.sort()

        # return sum(gifts)

        heap = [-g for g in gifts]

        heapq.heapify(heap)

        for i in range(k):
            largest = -heapq.heappop(heap)
            value = int(math.isqrt(largest))
            heapq.heappush(heap, -value)
        
        return -sum(heap)



        