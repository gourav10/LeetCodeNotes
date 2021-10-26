from typing import List

class Solution:
    def Solution(self):
        self.charList=list()
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) ==0: return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strList[i].index(prefix)!=0:
                prefix = prefix[0,len(prefix)-1]
                if not prefix: return ""
        return prefix


if __name__ =="__main__":
    s = Solution()
    strList= list()
    list_size = int(input("Enter size of list: "))
    for i in range(list_size):
        s = input()
        strList.append(s)
    print(strList)
    print("LCP: {}".format(s.longestCommonPrefix(strList)))
