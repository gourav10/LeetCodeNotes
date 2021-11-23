from HelperClass.TreeNode import TreeNode
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathSum(root,targetSum,)
        
    def pathSum(self,root,targetSum,pSum=0)->bool:
        if(root==None):
            return False
        
        pSum +=root.val
        
        if(root.left==None and root.right==None):
            if(pSum==targetSum): return True
            else: return False
        else:
            if(self.pathSum(root.left,targetSum,pSum)==True or self.pathSum(root.right,targetSum,pSum)==True):
                return True
            else:
                return False

if __name__=="__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(13)
    root.right.right.right= TreeNode(1)

    targetSum = 22
    s = Solution()
    print("Result: {}".format(s.hasPathSum(root,targetSum)))
