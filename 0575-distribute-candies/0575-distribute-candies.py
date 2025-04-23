class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        hashmap = {}
        for i in candyType:
            hashmap[i] = hashmap.get(i,0)+1

        return int(min(len(candyType) / 2 , len(hashmap)))

        