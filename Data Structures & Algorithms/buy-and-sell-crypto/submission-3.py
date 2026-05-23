class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_prof = 0 
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            else:
                max_prof = max(max_prof, profit)
                r += 1
        
        return max_prof