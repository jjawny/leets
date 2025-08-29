/**
 * BIG-O:
 *  MEMORY: O(n)
 *    Worst-case is it always holds n items (some soft deleted) until internal stack is 'healed'
 *
 * Solution w thoughts 💭
 *  #easy #stacks #queues
 */
class MyQueue {
  // Queues are FIFO
  // Can only use max 2 stacks (a.k.a JS arrays)
  // Can only use standard stack ops [push, peek/pop, size, isEmpty]
  // If not found, return nulls (undefined is better imo #javascript-the-better-parts)
  stack: number[] = [];
  frontIdx: number = 0;
  opsBeforeHealing: number = 15;

  constructor() {}

  // TIME: O(1)
  push(x: number): void {
    this.stack.push(x);
    this.opsBeforeHealing--;
  }

  // TIME: O(1) amortized (average), worst-case is a spike of O(n) when cleaning up the internal stack (recreate)
  pop(): number | null {
    if (this.empty()) return null;
    const front = this.stack[this.frontIdx];
    this.frontIdx++;

    // MEMORY ISSUE
    // If we always slide a pointer for front of queue, the array will never shrink...
    // We can "chop" (copy to new array and replace) after x number of ops
    // A.k.a self-healing

    if (--this.opsBeforeHealing === 0) {
      this.stack = this.stack.slice(this.frontIdx); // slice (start,end]
      this.opsBeforeHealing = 15; // reset
    }

    // BEFORE: 51.64mb beats 18.64%
    // AFTER: 51.42mb beats 44.36%

    return front ?? null;
  }

  // TIME: O(1)
  peek(): number | null {
    return this.stack[this.frontIdx] ?? null;
  }

  // TIME: O(1)
  empty(): boolean {
    return this.stack.length === this.frontIdx;
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
