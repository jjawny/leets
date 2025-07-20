/**
 * BIG-O:
 *  TIME: O(n)
 *    1x for loop
 *  MEMORY: O(n)
 *    Worst-case stack never needs popping e.g., all open brackets "{{([("
 *
 * Solution w thoughts 💭
 *  #easy #hashmaps #stacks
 */
function isValid(s: string): boolean {
  // 1. Prepare O(1) lookups for specific-pairs
  //    Make closing-brackets the keys to O(1) check for initial guard
  const bracketsHashmap = new Map<string, string>([
    ["}", "{"],
    ["]", "["],
    [")", "("],
  ]);

  // 2. Prepare stack to add opening brackets which should all be closed off (FIFO/push/pop)
  const bracketsStack: string[] = [];

  // 3. Guard: Handle cases that fail immediately
  const isCannotBeClosed = s.length <= 1 || s.length % 2 !== 0 || bracketsHashmap.has(s[0]);
  if (isCannotBeClosed) return false;

  // 4. O(n) over the string
  for (const bracket of s) {
    const openBracketNeeded = bracketsHashmap.get(bracket);
    if (openBracketNeeded) {
      const isClosedSuccessfully = bracketsStack.pop() === openBracketNeeded;
      if (!isClosedSuccessfully) return false;
      continue;
    }
    bracketsStack.push(bracket);
  }

  const isAllClosed = bracketsStack.length === 0;
  return isAllClosed;
}
