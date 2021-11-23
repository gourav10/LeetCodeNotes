from typing import Optional, Sized


class ListNode:
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next

    def getValue(self):
        return self.val
    
    def getNextNode(self):
        return self.next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if(head==None): return None
        
        
        if(head.val==val):
            curr = head
            head = None
            head = curr.next
        
        prev = None
        curr = head
        while(curr):
            if(curr.val == val):
                if(not curr.next):
                    prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head


if __name__=="__main__":
    head = ListNode(7)
    head.next = ListNode(7)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(7)
    k = 7
    print("Input:")
    curr = head
    result = ""
    while(curr):
        result +=str(curr.val)
        if curr.next:
            result+= " -> "
        curr = curr.next
    print(result)
    s = Solution()
    curr = s.removeElements(head,7)
    result=""
    while(curr):
        result +=str(curr.val)
        if curr.next:
            print(" -> ")
        curr = curr.next
    print(result)
    
