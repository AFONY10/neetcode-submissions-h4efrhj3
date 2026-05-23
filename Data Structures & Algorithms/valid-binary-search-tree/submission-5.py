# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsValid(node, leftBoundary, rightBoundary):
            if not node:
                return True
            
            if not (node.val < rightBoundary and node.val > leftBoundary):
                return False
            
            return dfsValid(node.left, leftBoundary, node.val) and dfsValid(node.right, node.val, rightBoundary)

        return dfsValid(root, float('-inf'), float('inf'))