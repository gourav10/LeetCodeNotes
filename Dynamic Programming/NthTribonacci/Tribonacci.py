class Solution:
    #The Tribonacci sequence Tn is defined as follows: 
    #T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    #Given n, return the value of Tn.
    
    def tribonacci(self, n: int) -> int:
        dp=dict()
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
            print(dp[i])
        return dp[n]

if __name__=="__main__":
    s = Solution()
    num = int(input("Enter a number: "))
    if num%10==1:
        print("{}st Tribonacci Number: {}".format(num,s.tribonacci(num)))
    elif num%10==2:
        print("{}nd Tribonacci Number: {}".format(num,s.tribonacci(num)))
    elif num%10==3:
        print("{}rd Tribonacci Number: {}".format(num,s.tribonacci(num)))
    else:
        print("{}th Tribonacci Number: {}".format(num,s.tribonacci(num)))
        
