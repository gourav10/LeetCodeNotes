from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result=list()
        for i in range (n+1):
            temp = "{0:b}".format(i)
            c=0
            for j in temp:
                if j=='1':
                    c+=1
            result.append(c)

        return result

if __name__=="__main__":
    s= Solution()
    n = int(input("Enter a number: "))
    print("The number of 1s in Binary Numbers from {} to {} are: {}".format(0,n+1,s.countBits(n)))


