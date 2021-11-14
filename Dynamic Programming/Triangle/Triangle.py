from typing import List, TextIO

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle)-1)):
            for j in range(i+1):
                triangle[i][j] = triangle[i][j]+min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]

if __name__=="__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    s = Solution()
    print("Input: {}".format(triangle))
    print("Output: {}".format(s.minimumTotal(triangle)))
