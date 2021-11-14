class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==" ":
            return 1
        if s=="":
            return 0
        tempSub = s[0]
        maxSub = s[0]
        maxLen = len(tempSub)
        start = 0
        end = 1
        while end <len(s):
            index = tempSub.find(s[end])
            if index!=-1:
                start = start+index+1
                maxSub = maxSub if len(maxSub) > len(tempSub) else tempSub
                maxLen = len(maxSub)
                tempSub = s[start:end+1]
            else:
                tempSub = tempSub +s[end]
                maxSub = maxSub if len(maxSub) > len(tempSub) else tempSub
                maxLen = len(maxSub)    
            end+=1
        return maxSub,maxLen 

if __name__=="__main__":
    sln = Solution()
    s = "bbbbb"
    print("Input: {}".format(s))
    print("Output: {}".format(sln.lengthOfLongestSubstring(s)))