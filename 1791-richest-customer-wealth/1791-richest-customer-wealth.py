class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        for r in accounts:
            maxx = max(sum(r), maxx)

        return maxx