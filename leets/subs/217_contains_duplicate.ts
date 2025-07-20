/**
 * BIG-O: O(n)
 *  Solution w thoughts 💭
 *  #easy #set
 */
function containsDuplicate(nums: number[]): boolean {
  const seenNumsSet = new Set<number>();
  for (const num of nums) {
    if (seenNumsSet.has(num)) return true;
    seenNumsSet.add(num);
  }
  return false;
}
