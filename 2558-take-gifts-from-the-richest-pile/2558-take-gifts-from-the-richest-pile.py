class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts.sort()

        for i in range(k):
            val = gifts.pop()
            gifts.append(math.floor(val**0.5))
            gifts.sort()

        return sum(gifts)
        