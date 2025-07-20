import { TreeNode } from "./types/TreeNode";

/**
 * BIG-O:
 *  TIME: O(n)
 *    Worst-case the tree is skewed (height = n items) and p&q are the same leaf node (aka the tree is just a linked list)
 *  MEMORY: O(1)
 *    No extra DS are needed
 *
 * Solution w thoughts 💭
 *  #easy #binary-search-trees
 */
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
  if (!p || !q) return null;

  // Guarenteed p & q exist
  // Hints that we don't need to traverse all the way to them each...
  // Since this is a BST (ordered) we know the path to take
  let curr = root;
  while (curr) {
    // Example:
    //  If p is found but q is a child? p is the lowest common ancestor
    if (curr.val === p.val) return p;
    if (curr.val === q.val) return q;

    // The lowest common ancestor will be the node we have to split from when traversing to p & q
    // ∴ we can stop at the split as subtrees won't have anything else in common deeper
    const l = curr.left;
    const r = curr.right;
    const nextJumpForP = p.val < curr.val ? l : r;
    const nextJumpForQ = q.val < curr.val ? l : r;
    const isSplitting = nextJumpForP !== nextJumpForQ;
    if (isSplitting) return curr;
    curr = nextJumpForP; // or Q as they are the same node
  }

  return curr;
}
