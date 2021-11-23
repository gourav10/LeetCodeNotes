from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad={
            {1,[]},
            {2,['abc']},
            {3,['d','e','f']},
            {4,['g','h','i']},
            {5,['j','k','l']},
            {6,['m','n','o']},
            {7,['p','q','r','s']},
            {8,['t','u','v']},
            {9,['w','x','y','z']}
        }

        if len(digits)==0:
            return []
        
        if len(digits)==1:
            return keypad[int(digits)]
        result=[]
        for digit in digits:
            pass
    
    def letterCombinations2(self, digits:str):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations2(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]

if __name__=="__main__":
    digits = "234"
    print(digits[:-1])
    s = Solution()
    print(s.letterCombinations2(digits))