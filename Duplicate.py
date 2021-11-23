from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return i
        return -1

if __name__=="__main__":
    s = Solution()
    ip = [1,3,4,2,2]
    print("Input: {}".format(ip))
    print("Output: {}".format(s.findDuplicate(ip)))