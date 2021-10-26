from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        dp=[0]*n
        dp[0]= nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

if __name__=="__main__":
    # n = int(input("Enter size of array: "))
    # print("Enter elements in array")
    numList=[-2,1,-3,4,-1,2,1,-5,4]
    print(numList)
    # for i in range(n):
    #     x = int(input())
    #     numList.append(x)
    s = Solution()
    print("Sum of largest subarray: {}".format(s.maxSubArray(numList)))