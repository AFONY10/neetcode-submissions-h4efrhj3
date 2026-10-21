# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfsCompute(node):
            if not node:
                return 0
            
            leftPath = dfsCompute(node.left)
            rightPath = dfsCompute(node.right)

            # Compute maxPath from both left and right paths combined
            leftMax = max(leftPath, 0)
            rightMax = max(rightPath, 0)
          
            maxPath = node.val + leftMax + rightMax
            if maxPath > self.res:
                self.res = maxPath
            
            return max(node.val + leftMax, node.val + rightMax)
        
        dfsCompute(root)

        return self.res