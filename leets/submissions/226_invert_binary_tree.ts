import { TreeNode } from "../types/TreeNode";

/**
 * BIG-O:
 *  TIME: O(n)
 *  MEMORY: TODO
 *
 * Solution w thoughts 💭
 *  #easy #binary-tree #queues
 */
function invertTree_using_BFS(root: TreeNode | null): TreeNode | null {
  if (!root) return null;
  const res = root; // the root remains the same after inversion

  // BFS will visit the 2 nodes we want to swap at a time
  // Use a pointer 'front' to avoid dequeing, just shifting the index
  let front = 0;
  const queue: TreeNode[] = [root];

  while (front < queue.length) {
    const node = queue[front]; // dequeue
    if (!node) break;

    // Swap the children of the node
    const temp = node.left;
    node.left = node.right;
    node.right = temp;

    // Go again
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
    front++;
  }

  return res;
}

/**
 * BIG-O: O(n) time
 *  Solution w thoughts 💭
 *  #easy #binary-tree #queues
 */
function invertTree_using_DFS(root: TreeNode | null): TreeNode | null {
  if (!root) return null;

  const dfs = (node: TreeNode | null): void => {
    if (!node) return;
    // Swap
    const temp = node.left;
    node.left = node.right;
    node.right = temp;
    dfs(node.left);
    dfs(node.right);
  };

  dfs(root);
  return root;
}
