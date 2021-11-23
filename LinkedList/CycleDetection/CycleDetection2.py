from Util.ListNode import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast = head,head
        cycleDetected = False
        if head==None:
            return None
        
        if head.next==None:
            return None
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                cycleDetected = True
                break

        if cycleDetected==False:
            return None
        
        slow = head
        while slow and fast:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
        return None