import { TreeNode } from "./types/TreeNode";

/**
 * BIG-O:
 *  TIME: O(n)
 *    Worst-case tree is balanced ∴ we traversed all elements in DFS
 *  MEMORY: O(n)
 *    Worst-case tree is skewed (height = number of n elements)
 *    Memory here is the number of function calls on the stack
 *
 * Solution w thoughts 💭
 *  #easy #binary-trees #recursion
 */
function isBalanced(root: TreeNode | null): boolean {
  // We are measuring depth so use DFS
  const isSubtreesHeightBalanced = dfs(root) !== -1;
  return isSubtreesHeightBalanced;
}

/**
 * DFS
 * Counts the height/depth
 * At each iteration, we check the subtree's left and right depths
 * If NOT height-balanced, we fail immediately (res -1)
 * If all height-balanced, we finally return the max height (0+)
 */
function dfs(node: TreeNode | null): number {
  if (!node) return 0; // reached bottom
  const lDepth = dfs(node.left);
  const rDepth = dfs(node.right);

  if (lDepth === -1 || rDepth === -1) return -1; // Already marked as invalid, bubble-up immediately

  const isSubtreesHeightBalanced = Math.abs(lDepth - rDepth) <= 1; // "height-balanced" means depths are equal or 1 off
  if (!isSubtreesHeightBalanced) return -1;

  // We take the max depth
  // +1 to increment current depth
  return Math.max(lDepth, rDepth) + 1;
}
