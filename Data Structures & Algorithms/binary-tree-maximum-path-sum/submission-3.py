# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfsMaxODP(currNode):
            if not currNode:
                return 0

            left = dfsMaxODP(currNode.left)
            right = dfsMaxODP(currNode.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            # Calculate max with two split
            self.res = max(self.res, currNode.val+left+right)
           
           # Return max one split from currNode
            return currNode.val + max(left, right, 0)
        
        dfsMaxODP(root)

        return self.res