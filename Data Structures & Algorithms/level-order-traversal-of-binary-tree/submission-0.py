# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#   [1, 2, 3, 4, 5, 6 , 7]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            currentRes = []
            for i in range(len(queue)):
                currNode = queue.popleft()
                if currNode:
                    queue.append(currNode.left)
                    queue.append(currNode.right)
                    currentRes.append(currNode.val)
            if currentRes:
                res.append(currentRes)
        
        return res

         


            

