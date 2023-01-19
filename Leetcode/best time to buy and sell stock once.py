class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far,max_profit = float('inf'), 0
        for price in prices:
            profit_sell_today = price - min_price_so_far
            max_profit = max(max_profit, profit_sell_today)
            min_price_so_far = min(min_price_so_far, price)
        return max_profit