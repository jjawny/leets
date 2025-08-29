import { ListNode } from "../types/ListNode";

/**
 * BIG-O:
 *  TIME: O(n)
 *  MEMORY: O(1)
 *
 * Solution w thoughts 💭
 *  #easy #hashmaps #linked-lists
 */
function middleNode(head: ListNode | null): ListNode | null {
  // O(n) traversal:
  //  - Count the length
  //  - Save indexes and their nodes
  // const nodeIndexHashmap = new Map<number, ListNode>();

  // let currNode = head;
  // let count = 1;
  // while (currNode) {
  //   nodeIndexHashmap.set(count, currNode);
  //   currNode = currNode.next;
  //   count++;
  // }

  // // Using the length we now know the mid point
  // // Using the hashmap we can O(1) lookup the mid node
  // const mid = Math.ceil(count / 2);
  // const res = nodeIndexHashmap.get(mid) ?? null;
  // return res;

  // OPTIMIZED SOLUTION: O(n) time (1x while loop), O(1) memory (no new data structures used)
  // Optimised memory solution using rabbit & hare
  // Figma diagram simulating odd and even cases (both successful)
  let fast = head;
  let slow = head;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow?.next ?? null; // `= slow.next` is safe bc they both start w head and fast will confirm next is defined, but resolve TS warnings
  }
  return slow;
}
