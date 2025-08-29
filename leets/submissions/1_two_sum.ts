/**
 * TIME: Worst-case O(n) when we loop through all nums
 * MEMORY: Worst-case O(n) when we add all nums to the cache
 *
 * ##hashmaps
 */
function twoSum(nums: number[], target: number): number[] {
  if (nums.length === 0) return [];

  // 2. Instead of using a nested loop to compare values, check a cache (hashmap)
  //    Keys are the nums, values are the indexes, why? we have the diffs ready for lookups and want the index back
  const cache = new Map<number, number>();

  // 1. We will need to loop over all nums at least once
  for (let i = 0; i < nums.length; i++) {
    // 3. Check the cache if the desired num exists/his index
    const num = nums[i];
    const diff = target - num;
    const diffIndex = cache.get(diff);
    if (diffIndex !== undefined) {
      return [i, diffIndex];
    }

    // 4. No match? cache for future iterations
    cache.set(num, i);
  }

  // 5. No matches
  return [];
}
