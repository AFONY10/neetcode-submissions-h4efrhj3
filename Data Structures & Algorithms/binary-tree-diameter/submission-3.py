# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfsMaxHeight(root):
            if root == None:
                return 0

            leftHeight = dfsMaxHeight(root.left)
            rightHeight = dfsMaxHeight(root.right)
            self.res = max(self.res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        dfsMaxHeight(root)

        return self.res