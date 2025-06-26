# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traversal(node):
            if not node:
                return []
            return [node] + traversal(node.left) + traversal(node.right)
        trav = traversal(root)
        for i in range(len(trav) -1):
            node = trav[i]
            node.left = None
            node.right = trav[i+1]
