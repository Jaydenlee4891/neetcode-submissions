class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        profit=0
        for right in range(1,len(prices)):
            if prices[right]<prices[left]:
                left=right
            else:
                current_profit=prices[right]-prices[left]
                profit = max(profit, current_profit)
        return profit