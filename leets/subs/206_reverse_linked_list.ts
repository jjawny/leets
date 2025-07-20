import { ListNode } from "./types/ListNode";

/**
 * BIG-O:
 *  TIME: O(n)
 *    1x while loop
 *  MEMORY: O(1)
 *    In-place reversing, no need for additional data structures
 *
 * Solution w thoughts 💭
 *  #easy #linked-lists
 */
function reverseList(head: ListNode | null): ListNode | null {
  // We will end up return the original LL tail
  // O(n) over the LL
  // Each step will point the current node to the previous node (reversing)

  let prev: ListNode | null = null;
  let curr: ListNode | null = head;

  while (curr) {
    // Save as references will be lost after reversing
    const nextPrev = curr;
    const nextCurr = curr.next;

    // Reverse a single link
    curr.next = prev;

    // Go again
    prev = nextPrev;
    curr = nextCurr;
  }

  return prev;
}
