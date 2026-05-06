class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfsCompare(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False
            
            left = dfsCompare(root1.left, root2.left)
            right = dfsCompare(root1.right, root2.right)

            return left and right

        if not root:
            return False
        
        if dfsCompare(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)