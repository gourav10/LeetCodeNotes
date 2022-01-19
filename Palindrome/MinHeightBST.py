class Node:
    def __init__(self,value) -> None:
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # use mergesort technique 
    def minHeightBST(self, array):
        low = 0
        high = len(array)-1

        def generateTree(array,low,high):
            if(high<low):
                return None

            mid = (low+high)//2
            node = Node(array[mid])
            node.left = generateTree(array,low,mid-1)
            node.right = generateTree(array,mid+1,high)
            return node

        root = generateTree(array,low,high)
        return root

        

    def printBST(self,root):
        if(root is None):
            return
        
        self.printBST(root.left)
        print(root.val,end=' ')
        self.printBST(root.right)

if __name__=='__main__':
    arr = [1,2,5,7,10,13,14,15,22]
    s = Solution()
    root = s.minHeightBST(arr)
    s.printBST(root)