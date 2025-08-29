/**
 * BIG-O: O(n) time
 *  Solution w thoughts 💭
 *  #easy #arrays
 */
function findDisappearedNumbers(nums: number[]): number[] {
  // O(n) use originally solution from 'Missing Number'
  const n = nums.length;
  const offsetStartingIndexBy = 1; // ignore 0th index
  const tracker = new Array(n + offsetStartingIndexBy);
  for (let i = 0; i < n; i++) {
    tracker[nums[i]] = true; // found
  }

  // O(n) return the missing ones
  const res: number[] = [];
  for (let i = offsetStartingIndexBy; i < tracker.length; i++) {
    const isMissing = !tracker[i];
    console.log(`Is ${i} missing? ${isMissing}`);
    if (isMissing) res.push(i);
  }

  return res;
}
