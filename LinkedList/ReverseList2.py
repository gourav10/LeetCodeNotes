from typing import Optional

class ListNode:
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next

    def getValue(self):
        return self.val
    
    def getNextNode(self):
        return self.next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        if left == right:
            for i in range(left):
                curr = curr.next
            return curr.val
        
        curr = head
        leftNode = head
        for i in range(left):
            leftNode = leftNode.next
            curr = curr.next
    
        stack = []
        while(left<=right):
            stack.append(leftNode.val)
            left+=1
            leftNode = leftNode.next

        while(stack):
            curr.val = stack.pop()
            curr = curr.next

        return head

if __name__=="__main__":
    head = ListNode(5)
    head.next = ListNode(7)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(9)
    head.next.next.next.next = ListNode(1)
    left =  2
    right = 4
    print("Original List:")
    while(head):
        print(head.val)
        head=head.next

    s = Solution()
    head = s.reverseBetween(head,left,right)
    print("After Reverser Operation, List:")
    while(head):
        print(head.val)
        head=head.next

            
        
        
        



