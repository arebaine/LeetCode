# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node, res):
            if node is not None:
                if node.left is not None:
                    bfs(node.left, res)
                res.append(node.val)
                if node.right is not None:
                    bfs(node.right, res)
        res = []
        bfs(root, res)
        return res