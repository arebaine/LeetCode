# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node):
            if node is None:
                return set()
            if not node.left and not node.right:
                return set([node.val])
            else:
                return {x + node.val for x in dfs(node.left)} | {x + node.val for x in dfs(node.right)}
        if targetSum in dfs(root):
            return True
        return False
