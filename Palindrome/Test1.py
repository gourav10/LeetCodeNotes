class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree,target):
    diffList = dict()

    def InOrder(tree,target,diffList):
        if tree:
            if(target <= tree.value):
                diff = tree.value - target
            else:
                diff = target - tree.value
            diffList[tree.value] = diff
            InOrder(tree.left,target,diffList)
            InOrder(tree.right,target,diffList)

    InOrder(tree,target,diffList)
    return min(diffList.items(),key = lambda x:x[1])[0]

if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.right = BST(22)
    root.right.left = BST(13)
    root.right.left.right = BST(14)

    target  = 12
    print(findClosestValueInBst(root,target))




