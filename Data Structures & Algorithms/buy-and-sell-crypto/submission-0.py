class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                buy = prices[i]
                sell = prices[j]
                prof = sell - buy
                if prof > max_prof:
                    max_prof = prof
        return max_prof
        