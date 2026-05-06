class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases
        if not subRoot:
            return True   # empty tree is always a subtree
        
        if not root:
            return False  # no place left to search
        
        # Helper function to compare the trees starting from given roots
        def dfsCompare(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False
            
            return dfsCompare(root1.left, root2.left) and dfsCompare(root1.right, root2.right)

        if dfsCompare(root, subRoot):
            return True
        
        # Recursive Case
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)