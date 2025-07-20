from typing import List, Optional
from leets.types.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        TIME: O(n) as we visit each node
        MEMORY: O(n) as we capture all nodes again in the result (and visited)

        ##dfs ##bst ##recursion
        """
        # Qs is basically just the DFS template (recursion strat)
        result: List[int] = []
        visited: List[TreeNode] = []

        def dfs(node: Optional[TreeNode]):
            if not node or node in visited:
                return
            visited.append(node)
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)

        return result
