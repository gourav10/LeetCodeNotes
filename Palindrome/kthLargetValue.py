class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left  = None
        self.right = None

class Solution:
    def kthLargetsNode_old(self,root,k):
        sortedList = []
        self.inOrderTraverse(root,sortedList)
        print(sortedList)
        #sortedList.sort(reverse=True)
        #print(sortedList)
        return sortedList[-k]
    
    def inOrderTraverse(self,root,sortedList):
        if(root):
            self.inOrderTraverse(root.left,sortedList)
            sortedList.append(root.value)
            self.inOrderTraverse(root.right,sortedList)

    def kthLargetsNode(self,root,k):
        visited = 0
        lastValue = -1
        self.reverseInOrder(root,visited,lastValue,k)
        return lastValue
    
    def reverseInOrder(self,root,visited,lastValue,k):
            if(root==None or visited>=k):
                return
            
            self.reverseInOrder(root.right,visited,lastValue,k)
            if(visited<k):
                lastValue = root.value
                visited+=1
                self.reverseInOrder(root.left,visited,lastValue,k)

if __name__=='__main__':
    root = Node(15)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.left.left.left = Node(1)
    root.left.left.right = Node(3)
    root.right = Node(20)
    root.right.left = Node(17)
    root.right.right = Node(22)

    s = Solution()
    result = s.kthLargetsNode(root,3)
    print(result)