# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [[node.val]]
            node_path = []
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            for path in left_path + right_path:
                node_path.append([node.val] + path)
            return node_path
        root_path = dfs(root)
        valid_path = []
        for path in root_path:
            if sum(path) == targetSum:
                valid_path.append(path)
        return valid_path
