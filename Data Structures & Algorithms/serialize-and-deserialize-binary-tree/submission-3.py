# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.values = []

        def dfs(node):
            if not node:
                self.values.append("Null")
            else:
                self.values.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(self.values)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.values = data.split(",")
        self.i = 0
        def dfs():
            if self.values[self.i] == "Null":
                self.i += 1
                return None
            node = TreeNode(int(self.values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()



