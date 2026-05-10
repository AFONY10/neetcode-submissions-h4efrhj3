# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper functions for sub problems
        def reverseList(newHead):
            curr = newHead
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev

        def findPartition(currList, k):
            if not currList:
                return None, None
            count = 1
            curr = currList
            while curr:
                if count == k:
                    nxt = curr.next
                    curr.next = None
                    newHead = nxt
                    return currList, newHead
                curr = curr.next
                count = count + 1
            
            return currList, None
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            currentPartition, newCurr = findPartition(curr.next, k)

            # Checking the partition we got returned by function, 
            # does it need to be reversed or is amount of nodes less than k?
            check = currentPartition
            count = 0
            while check:
                count += 1
                check = check.next
            if count < k:
                curr.next = currentPartition
                break
            
            
            group_tail = currentPartition
            reversed_head = reverseList(currentPartition)
            curr.next = reversed_head
            group_tail.next = newCurr
            curr = group_tail   
        return dummy.next   







