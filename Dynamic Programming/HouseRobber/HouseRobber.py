from typing import List

#198. House Robber (Medium)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums)

        dp = [0]*len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2,len(nums)):
            maxAmt = -float('inf')
            for j in range(i-1):
                maxAmt = max(maxAmt,dp[j])
            dp[i] = max(nums[i]+maxAmt,dp[i-1])
        return dp[len(nums)-1]

if __name__=="__main__":
    s = Solution()
    nums = [2,1,1,2]
    print("Input: {}".format(nums))
    print("Expected Output: 4")
    print("Actual Output: {}".format(s.rob(nums)))
