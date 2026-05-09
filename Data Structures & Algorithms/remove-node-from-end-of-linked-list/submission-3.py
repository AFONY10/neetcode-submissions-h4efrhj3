# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]
#   reverse linked list 
#       1->2->3->4
#       4->3->2->1 
#   remove nth element from reversed list
#       4->2->1 
#   Reverse back
#       1->2->4 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        revHead = prev
        curr = revHead
        prev = None
        visitedCounter = 1
        while curr:
            if visitedCounter == n:
                if prev:
                    prev.next = curr.next
                else:
                    revHead = curr.next
                curr.next = None
                curr = nxt
                break
            prev = curr
            curr = curr.next
            visitedCounter += 1
        
        curr = revHead
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev


            

        