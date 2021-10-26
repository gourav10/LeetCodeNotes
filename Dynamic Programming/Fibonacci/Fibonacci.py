class Solution:
    def fib(self, n: int) -> int:
        dp=dict()
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

if __name__=="__main__":
    s = Solution()
    num = int(input("Enter a Number: "))
    if num%10==1:
        print("{}st Fibonacci Number: {}".format(num,s.fib(num)))
    elif num%10==2:
        print("{}nd Fibonacci Number: {}".format(num,s.fib(num)))
    elif num%10==3:
        print("{}rd Fibonacci Number: {}".format(num,s.fib(num)))
    else:
        print("{}th Fibonacci Number: {}".format(num,s.fib(num)))

