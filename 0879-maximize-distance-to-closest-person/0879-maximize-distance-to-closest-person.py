class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        oc_i = []

        for i in range(len(seats)):
            if seats[i]==1:
                oc_i.append(i)

        print(oc_i)

        mid_diff = 0
        start = oc_i[0]
        end = len(seats) - oc_i[-1] -1
        for i in range(len(oc_i)-1):
            mid_diff = max(oc_i[i+1]-oc_i[i], mid_diff)
            
        
        return max([start, end, mid_diff//2])

        