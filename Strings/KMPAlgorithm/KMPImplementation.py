##
# This algorithm is used to find occurence of a pattern in a string.
# #

from typing import Pattern


class Solution:
    ##
    # Steps involved in KMP Algorithm:
    # 1. Generate LPS Table
    # 2. Compare the i,j indexes.
    # #
    def computeLPS(self,lps,n,pat):
        len=0
        i=1
        while i<n:
            if pat[i]==pat[len]:
                len+=1
                lps[i] = len
                i+=1
            else:
                if len!=0:
                    len = lps[len-1]
                else:
                    lps[i] = 0
                    i+=1


    def subStringOccurence(self,inputStr,pattern):
        
        m = len(pattern)
        n = len(inputStr)    
      
        piTable = [0]*m

        self.computeLPS(piTable,m,pattern)
        
        i=0
        j=0

        while(i<n):
            if pattern[j]==inputStr[i]:
                i+=1
                j+=1
            
            if j==m:
                print("Found at index: {}".format((i-j)))
                j = piTable[j-1]
            
            elif(i<n and pattern[j]!=inputStr[i]):
                if j!=0:
                    j = piTable[j-1]
                else:
                    i+=1

if __name__=="__main__":
    text = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    s = Solution()
    s.subStringOccurence(text,pat)

  
            
        
        