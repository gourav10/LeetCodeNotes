from _typeshed import Self


class ListNode:
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next

    def getValue(self):
        return self.val
    
    def getNextNode(self):
        return self.next