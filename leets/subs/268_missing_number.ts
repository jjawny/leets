/**
 * BIG-O:
 *  TIME: O(n)
 *    1x while loop
 *  MEMORY: O(1)
 *    1x int used to track
 *
 * Solution w thoughts 💭
 *  #easy #arrays
 */
function missingNumber(nums: number[]): number {
  const n = nums.length;

  // SOLUTION 1 = O(n) + O(n) = O(n)
  //  In both solutions we need something to track nums/find the missing num
  //  Since we know n upfront, create an array (O(1)) w empty slots (the indexes are useful)
  //  Offset by 1 since we don't count 0
  // const foundNums = new Array(n + 1);
  // for (const num of nums) foundNums[num] = true;
  // for (let i = 1; i <= n; i++) {
  //     const isMissing = !foundNums[i];
  //     if (isMissing) return i;
  // }

  // SOLUTION 2 = O(n)
  //  Remove one of the O(n) traversals by using the sum (which we know upfront)
  let sum = (n * (n + 1)) / 2;
  for (const num of nums) {
    sum -= num;
  }
  return sum;

  return 0;
}
