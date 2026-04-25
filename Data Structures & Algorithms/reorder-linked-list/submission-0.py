class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        lp = 0
        rp = len(nodes) - 1

        dummy = ListNode(0)
        tail = dummy

        while lp <= rp:
            if lp == rp:
                tail.next = nodes[lp]
                tail = tail.next
            else:
                tail.next = nodes[lp]
                tail = tail.next

                tail.next = nodes[rp]
                tail = tail.next

            lp += 1
            rp -= 1

        tail.next = None