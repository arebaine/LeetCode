# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(left, right):
            if left is not None and right is not None:
                if left.val == right.val:
                    return sym(left.right, right.left) and sym(left.left, right.right)
                else:
                    return False
            if (left is None and right is not None) or (right is None and left is not None):
                return False
            if left is None and right is None:
                return True
        return sym(root.left, root.right)