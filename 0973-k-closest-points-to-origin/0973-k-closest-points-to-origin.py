class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lengths = []

        for x, y in points:
            dist = x**2 + y**2
            lengths.append((-dist, [x,y]))

        heap = []

        for i in lengths:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [p for _, p in heap]



        