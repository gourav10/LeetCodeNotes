from typing import List
import math
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1 for i in range(n)]
        
        lookUp = dict()

        for p in primes:
            lookUp[p] = 0
        print(lookUp)

        for i in range(1,n):
            minVal = math.inf
            for p in primes:
                minVal = min(minVal,dp[lookUp[p]]*p)
            for p in primes:
                if(minVal == dp[lookUp[p]]*p):
                    lookUp[p]+=1
            dp[i] = minVal
        return dp[n-1]
            
                
            


if __name__=="__main__":
    n = 1
    primes = [2,3,5]

    sol = Solution()
    print(sol.nthSuperUglyNumber(n,primes))
