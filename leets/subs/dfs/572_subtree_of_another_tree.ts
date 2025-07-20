import { TreeNode } from "../../types/TreeNode";

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/**
 * BIG O: Where n is root's nodes and m is subRoot's nodes
 * TIME: Worst-case O(n) for the BFS algo alone, but O(n * m) if including `isEqualViaDfs`
 *        as we could potentially perform a full DFS (checking for equality) on every node
 *        during the BFS (assuming they all fail the equality check)
 * MEMORY: Worst-case O(n + m)for the 2 recursion function calls (on the stack) when both trees are skewed
 *
 * ##bfs ##dfs ##bst
 */
function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (!root || !subRoot) return false;

  // 1. Start with BFS on main tree's root
  let front = 0;
  const queue: (TreeNode | null)[] = [root];

  while (front < queue.length) {
    const currNode = queue[front];
    if (!currNode) continue;

    // 2. If main tree's current node matches the subRoot node,
    //    we should start checking for equality, answering
    //    "does the current subtree inside main tree === subRoot's tree?"
    const isEqual =
      currNode.val === subRoot.val && isEqualViaDfs(currNode, subRoot);
    if (isEqual) return true;

    // 3. Continue BFS traversal if not equal
    if (currNode.left) queue.push(currNode.left);
    if (currNode.right) queue.push(currNode.right);
    front++;
  }

  return false;
}

// We need a way to compare equality, we can use DFS upon both trees
function isEqualViaDfs(a: TreeNode | null, b: TreeNode | null): boolean {
  if (!a && !b) return true;
  if (!a || !b || a.val !== b.val) return false;
  return isEqualViaDfs(a.left, b.left) && isEqualViaDfs(a.right, b.right);
}
