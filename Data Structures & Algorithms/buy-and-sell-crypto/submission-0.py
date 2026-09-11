
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy pointer (represents the lowest price seen so far)
        max_profit = 0
        
        for right in range(1, len(prices)):
            # If we find a price lower than our current buy price, shift our buy pointer
            if prices[right] < prices[left]:
                left = right
            else:
                # Otherwise, calculate profit and update max_profit if it's higher
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
                
        return max_profit