class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.pathSum=0
        def dfs(root):
            if(root is None):
                return 0
            dfs(root.right)
            self.pathSum = self.pathSum+root.val
            root.val = self.pathSum
            dfs(root.left)
            return root
        root = dfs(root)
        return root

    def printBST(self,root):
        if(root is None):
            return
        print(root.val,end=' ')
        self.printBST(root.left)
        
        self.printBST(root.right)

if __name__=='__main__':
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    s = Solution()
    newRoot = s.bstToGst(root)
    s.printBST(newRoot)
