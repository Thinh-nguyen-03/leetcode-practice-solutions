class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        min_price = float('inf')  # Initialize to infinity
        max_profit = 0

        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Calculate the potential profit
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)

        return max_profit
