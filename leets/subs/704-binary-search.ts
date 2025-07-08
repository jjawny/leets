/**
 * TIME: Worst-case O(log n) because each loop halves the remaining problem size
 * MEMORY: Worst-case O(1) since we only use 2 pointers and everything else is destroyed after each loop (no bundling)
 *
 * #sliding-window #two-pointers #binary-search
 */
function search(nums: number[], target: number): number {
  // 1. Create a window using 2 pointers (num indexes)
  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while (leftIdx <= rightIdx) {
    // 2. Calc the next middle index
    //    We need to find amount halfway between left and right
    //    So focusing on right (example: 8), remove the left portion (example: 4)
    //    So the amount inbetween is right - left = 4
    //    Then divide by 2 to get the halfway amount
    const amountHalfwayBetweenLeftAndRight = Math.floor((rightIdx - leftIdx) / 2);
    //    Then apply it starting from the left (to get the true middle)
    const midIdx = leftIdx + amountHalfwayBetweenLeftAndRight;

    // 3. Check if the middle num is the target (HIT!)
    const midNum = nums[midIdx];

    if (target === midNum) return midIdx;
    // Miss? adjust the window to the left or right:
    // - target < midNum? move the right pointer to the middle (-1 to exclude middle)
    // - target > midNum? move the left pointer to the middle (+1 to exclude middle)
    else if (target < midNum) rightIdx = midIdx - 1;
    else if (target > midNum) leftIdx = midIdx + 1;
  }

  return -1; // MISS!
}
