# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        def dfsTraversal(curr, res):
            if not curr:
                return
            
            dfsTraversal(curr.left, res)
            res.append(curr.val)
            dfsTraversal(curr.right, res)
        dfsTraversal(root, self.res)
        print(self.res)

        return self.res[k-1]