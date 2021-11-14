#108. Convert Sorted Array to Binary Search Tree
from typing import List, Optional
import math
from BST.HelperClass.TreeNode import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        resultNode = self.convertBST(nums,0,len(nums)-1)
        return resultNode

    def convertBST(self,nums,start,end):
        if start == end: 
            return TreeNode(nums[start])
        if start>end: 
            return None
        node = TreeNode()
        mid = math.floor(start+(end-start)/2)
        node.val = nums[mid]
        node.left = self.convertBST(nums,start,mid-1)
        node.right = self.convertBST(nums,mid+1,end)
        return node


