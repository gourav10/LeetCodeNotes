from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        start = (root,0)
        depth = 0

        frontier = [start]
        while(frontier):
            u,nodeLevel = frontier.pop()
            
            if(u == None):
                return 0
            
            if(depth<nodeLevel):
                depth = nodeLevel

            if(u.right):
                frontier.append(u.right,nodeLevel+1)
            
            if(u.left):
                frontier.append(u.left,nodeLevel+1)
        return depth
        
if __name__ == '__main__':
    
