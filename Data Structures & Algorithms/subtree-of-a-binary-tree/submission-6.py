# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        def dfsCompare(curr, comparable):
            if not curr and not comparable:
                return True
            if not curr or not comparable:
                return False
            if curr.val != comparable.val:
                return False
            
            left = dfsCompare(curr.left, comparable.left)
            right = dfsCompare(curr.right, comparable.right)
            
            return left and right
        
        if dfsCompare(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right