class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)==0: return 0
        ans, prev, curr = 0,0,1
        for i in range(1,len(s)):
            if s[i-1] is not s[i]:
                ans+=min(prev,curr)
                prev,curr = curr,1
            else:
                curr+=1
        return ans+min(prev,curr)


if __name__=="__main__":
    inp="00110011"
    sol = Solution()
    print("Input: {}".format(inp))
    print("No. Of Binary Substrings: {}".format(sol.countBinarySubstrings(inp)))