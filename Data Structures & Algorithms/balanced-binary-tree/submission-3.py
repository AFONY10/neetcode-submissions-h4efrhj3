# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsHeight(root):
            if root == None:
                return [True, 0]
            
            lHeight = dfsHeight(root.left)
            rHeight = dfsHeight(root.right)

            balanced = lHeight[0] and rHeight[0] and abs(lHeight[1] - rHeight[1]) <= 1
               
            
            return [balanced, 1 + max(lHeight[1], rHeight[1])]
        
        return dfsHeight(root)[0]