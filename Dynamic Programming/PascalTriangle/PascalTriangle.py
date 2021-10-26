from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=list()
        for i in range(numRows):
            tempList=[]
            for k in range(i+1):
                tempList.append(1)
            dp.append(tempList)

        
        for i in range(2,numRows):
            for k in range(1,i):
                dp[i][k] = dp[i-1][k-1]+dp[i-1][k]
        return dp

if __name__=="__main__":
    numRows = int(input("Enter size of Pascal Tree: "))
    s = Solution()
    print(s.generate(numRows))
        