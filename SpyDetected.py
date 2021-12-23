from typing import DefaultDict, List


from typing import List

class Solution:
    def SpyDetect(self,arr:List):
        lookUp=dict()
        
        for item in arr:
            if item in lookUp:
                lookUp[item]+=1
            else:
                lookUp[item]=1

        for key in lookUp:
            if(lookUp[key]==1):
                return arr.index(key)+1
        return -1

if __name__=="__main__":
    s = Solution()
    it = int(input(""))
    for i in range(it):
        n = int(input(""))
        inp = input("")
        arr = [int(ch) for ch in inp.split(" ")]
        print(s.SpyDetect(arr))

    
