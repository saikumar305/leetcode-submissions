class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        # curr_max = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             curr_max = curr_max if curr_max > prices[j] - prices[i] else prices[j] - prices[i]

        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy


        return profit


        