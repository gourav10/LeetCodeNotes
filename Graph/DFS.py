
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.DFSUtil(root)
    
    def DFSUtil(self,root):
        start = (root,0)
        frontier = []
        frontier.append(start)
        result = 0
        while(frontier):
            u,currNum = frontier.pop()
            if(u is not None):
                currNum = currNum<<1|u.val
                if(u.left==None and u.right==None):
                    result += currNum
                else:
                    frontier.append((u.left,currNum))
                    frontier.append((u.right,currNum))
        return result 
        


if __name__=="__main__":
    graph = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    s = Solution()
    s.sumRootToLeaf(root)