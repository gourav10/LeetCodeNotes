class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

#Top-Down with Memoization
    memo={}
    memo[1]=1
    memo[2]=2
    def climbStairsMemoization(self,n:int)->int:
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairsMemoization(n-1)+self.climbStairsMemoization(n-2)

#Bottom-Up Approach
    def climbStairsDP(self,n:int)->int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        C={}
        C[1]=1
        C[2] = 2
        for i in range(3,n+1):
            C[i] = C[i-1]+C[i-2]
        return C[n]
    

if __name__=="__main__":
    s = Solution()
    noStairs = int(input("Enter number of stairs: "))
    print("Total Number of ways to climb: {}".format(s.climbStairsDP(noStairs)))