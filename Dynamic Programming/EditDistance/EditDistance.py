class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[0]*len(word1)
        m = 0
        n = 0
        #Base Case
        if(m==0):
            pass 
        while(m!=len(word1) and n!=len(word2)):
            #No Action Taken
            if(word1[m]==word2[n]):
                dp[m] = dp[m-1]
                m+=1
                n+=1
            elif(word1[m]!=word2[n] and m==n):
                #Delete Action
                if(word1[m+1]==word2[n]):
                    dp[m] = dp[m-1]+1
                    n+=1
                #Replace()
                else:
                    dp[m] = 1+dp[m-1]
                    m+=1
                    n+=1
            else:
                dp[m]=1+dp[m-1]
                m+=1

            

                
                
            

    
if __name__=="__main__":
    w1 = "intention"
    w2 = "execution"

    s = Solution()
    print(s.minDistance(w1,w2))
        