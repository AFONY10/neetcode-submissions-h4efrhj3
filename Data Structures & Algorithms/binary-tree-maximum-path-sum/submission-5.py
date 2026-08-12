# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            # Checking values gained from far left and right (leaf nodes)
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # If leaf-nodes are negative, we dont want to count them, and so theyre initilized to 0
            if leftMax < 0:
                leftMax = 0
            if rightMax < 0:
                rightMax = 0
            
            # Computing max to update res by including split
            self.res = max(self.res, root.val + leftMax + rightMax)
            print(self.res)

            # Return max path with no split so it can be used for another split
            return root.val + max(leftMax, rightMax, 0)
        
        dfs(root)
        return self.res
            


