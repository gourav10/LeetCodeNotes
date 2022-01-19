from tkinter import SOLID
from typing import List

class Solution:
    def nonConstructibleChange(self,coins:List[int])->int:
        coins.sort()
        currentChangeCreate=0
        for coin in coins:
            if(coin>currentChangeCreate+1):
                return currentChangeCreate+1
            currentChangeCreate+=coin
            
        return currentChangeCreate+1
        

if __name__=='__main__':
    coins=[1,1,1,1,1]
    s = Solution()
    print(s.nonConstructibleChange(coins))
