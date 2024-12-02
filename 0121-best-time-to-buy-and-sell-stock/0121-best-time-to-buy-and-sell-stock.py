class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0];
        n = len(prices);
        
        for i in range(0,n):
            mini = min(mini,prices[i])        
            profit = prices[i]-mini
            maxi = max(maxi,profit)
            
        return maxi