# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        previous, first, second = None, None, None

        def dfs(node):
            nonlocal previous, first, second
            if not node:
                return
            dfs(node.left)
            if previous and previous.val > node.val:
                if not first:
                    first = previous
                second = node
            previous = node
            dfs(node.right)

        dfs(root)
        if first and second:
            first.val, second.val = second.val, first.val
