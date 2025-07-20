/**
 * Run through (see "x"s) using twoSum([2,7,11,15], 9)
 *
 * TIME: Worst-case O(n) when we loop through all nums
 * MEMORY: Worst-case O(1) when we add every number to the cache
 *
 * ##hashmaps
 */
function twoSum(nums: number[], target: number): number[] {
  if (nums.length === 0) return [];

  // 2. Instead of using a nested loop to compare values, check a fast cache
  //    Fast cache = hashmap w O(1) ops
  //    KV = <num, index>, why? we know the diffs to lookup, and want the index back
  const cache = new Map<number, number>();

  // 1. We will need to loop over nums at least once
  for (let i = 0; i < nums.length; i++) {
    // 3. Check the cache if the desired num exists/his index
    const num = nums[i]; // x 2nd iteration, num = 7
    const diff = target - num; // x 9 - 7 = 2
    const diffIndex = cache.get(diff); // x by 2nd iteration, cache has num '2' at pos 0
    if (diffIndex !== undefined) {
      // x diffIndex is valid but 0, so don't use falsey check
      return [i, diffIndex]; // x return [0,1]
    }

    // 4. No match? save in cache for future iterations to lookip
    cache.set(num, i);
  }

  // 5. No matches
  return [];
}
