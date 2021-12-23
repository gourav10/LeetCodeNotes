from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i1 = self.binarySearchLeft(nums,0,(len(nums)-1),target)
        i2 = self.binarySearchRight(nums,0,len(nums)-1,target)
        return [i1,i2]

    def binarySearchLeft(self, arr,start,end, key):
        res = -1
        while(start <= end):
            mid = (start+end)//2
            if(arr[mid] == key):
                res = mid
                end = mid-1
            elif(arr[mid] > key):
                end = mid - 1
            else:
                start = mid + 1
        return res

    def binarySearchRight(self, arr,start,end, key):
        res = -1
        while(start <= end):
            mid = (start+end)//2
            if(arr[mid] == key):
                res = mid
                start = mid+1
            elif(arr[mid] > key):
                end = mid - 1
            else:
                start = mid + 1
        return res

if __name__=="__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    s = Solution()
    print(s.searchRange(nums,target))