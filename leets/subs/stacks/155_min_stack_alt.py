class MinStack:
    """
    See other solution using hashmap (same Big Os)

    ##stacks
    """
    def __init__(self):
        self.stack = []
        self.stack_mins = [] # history of mins corresponding to vals (in self.stack) by index

    def push(self, val: int) -> None:
        currMin = self.stack_mins[-1] if self.stack else None
        nextMin = min(val, currMin) if currMin is not None else val
        self.stack_mins.append(nextMin)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()