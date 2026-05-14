# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = [True, 0]

        def dfsHeight(curr):
            if curr == None:
                return [True, 0]
            
            left = dfsHeight(curr.left)
            right = dfsHeight(curr.right)

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                self.balanced = [True, 1 + max(left[1], right[1])]
            else:
                self.balanced = [False, 1 + max(left[1], right[1])]
                
            return self.balanced
        
        return dfsHeight(root)[0]
