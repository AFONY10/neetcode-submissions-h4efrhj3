# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            dummy = ListNode(0)
            tail = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                
                tail = tail.next # Iteration point
            
            # Attach rest of list 1 or 2, if they are different sizes during merge
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

            return dummy.next
        n = len(lists)
        for i in range(1, n):
            lists[i] = merge2Lists(lists[i-1],lists[i])

        return lists[n-1] if lists else None
