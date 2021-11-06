class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        lookUpList={}
        for ch in s:
            lookUpList[ch]=0
            
        for ch in s:
            lookUpList[ch]+=1
        validSubstr = True
        filterChars = list()
        for i in range(len(s)):
            if lookUpList[s[i]] < k:
                filterChars.append(s[i])
                validSubstr = False
        
        if validSubstr:
            return len(s)

        for letter in filterChars:
            s = s.replace(letter, ' ')

        modifiedStr = s.split()
        ssLen = 0
        for substr in modifiedStr:
            ssLen = max(ssLen,self.longestSubstring(substr,k))        
        
        return ssLen
    
if __name__ == '__main__':
   sInput = "ababacb"
   k = 3
   s = Solution()
   print("Input: {}".format(sInput))
   print("Length of longest substring with atleast {} characters is {}".format(k,s.longestSubstring(sInput,k))) 