class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        l = len(prices)

        for i in range(l):
            for j in range(i+1, l):
                diff = prices[j] - prices[i]
                if diff >= profit:
                    profit = diff
                else:
                    continue
        
        return profit
                