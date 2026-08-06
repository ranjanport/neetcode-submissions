class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
            else:
                buy_price = min(buy_price, prices[i])
        
        return profit
        