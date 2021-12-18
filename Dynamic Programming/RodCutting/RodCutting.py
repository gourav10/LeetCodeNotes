class Solution:
    def maxPrice(self,n,prices)->int:
        if(n==0): return 0

        dp = [0]*n
        dp[0]=0
        for i in range(1,n+1):
            max_price = -float('inf')
            for k in range(i):
                max_price = max(prices[k]+dp[i-k-1],max_price)
            dp[i] = max_price
            print(dp)
        return dp[n] 
            


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(prices)
    s = Solution()
    print(prices)
    print(s.maxPrice(n,prices))


