class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:

        cash = 0
        hold = -prices[0]

        for price in prices[1:]:

            previous_cash = cash

            # Sell stock today
            cash = max(cash, hold + price - fee)

            # Buy stock today
            hold = max(hold, previous_cash - price)

        return cash