import { ListNode } from "../shared/ListNode";

/**
 * Run through (see "x"s) using [0 -> 1 -> 2 -> 3 -> back to 1]
 *
 * TIME: Worst-case O(n) when we reach the end of a singly linked list (hare reaches at O(n/2) but we drop the constant so O(n))
 * MEMORY: Worst-case O(1) since we only use 2 pointers
 *
 * ##linked-lists
 */
function hasCycle(head: ListNode | null): boolean {
  // 3. Guard for edge-case: at least 2 nodes needed for a cycle
  if (!head?.next) return false;

  // 1. This is the classic tortoise n hare problem
  let tortoise: ListNode | null = head;
  let hare: ListNode | null = head?.next;

  // 2. Run until they collide or either has an end/tail (not a cycle)
  while (tortoise.next && hare.next?.next) {
    // x 1st iteration positions: t = 0, h = 1
    // x 2nd iteration positions: t = 1, h = 3
    // x 3rd iteration positions: t = 2, h = 2 (looped back) a MATCH!
    if (tortoise === hare) return true;

    tortoise = tortoise.next;
    hare = hare.next.next;
  }

  return false;
}
