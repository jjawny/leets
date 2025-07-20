/**
 * BIG-O:
 *  TIME: O(n) + O(n/2) = O(n)
 *    1x for loop to transform the input, 1x while loop to compare using a shrinking window
 *  MEMORY: O(n)
 *    Worse-case entire input is valid
 *
 * Solution w thoughts 💭
 *  #easy #arrays #sliding-windows
 */
function isPalindrome(s: string): boolean {
  // Faster/simpler to assume true and fail immediately
  // Transformation required:
  //  - alpha numeric
  //  - lowercase

  // The chars before transformation affect the window lengths
  // O(n) to create the new array, don't bother converting back to a string (avoid another O(n))
  // Yes we can check the ascii code as alphanumerics are contigious, but irl that's JIT info, not practical to memorise
  const validChars = new Set([
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
  ]);
  const sTransformed: string[] = [];

  for (const char of s) {
    const charFormatted = char.toLowerCase();
    if (validChars.has(charFormatted)) sTransformed.push(charFormatted);
  }
  console.log(sTransformed);

  // INITIAL SOLUTION: Determine mid, and compare moving outwards
  // Determine window starting indexes
  // const isOdd = sTransformed.length % 2 !== 0;
  // const mid = sTransformed.length / 2;
  // let leftWindowIdx = (isOdd ? Math.floor(mid) : mid) - 1; // -1 to start at 0th index
  // let rightWindowIdx = isOdd ? Math.ceil(mid) : mid; // already at valid index

  // // O(n / 2) iterate for the length of either window
  // for (let i = 0; i < Math.floor(mid); i++) {
  //   const leftChar = sTransformed[leftWindowIdx];
  //   const rightChar = sTransformed[rightWindowIdx];

  //   console.log(`Comparing ${leftChar} & ${rightChar}`);

  //   const isNotPalindrome = leftChar !== rightChar;
  //   if (isNotPalindrome) return false;

  //   leftWindowIdx--;
  //   rightWindowIdx++;
  // }

  // SIMPLIFIED SOLUTION: Compare moving inwards until intersection, no mid calcs needed
  let left = 0;
  let right = sTransformed.length - 1;

  // O(n / 2) iterate for the length of a window
  while (left < right) {
    const leftChar = sTransformed[left];
    const rightChar = sTransformed[right];

    console.log(`Comparing ${leftChar} & ${rightChar}`);

    const isNotPalindrome = leftChar !== rightChar;
    if (isNotPalindrome) return false;

    left++;
    right--;
  }

  return true;
}
