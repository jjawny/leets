/**
 * BIG-O:
 *  TIME: O(n)
 *    1x for loop
 *  MEMORY: O(1)
 *    1x int used to track
 *
 * Solution w thoughts 💭
 *  #easy #bit-manipulation
 */
function singleNumber(nums: number[]): number {
  // MUST:
  //  O(n) time = 1 loop
  //  O(1) Space = somehow use a number to track progress

  // If we could use O(n) space, use a set (add/remove/add/remove...)
  //  any remaining items were found once (added but not removed)

  // To achieve O(1) space
  //  track progress in a sum and use O(1) ops (arithmetic/bitwise)
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum ^= nums[i]; // do a XOR to toggle each bit a.k.a each num
  }
  return sum;
}
