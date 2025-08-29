# Q restricts us to implementing 1x queue using 2x stacks
# 
# 'deque' from stdlib (collections module) has 3 ops (ignoring appendleft)
#   that support our data structures:
#   - Stack (FILO): append to top (right-side), pop from top (right-side)
#   - Queue (FIFO): append to end (right-side enqueue), popleft (left-side dequeue)

# But use 2x lists as the stacks instead (has same stack ops at ~same perf O(1))
#   and avoids us having an unnecessary dep

# Original idea (successful submission!) was using 1x stack and a frontPtr
#   a rewrite to using 2 stacks means:
#       - queue for in (push at O(1))
#       - queue for out (pop at O(1))
#       - when does out queue get the data?
#           after moving items O(n) from in queue (popping) -> out queue (pushing)
#           which will reverse the order, so popping from out queue is FIFO
#       - self-healing: moving only happens when...
#           user tries to pop AND there's no data left in out queue AND there's
#           some data waiting in in queue
#       - optimizations? if we push 1000_000 items, the next pop will be slow af
#           as move will block for O(1000_000), avoid this by trying to perform the move
#           at every X pushes (like 50?), so worst-case is every 50 pushes w no pops costs
#           a move at O(50) time

class MyQueue:
    """
    OBJECT's STATE MEMORY: O(n) to hold every item (no dupes!)

    #stacks
    """
    MOVE_AFTER_COUNT = 50

    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def push(self, x: int) -> None:
        """
        TIME: O(1) amortized (bcuz of _move)
        MEMORY: O(1) - no additional mem needed
        """
        self.in_queue.append(x)
        if len(self.in_queue) >= self.MOVE_AFTER_COUNT:
            self._move()

    def pop(self) -> int:
        """
        TIME: O(1) amortized (bcuz of _move)
        MEMORY: O(1) - no additional mem needed
        """
        self._move()
        item = self.out_queue.pop()
        return item

    def peek(self) -> int | None:
        """
        TIME: O(1) amortized (bcuz of _move)
        MEMORY: O(1) - no additional mem needed
        """
        self._move()
        item = None if len(self.out_queue) == 0 else self.out_queue[-1]
        return item
        
    def empty(self) -> bool:
        """
        TIME: O(1)
        MEMORY: O(1) - no additional mem needed
        """
        return len(self.in_queue) == 0 and len(self.out_queue) == 0

    def _move(self):
        """
        TIME: O(n) when all n items are yet to be moved (all moved at once to ensure order for FIFO)
        MEMORY: O(1) - no additional mem needed
        """
        if len(self.out_queue) > 0:
            return # need to dequeue all before next move to avoid destroying the order

        while len(self.in_queue) > 0:
            self.out_queue.append(self.in_queue.pop())
