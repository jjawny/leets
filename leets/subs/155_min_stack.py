class MinStack:
    """
    TIME: All ops at O(1)
    MEMORY: Always O(n) - for the stack and corresponding history of min vals (same n for both)

    ##stacks ##hashmaps
    """
    def __init__(self):
        self.inner_stack = []
        # Using a hashmap is implied since getMin op is meant to be O(1)
        #   Indexes (height/length of the stack) are the keys, the mins at each height are the values
        
        # GOTCHA: How do we handle key collisions? using the index means no collisions
        
        # 💡 Realised we could totally just use another stack for the history of mins
        #    which might be a better mental model, the only benefit using the hashmap
        #    is if we needed to access the mins at any point in the history (not just the latest)
        self.history_of_min_per_val_idx = {}

    def push(self, val: int) -> None:
        # Update min val history:
        #   We only need to compare w the last min as the last min
        #   was compared w the previous, etc, etc (so guarenteed to be the smallest)
        #   Python 3.7+ hashmaps (dicts) maintains order but don't support index access
        #   this is fine, we can peek before append to get the latest key (aka the -1 index)
        currHeight = len(self.inner_stack)
        currMin = self.history_of_min_per_val_idx.get(currHeight, None)
        nextHeight = currHeight + 1
        nextMin = min(val, currMin) if currMin is not None else val # GOTCHA: currMin can be 0 so don't truthy check
        self.history_of_min_per_val_idx[nextHeight] = nextMin
        
        # Do the actual push
        self.inner_stack.append(val)

    def pop(self) -> None:
        # Update min val history:
        #   save mem by removing the dead item
        currHeight = len(self.inner_stack)
        if currHeight in self.history_of_min_per_val_idx:
            del self.history_of_min_per_val_idx[currHeight]

        # Do the actual pop
        self.inner_stack.pop()

    def top(self) -> int | None:
        return self.inner_stack[-1] if self.inner_stack else None

    def getMin(self) -> int | None:
        # Easily get the current min val using hashmap lookup O(1)
        currHeight = len(self.inner_stack)
        currMin = self.history_of_min_per_val_idx.get(currHeight, None)
        return currMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()