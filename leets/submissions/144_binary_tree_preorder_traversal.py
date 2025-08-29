from typing import List, Optional
from leets.types.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Same as 94_binary_tree_inorder_traversal but order of traversal (when we capture the node) is different

        ##dfs ##bst ##recursion
        """
        result: List[int] = []
        visited: List[TreeNode] = []

        def dfs(node: Optional[TreeNode]):
            if not node or node in visited:
                return
            result.append(node.val)
            visited.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result