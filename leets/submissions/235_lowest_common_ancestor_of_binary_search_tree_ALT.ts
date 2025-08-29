import { TreeNode } from "./types/TreeNode";

/*
     _____  .____  ___________
    /  _  \ |    | \__    ___/
   /  /_\  \|    |   |    |
  /    |    \    |___|    |
  \____|__  /_______ \____|
          \/        \/

  THIS IS AN ALT SOLUTION
  Where I assumed 'lowest' meant smallest TreeNode.val instead of the deepest common ancestor
*/

type ancestors = {
  isFoundTarget: boolean;
  ancestors: TreeNode[];
};

/**
 * BIG-O:
 *  TIME: O(n)
 *  MEMORY: O(n)
 *    Worst-case the tree is skewed (height = n items), the number of function calls on the stack grows
 *
 * Solution w thoughts 💭
 *  #easy #binary-search-trees
 */
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
  const pAncestors = dfs(root, p).ancestors;
  const qAncestors = dfs(root, q).ancestors;

  // Intersect ancestors
  // .filter(.includes) is O(n^2)
  // To avoid O(n^2), convert one list to a set (separate O(n))
  // .filter(.has) is now O(n)
  const pAncestorsSet = new Set(pAncestors);
  const intersect = qAncestors.filter((a) => pAncestorsSet.has(a));

  // Final O(n) to locate the smallest
  let min: TreeNode | null = null;
  for (const ancestor of intersect) {
    if (!min) min = ancestor;
    if (ancestor.val < min.val) min = ancestor;
  }

  return min;
}

// To determine if 2 nodes have common ancestors (to cherry-pick lowest)
//  we need 2 lists of ancestors
// Use DFS to find the target, then collect ancestors when bubbling-up (stop traversing)
// Ancestors are inclusive (count curr node)
function dfs(node: TreeNode | null, target: TreeNode | null): ancestors {
  const notFoundRes = { isFoundTarget: false, ancestors: [] };
  if (!node) return notFoundRes;
  if (node === target) return { isFoundTarget: true, ancestors: [node] };

  const l = dfs(node.left, target);
  const r = dfs(node.right, target);

  if (l.isFoundTarget) {
    l.ancestors.push(node);
    return l;
  }

  if (r.isFoundTarget) {
    r.ancestors.push(node);
    return r;
  }

  return notFoundRes;
}
