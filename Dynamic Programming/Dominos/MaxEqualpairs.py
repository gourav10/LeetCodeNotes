from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dp={}
        sum =0
        for i in dominoes:
            x,y = min(i),max(i)
            if (x,y) not in dp:
                dp[(x,y)] = 1
            else:
                sum+=dp[(x,y)]
                dp[(x,y)]+=1
        return sum


if __name__=="__main__":
    dominospairs =[[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
    s = Solution()

    print("No. of Equal Pairs: {}".format(s.numEquivDominoPairs(dominospairs)))