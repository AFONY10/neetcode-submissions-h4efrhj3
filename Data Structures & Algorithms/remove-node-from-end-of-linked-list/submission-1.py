class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Reverse the list
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 2. Remove Nth element from end
        reversed_head = prev
        curr = reversed_head
        count = 1
        prev = None

        while curr:
            if count == n:
                temp = curr.next
                curr.next = None

                if prev:
                    prev.next = temp
                else:
                    reversed_head = temp

                break

            prev = curr
            curr = curr.next
            count += 1

        # 3. Reverse the list back to original
        curr = reversed_head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev