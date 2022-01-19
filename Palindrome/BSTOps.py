class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    


class BST:
    def __init__(self,root) -> None:
        self.root = root

    def insert(self,val):
        node = Node(val)
        if(self.root==None):
            self.root = node

        currNode = self.root
        while(True):    
            if(currNode.value >= val):
                if(currNode.left):
                    currNode = currNode.left
                else:
                    currNode.left = node
                    break

            elif(currNode.value < val):
                if(currNode.right):
                    currNode = currNode.right
                else:
                    currNode = node
                    break
            return self.root
    
    def contains(self,key):
        currNode = self.root
        while(currNode):
            if(key==currNode.value):
                return True
            elif(key > currNode.value):
                currNode = currNode.right
            else:
                currNode = currNode.left
        return False

    def getMinValue(self,root):
        currNode = root
        while currNode.left:
            currNode = currNode.left
        return currNode

    def remove(self,key, parentNode = None):
        currNode = self.root
        while(currNode):
            if(key==currNode.value):
                if(currNode.left and currNode.right):
                    currNode.value = self.getMinValue(currNode.right)
                    self.remove(currNode.value,currNode)
                elif(parentNode==None):
                    if currNode.left:
                        currNode.value = currNode.left.value
                        currNode.right = currNode.left.right
                        currNode.left = currNode.left.left
                    elif currNode.right:
                        currNode.value = currNode.right.value
                        currNode.left = currNode.right.left
                        currNode.right = currNode.right.right
                    else:
                        currNode.value = None
                    break
                elif(parentNode.left == currNode):
                    if currNode.left:
                        parentNode.left = currNode.left
                    else:
                        parentNode.left = currNode.right
                elif(parentNode.right==currNode):
                    if(currNode.left):
                        parentNode.right = currNode.left
                    else:
                        parentNode.right = currNode.right

            elif(key > currNode.value):
                parentNode = currNode
                currNode = currNode.right
            else:
                parentNode = currNode
                currNode = currNode.left
        return self.root


            

        
            

