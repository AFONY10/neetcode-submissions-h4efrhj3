# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find mid-way
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse second-half
        second = slow.next      # Node after slow is beginning of 2nd half
        slow.next = None        # Breaking the link between 1st and 2nd half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # After this loop, prev stores the end of 2nd half (check reverse linkedlist problem)

        # 3. Merge the two halves
        first = head # =Leftpointer
        second = prev # =Rightpointer
        while second:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        
        # No need to assign tail to null pointer here, 
        # because we already did that during reverse


            

        