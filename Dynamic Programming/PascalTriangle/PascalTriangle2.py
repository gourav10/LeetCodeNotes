from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        dp=list()
        for i in range(0,rowIndex+1):
            tempList=list()
            for k in range(0,i+1):
                tempList.append(1)
            dp.append(tempList)

        for i in range(2,rowIndex+1):
            for k in range(1,i):
                dp[i][k] = dp[i-1][k-1]+dp[i-1][k]    
        return dp[rowIndex]

if __name__=="__main__":
    rowIndex = int(input("Enter the Row Index of Pascal Triangle: "))
    s = Solution()
    pascalCalcList = s.getRow(rowIndex)
    print("Result: {}".format(pascalCalcList))