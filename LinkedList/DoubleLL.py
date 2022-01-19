class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def setHead(self,node):
        if(self.head):
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
    
    def setTail(self,node):
        currNode = self.head
        while(currNode):
            if(currNode.value==node.value):
                self.tail = node
                break
            currNode = currNode.next

    def insertBefore(self, node, nodeToInsert):
        if(self.head):
            currNode = self.head
            while(currNode):
                if(currNode.value==node.value):
                    temp = currNode.prev
                    temp.next = nodeToInsert
                    nodeToInsert.prev = temp
                    nodeToInsert.next = currNode
                    currNode.prev = nodeToInsert
                    break
                currNode = currNode.next
        else:
            self.setHead(nodeToInsert)

    def insertAfter(self, node, nodeToInsert):
        if(self.head):
            currNode = self.head
            while(currNode):
                if(currNode.value==node.value):
                    temp = currNode.prev
                    temp.next = nodeToInsert
                    nodeToInsert.prev = temp
                    nodeToInsert.next = currNode
                    currNode.prev = nodeToInsert
                    break
                currNode = currNode.next
        else:
            self.setTail(nodeToInsert)
    


