# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
[ 1, 2, 3]
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfsPostorder(node):
            if not node:
                return 0
            
            leftMax = dfsPostorder(node.left)
            rightMax = dfsPostorder(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # Compute result in root, with split
            self.res = max(self.res, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        dfsPostorder(root)

        return self.res