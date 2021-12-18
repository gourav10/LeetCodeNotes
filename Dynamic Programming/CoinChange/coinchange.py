from typing import List        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # code here
        dp=[-float('inf') for i in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for k in coins:
                if(i>=k):
                    dp[i] = min(dp[i],dp[i-k]+1)

        if(dp[amount]==amount+1):
            return -1
        return dp[amount]  
              
if __name__ == "__main__":
    s = Solution()
    ip = [1,2,5]
    n = 11
    print("I/P: {},{}".format(n,ip))
    print("O/P: {}".format(s.coinChange(ip,n)))