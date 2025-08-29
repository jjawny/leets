/**
 * BIG-O: O(n) time where n = number of steps...
 *  ...as any duplicate recursions using the same number of remaining steps are returned immediately (does not branch)...
 *  ...the cache is passed by ref so available at any point of the tree
 *  Solution w thoughts 💭
 *  #easy #dynamic-programming #recursion
 */
function climbStairs(n: number): number {
  // To avoid an exponential O(2^n) timeout
  //  We can avoid extra recursion calls if a path is already calculated
  //  Example given 5 steps:
  //      - Branches off to 2 recursions (4 steps left & 3 steps left)
  //      - These paths will eventually calculate the same remaining steps
  //          4 steps left? calc 3 steps and 2 steps
  //          3 steps left? calc 1 steps and 2 steps
  //      - And here's the problem ----------^
  //      - So cache this result and let subsequent recursions read from the cache
  //          we branch out (only returning a count when we reached the top, forgetting the cache)
  const cache: number[] = Array(n + 1).fill(-1);
  return getNextPossiblePath(n, cache);
}

function getNextPossiblePath(remainingSteps: number, cache: number[]): number {
  if (remainingSteps < 0) return 0; // safety
  const isReachedTheTop = remainingSteps === 0;
  if (isReachedTheTop) return 1; // completed 1 possible path

  // Cache hit!
  if (cache[remainingSteps] !== -1) return cache[remainingSteps]; // number of possible branches from here were already calculated, return early

  // Cache miss!
  let count = 0; // number of sub-branches/paths that reached the top
  count += getNextPossiblePath(remainingSteps - 1, cache); // branch off to an alt path
  count += getNextPossiblePath(remainingSteps - 2, cache); // branch off to an alt path
  cache[remainingSteps] = count;
  return count;
}
