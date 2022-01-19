from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.numList=[]
        def inOrder(root):
            if(root):
                inOrder(root.left)
                self.numList.append(root.val)
                inOrder(root.right)
        inOrder(root1)
        inOrder(root2)
        self.numList.sort()
        return self.numList

if __name__=='__main__':
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)


    root2=TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)

    s = Solution()
    numList = s.getAllElements(root1,root2)
    print(numList)