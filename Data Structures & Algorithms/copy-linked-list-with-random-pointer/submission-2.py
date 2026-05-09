"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Making Hashmap with original (ket) to copy (value)
        originalToCopy = {None : None}  # When iterating through nodes, 
                                        # we wont be finding Null nodes, 
                                        # so we  manually add to dict
        
        # Append just nodes to hashmap
        curr = head
        while curr:
            copy = Node(curr.val)
            originalToCopy[curr] = copy
            curr = curr.next
        
        # Assign pointer values for each copy in hashmap
        curr = head
        while curr:
            copy = originalToCopy[curr]
            copy.next = originalToCopy[curr.next]
            copy.random = originalToCopy[curr.random]
            curr = curr.next
        
        return originalToCopy[head]
