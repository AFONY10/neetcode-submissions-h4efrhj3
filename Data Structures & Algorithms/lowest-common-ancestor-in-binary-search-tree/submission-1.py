# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        if not curr or not p or not q:
            return None
        # If we're in ride side
        if p.val > curr.val and q.val > curr.val:
            return self.lowestCommonAncestor(curr.right, p, q)
        # If we're in left side
        elif p.val < curr.val and q.val < curr.val:
            return self.lowestCommonAncestor(curr.left, p, q)
        else:
            return curr
        