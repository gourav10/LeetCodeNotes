class Solution:
    def CheckSimilar(self,str1:str, str2:str)->bool:
        s1=str1.lower()
        s2=str2.lower()
        lookUp={}
        for s in s1:
            lookUp[s]=0

        for s in s1:
            lookUp[s]+=1
        
        result=True        
        for s in s2:
            if s in lookUp:
                continue
            else:
                result=False 
                
        return result

if __name__=="__main__":
    s1 = 'rat'
    s2='tag'
    sol = Solution()
    print(sol.CheckSimilar(s1,s2))
