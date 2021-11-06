from typing import Tuple


class Solution:
    ValidRomanChars={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    def romanToInt(self, s: str) -> int:
        n = len(s)
        num = 0
        for i in range(n):
            if i+1<n and self.ValidRomanChars[s[i]]<self.ValidRomanChars[s[i+1]]:
                num -= self.ValidRomanChars[s[i]]
            else:
                num += self.ValidRomanChars[s[i]]
        return num

    


if __name__=="__main__":
    s = Solution()
    print(s.ValidRomanChars)
    romanNum = str(input("Enter a Roman Number: "))
    print("The Decimal Form of {} is: {}".format(romanNum,s.romanToInt(romanNum)))

    