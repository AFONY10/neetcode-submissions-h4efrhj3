# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeStack = []
        for linkedList in lists:
            curr = linkedList
            while curr:
                nodeStack.append(curr.val)
                curr = curr.next
        nodeStack.sort(reverse = True, key = lambda node:node)

        dummy = ListNode(0)
        curr = dummy
        while nodeStack:
            nxt = ListNode(nodeStack.pop())
            curr.next = nxt
            curr = nxt
        return dummy.next