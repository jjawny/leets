from collections import deque
from typing import List
from leets.types.tree_node import TreeNode

def bfs_on_trees(root) -> List[int]:
  result = []
  queue = deque([root])
        
  while queue:
      curr_node: TreeNode = queue.popleft() # dequeue
      result.append(curr_node.val)

      if curr_node.left:
          queue.append(curr_node.left)
      if curr_node.right:
          queue.append(curr_node.right)
  return result
    