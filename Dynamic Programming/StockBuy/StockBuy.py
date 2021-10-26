from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: return 0

        maxProfit=-math.inf
        minPrice = prices[0]
        for i in range(1,len(prices)):
            minPrice = min(minPrice,prices[i])
            maxProfit = max(maxProfit,prices[i]-minPrice)
        return maxProfit

if __name__=="__main__":
    stockList = [7,1,5,3,6,4]
    s = Solution()
    print("Stocks: {}".format(stockList))
    print("Max Profit: {}".format(s.maxProfit(stockList)))