# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#           preorder=[1,2,3,4]
#           inorder=[2,1,3,4]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        leftLen = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:leftLen+1], inorder[:leftLen])    # preorder: skip root with 1. From there we want all amount of left nodes, so leftLen + 1 (end index non inclusive)
                                                                                # inorder: all leftnodes until root non-inclusive
        root.right = self.buildTree(preorder[1+leftLen:], inorder[leftLen+1:])  # preorder: skip root with 1, +leftLen skips rest of leftnodes. 
                                                                                # With 0 index, that marks start of right.
                                                                                # Inorder: leftLen is all leftnodes + root, +1 starts at first right node.

        return root


