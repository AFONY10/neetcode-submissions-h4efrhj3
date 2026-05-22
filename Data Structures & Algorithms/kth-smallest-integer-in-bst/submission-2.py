# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []

        def dfsInOrderTraversal(node, resList):
            if not node:
                return
            
            dfsInOrderTraversal(node.left, resList)
            resList.append(node.val)
            dfsInOrderTraversal(node.right, resList)
        
        dfsInOrderTraversal(root, self.res)

        return self.res[k-1]