from typing import Counter


class Result:
    def checkMagazine(self,magzine:str,note:str)->bool:
        lookUp=dict()
        
        for s in magzine.split():
            if s in lookUp:
               lookUp[s]+=1
            else:
                lookUp[s]=1
        
        noteLookUp=dict()
        
        for s in note.split():
            if s in noteLookUp:
                noteLookUp[s]+=1
            else:
                noteLookUp[s]=1
        
        for word in noteLookUp.keys():
            if  word in lookUp:
                if noteLookUp[word]>lookUp[word]:
                    return False
            else:
                return False
        return True

if __name__=="__main__":
    mag="give me one grand today night"
    note = "give one grand today"
    s = Result()
    print(s.checkMagazine(mag,note))