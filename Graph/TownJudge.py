from typing import List
import math

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        lookUp = dict()
        if len(trust)==1:
            return trust[0][1]
        for edge in trust:
            if edge[1] in lookUp:
                lookUp[edge[1]]+=1
            else:
                lookUp[edge[1]]=1
        
        judge = 0
        for person in lookUp.keys():
            if(max(judge,lookUp[person])==lookUp[person]):
                judge=person

        if(lookUp[judge]==n-1):
            
            return judge

        return -1

if __name__=="__main__":
    n = 4
    trust = [[1,3]]
    s = Solution()
    print(s.findJudge(n,trust))