from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            nums[i] = nums[i]+nums[i+1]
            nums[i+1] = 0
        
if __name__=="__main__":
    nums=[0,1,0,3,12]
    print(nums)
    s = Solution()
    s.moveZeroes(nums)
    print(nums)