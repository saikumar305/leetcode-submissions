class Solution:
    def fillCups(self, amount: List[int]) -> int:

        heap = [-a for a in amount if a>0]
        heapq.heapify(heap)

        time = 0

        while heap:
            first = -heapq.heappop(heap)

            if heap:
                second = -heapq.heappop(heap)
                second -= 1
                if second>0:
                    heapq.heappush(heap, -second)

            first-=1
            
            if first>0:
                    heapq.heappush(heap, -first )
            
            time+=1
            
        return time
            