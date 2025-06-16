# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return []
            if (not node.left) and (not node.right):
                return [node.val]
            else:
                return dfs(node.left) + [node.val] + dfs(node.right)
        traversal = dfs(root)
        n = len(traversal)
        for i in range(n-1):
            if traversal[i] >= traversal[i+1]:
                return False
        return True   
