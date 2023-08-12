from typing import List

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

test = Solution()
prices = [2, 4,1]
test2 = test.maxProfit(prices)
print(test2)