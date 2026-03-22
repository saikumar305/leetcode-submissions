class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-num for num in nums]

        heapq.heapify(heap)
        largest = None

        for i in range(k):
            largest = -heapq.heappop(heap)


        return largest
        