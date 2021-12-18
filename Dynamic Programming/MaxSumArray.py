class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if(n==0):
            return 0
        nums = list()
        nums.append(0)
        nums.append(1)
        
        i=1
        while(i<=n):
            if(2*i>=0 and 2*i<=n):
                nums.append(nums[i])
            if(2*i+1>=0 and 2*i+1<=n):
                nums.append(nums[i+1]+nums[i])
            i+=1
        
        return max(nums)


if __name__=="__main__":
    n = 3
    s = Solution()
    print(s.getMaximumGenerated(n))