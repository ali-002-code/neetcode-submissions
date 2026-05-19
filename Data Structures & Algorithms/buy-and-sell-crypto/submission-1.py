class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_prof = 0
        for price in prices:
            min_price = min(price, min_price)
            prof = price - min_price
            max_prof = max(prof, max_prof)
        return max_prof