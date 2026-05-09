# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##### Example ####
# Input:  2 -> 4 -> 6 -> 8
# Output: 2 -> 8 -> 4 -> 6

# Fast and slow pointer to cut halves and reverse 2nd half
# 2 -> 4 | 6 -> 8
# 2 -> 4 | 6 <- 8

# Merge two halves with 2 pointers:
# 1. halve1.curr -> halve2.curr -> halve1.next -> halve2.next etc.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next, prev = None, None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # Merge two halves with 2 pointers:
#       1. first->second->first.next->second.next->
        firstP = head
        secondP = prev
        while secondP:
            firstNxtP = firstP.next
            secondNxtP = secondP.next
            firstP.next = secondP
            secondP.next = firstNxtP
            firstP = firstNxtP
            secondP = secondNxtP



