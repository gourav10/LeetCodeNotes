from typing import List

#1525. Number of Good Ways to Split a String
class Solution:

    memo = []
    def numSplits(self, s: str) -> int:
        memo = [[0]*len(s) for i in range(s)]
        noGoodSplits = self.topDownDp(s,memo)

    def topDownDp(self,s: str,memo: List[List[int]]) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

    def distinctChars(self,s: str)-> int:
        lookUp={}
        for ch in s:
            lookUp[ch] = 0
        
        return lookUp.keys

        



if __name__=="__main__":
    ip = "aacaba"
    s = Solution()
    print("Input: {}".format(ip))
    print("Output: {}".format(s.numSplits(ip)))