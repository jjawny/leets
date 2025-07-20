from collections import deque
from typing import Optional
from leets.types.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        BIG O: Where n is root's nodes and m is subRoot's nodes
        TIME: Worst-case O(n) for the BFS algo alone, but O(n * m) if including `isMatchingTrees`
              as we could potentially perform a full DFS (checking for equality) on every node
              during the BFS (assuming they all fail the equality check)
        MEMORY: Worst-case O(n + m)for the 2 recursion function calls (on the stack) when both trees are skewed
        """
        if not root or not subRoot:
            return False
        
        queue = deque([root])
        
        # 1. BFS the main tree until there's a match on sub tree's root node
        while queue:
            curr_node = queue.popleft()
            # We don't need to capture the curr_node here (save mem)
            # We DO need to check for equality if curr_node is also the sub tree's root node
            is_matching_roots = curr_node.val == subRoot.val
            if is_matching_roots and isMatchingTrees(curr_node, subRoot):
                    return True

            # Reminder BFS is left -> right, progress a level deeper, repeat
            # So we will process: 3, 4, 5, then 1
            #        (3)
            #      (4) (5)
            #    (1)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return False
            
def isMatchingTrees(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    # 2. The check can be either BFS or DFS (using DFS here)
    #    Traversing the trees at the same time
    #    Fail anytime nodes do not match
    #    Success by default
    if not a and not b:
        return True
    if not a or not b or a.val != b.val:
        return False
    return isMatchingTrees(a.left, b.left) and isMatchingTrees(a.right, b.right)