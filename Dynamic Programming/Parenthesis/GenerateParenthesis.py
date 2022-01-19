from typing import List
class Solution:
    def generateParenthesis(self, n: int):
        dp=[[] for i in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                dp[i]+=['('+ x +')'+y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]

if __name__=="__main__":
    n=3
    s = Solution()
    print(s.generateParenthesis(n))