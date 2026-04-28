# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.trueFalse = set()
        
        def dfsHeight(curr):
            if not curr:
                return 0
            
            left = dfsHeight(curr.left)
            right = dfsHeight(curr.right)
            if abs(left-right) > 1:
                self.trueFalse.add(0)
            
            return 1 + max(left, right)
        
        dfsHeight(root)

        if 0 in self.trueFalse:
            return False
        else:
            return True
            

        
