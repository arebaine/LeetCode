# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth_fn(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            else:
                return 1 + max(depth_fn(node.left), depth_fn(node.right))
        def balanced(node):
            if node is None:
                return True
            return abs(depth_fn(node.left) - depth_fn(node.right)) <= 1 and balanced(node.left) and balanced(node.right)
        return balanced(root)