from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]):
        if(root==None):
            return [""]
        start = (root,[root.val])
        frontier = []
        result = list()
        frontier.append(start)
        while(frontier):
            u,pathList = frontier.pop()
            if(u.left==None and u.right==None):
                resStr = ""
                for i in range(len(pathList)):
                    if i==0:
                        resStr+=str(pathList[i])
                    else:
                        resStr+="->"+str(pathList[i])
                result.append(resStr)
            else:
                if(u.left):
                    frontier.append((u.left,pathList+[u.left.val]))
                if(u.right):
                    frontier.append((u.right,pathList+[u.right.val]))
        return result

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    s = Solution()
    print(s.binaryTreePaths(root))